from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import DrinkOrder, DrinkOrderLineItem
from home.models import Drink
from user_profiles.models import UserProfiles

import json
import time


class StripeWH_Handler:
    # handles stripe webhooks
    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, drink_order):
        # send users confirmation email
        customer_email = drink_order.email
        subject_txt = render_to_string(
            "payment/confirmation_emails/confirmation_email_subject.txt",
            {
                "drink_order": drink_order
            })
        body_txt = render_to_string(
            "payment/confirmation_emails/confirmation_email_body.txt",
            {
                "drink_order": drink_order,
                "contact_email": settings.COMPANY_EMAIL
            })

        send_mail(
            subject_txt,
            body_txt,
            settings.COMPANY_EMAIL,
            [customer_email]
        )

    def handle_event(self, event):
        # handles generic/unknown/unexpected webhook events
        return HttpResponse(
            content=f"Unhandled webhook received: {event['type']}",
            status=200)

    def handle_payment_intent_succeeded(self, event):
        # handles payment_intent.succeeded webhook from stripe
        intent = event.data.object
        pid = intent.id
        shopping_cart = intent.metadata.shopping_cart

        # error REMOVE OTHERWISE
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # clean data in shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # update user profile info when saveInfo is checked
        user_profiles = None
        username = intent.metadata.username
        if username != "AnonymousUser":
            user_profiles = UserProfiles.objects.get(user__username=username)
            if save_info:
                user_profiles.default_phone_number = shipping_details.phone
                user_profiles.default_street_address1 = shipping_details.address.line1
                user_profiles.default_street_address2 = shipping_details.address.line2
                user_profiles.default_postcode = shipping_details.address.postal_code
                user_profiles.default_country = shipping_details.address.country
                user_profiles.save()

        drink_order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                drink_order = DrinkOrder.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    postcode__iexact=shipping_details.address.postal_code,
                    country__iexact=shipping_details.address.country,
                    grand_total=grand_total,
                    original_shopping_cart=shopping_cart,
                    stripe_pid=pid,
                )
                drink_order_exists = True
                break
            except DrinkOrder.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if drink_order_exists:
            self._send_confirmation_email(drink_order)
            return HttpResponse(
                content=f"Webhook received: {event['type']} \
                    | SUCCESS: Verified drink order already in database",
                status=200)
        else:
            drink_order = None
            try:
                drink_order = DrinkOrder.objects.create(
                    full_name=shipping_details.name,
                    user_profiles=user_profiles,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    postcode=shipping_details.address.postal_code,
                    country=shipping_details.address.country,
                    original_shopping_cart=shopping_cart,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(shopping_cart).items():
                    drink = Drink.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        drink_order_line_item = DrinkOrderLineItem(
                            drink_order=drink_order,
                            drink=drink,
                            drink_quantity=item_data,
                        )
                        drink_order_line_item.save()
                    else:
                        for quantity in item_data.items():
                            drink_order_line_item = DrinkOrderLineItem(
                                drink_order=drink_order,
                                drink=drink,
                                drink_quantity=item_data,
                            )
                            drink_order_line_item.save()
            except Exception as e:
                if drink_order:
                    drink_order.delete()
                return HttpResponse(
                    content=f"Webhook received: {event['type']} | ERROR: {e}",
                    status=500)
        self._send_confirmation_email(drink_order)
        return HttpResponse(
            content=f"Webhook received: {event['type']} \
                 | SUCCESS: Created drink order in webhook", status=200)

    def handle_payment_intent_payment_failed(self, event):
        # handles payment_intent.payment_failed webhook from stripe
        return HttpResponse(
            content=f"Webhook received: {event['type']}",
            status=200)

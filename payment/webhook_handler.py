from django.http import HttpResponse


class StripeWH_Handler:
    # handles stripe webhooks
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        # handles generic/unknown/unexpected webhook events
        return HttpResponse(
            content=f"Unhandled webhook received: {event['type']}",
            status=200)

    def handle_payment_intent_succeeded(self, event):
        # handles payment_intent.succeeded webhook from stripe
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f"Webhook received: {event['type']}",
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        # handles payment_intent.payment_failed webhook from stripe
        return HttpResponse(
            content=f"Webhook received: {event['type']}",
            status=200)

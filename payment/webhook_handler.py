from django.http import HttpResponse


class StripeWH_Handler:
    # handles stripe webhooks
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        # handles generic/unknown/unexpected webhook events
        return HttpResponse(
            content=f"Webhook received: {event['type']}",
            status=200)

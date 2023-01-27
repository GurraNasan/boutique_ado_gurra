from django.http import HttpResponse


class StripeWH_Handler:
    """Handel Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled Webhook receved: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment intent succeede dwebhook from strip
        """
        intent = event.data.object
        return HttpResponse(
            content=f'Webhook receved: {event["type"]}',
            status=200)
    
    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment intent payment failed webhook from stripe
        """
        return HttpResponse(
            content=f'Payment failed Webhook receved: {event["type"]}',
            status=200)

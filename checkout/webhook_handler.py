from django.http import HttpResponse

class StripeWH_Handler:
    """Handel Stripe webhooks"""

    def __init__(self,request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook receved: {event("type")}',
            status=200)
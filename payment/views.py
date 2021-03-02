import json
import stripe
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.urls import reverse
from django.views import View
from workshop.models import Pricing, Workshop


stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = "payment/success.html"


class CancelView(TemplateView):
    template_name = "payment/cancel.html"


class ProductLandingPageView(TemplateView):
    template_name = "landing.html"

    def get_context_data(self, **kwargs):
        product = Product.objects.get(name="Test Product")
        context = super(ProductLandingPageView, self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        pricing_value = self.kwargs["pricing_id"]  # Need to be change with real id
        pricing = Pricing.objects.get(price__contains=pricing_value)
        workshop_id = self.kwargs["workshop_id"]
        workshop = Workshop.objects.get(id=workshop_id)
        success_url = request.build_absolute_uri(
            reverse('users:register', kwargs={'workshop_slug': workshop.slug,
                                              'pricing_slug': pricing.slug}))
        success_url += '?session_id={CHECKOUT_SESSION_ID}'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': pricing.get_stripe_price(),
                        'product_data': {
                            'name': pricing.name,
                            'images': ['https://dipy.org/dipy/static/images/dipy-logo.png'],  #['https://dipy.org/dipy/static/images/dipy-favicon.png'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "workshop_id": workshop_id,
            },
            mode='payment',
            success_url=success_url,


            cancel_url=request.build_absolute_uri(
                reverse('workshop:index', kwargs={'workshop_slug': workshop.slug})),
        )
        return JsonResponse({
            'id': checkout_session.id
        })


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        print(settings.STRIPE_WEBHOOK_SECRET)
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )

    except ValueError as e:
        # Invalid payload
        print('Invalid payload : {}'.format(str(e)))
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        print('Invalid signature : {}'.format(str(e)))
        return HttpResponse(status=400)

    # # Handle the checkout.session.completed event
    # if event['type'] == 'checkout.session.completed':
    #     session = event['data']['object']

    #     customer_email = session["customer_details"]["email"]
    #     workshop_id = session["metadata"]["workshop_id"]

    #     workshop = Workshop.objects.get(id=workshop_id)

    #     send_mail(
    #         subject="Welcome to DIPY Workshop {}".format(workshop.year),
    #         message=f"Thanks for your sponsoring DIPY Workshop.",
    #         recipient_list=[customer_email],
    #         from_email="garyfallidis@gmail.com"
    #     )

    #     # TODO - decide whether you want to send the file or the URL

    # elif event["type"] == "payment_intent.succeeded":
    #     intent = event['data']['object']

    #     stripe_customer_id = intent["customer"]
    #     stripe_customer = stripe.Customer.retrieve(stripe_customer_id)

    #     customer_email = stripe_customer['email']
    #     workshop_id = intent["metadata"]["workshop_id"]

    #     workshop = Workshop.objects.get(id=workshop_id)

    #     send_mail(
    #         subject="Welcome to DIPY Workshop {}".format(workshop.year),
    #         message=f"Thanks for your sponsoring DIPY Workshop.",
    #         recipient_list=[customer_email],
    #         from_email="garyfallidis@gmail.com"
    #     )

    return HttpResponse(status=200)


class StripeIntentView(View):
    def post(self, request, *args, **kwargs):
        try:
            req_json = json.loads(request.body)
            customer = stripe.Customer.create(email=req_json['email'])
            pricing_value = self.kwargs["pricing_id"]  # Need to be change with real id
            pricing = Pricing.objects.get(price__contains=pricing_value)
            workshop_id = self.kwargs["workshop_id"]
            workshop = Workshop.objects.get(id=workshop_id)
            intent = stripe.PaymentIntent.create(
                amount=pricing.get_stripe_price(),
                currency='usd',
                customer=customer['id'],
                metadata={
                    "workshop_id": workshop.id
                }
            )
            return JsonResponse({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return JsonResponse({ 'error': str(e) })
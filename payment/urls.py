from django.urls import path
from .views import (StripeIntentView, stripe_webhook, CancelView, SuccessView,
                    ProductLandingPageView, CreateCheckoutSessionView)

app_name = "payment"

urlpatterns = [
    path('create-payment-intent/<workshop_id>/<pricing_id>/', StripeIntentView.as_view(),
         name='create-payment-intent'),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('', ProductLandingPageView.as_view(), name='landing-page'),
    path('create-checkout-session/<workshop_id>/<pricing_id>/', CreateCheckoutSessionView.as_view(),
         name='create-checkout-session')
]

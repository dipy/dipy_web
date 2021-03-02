from urllib.parse import urlparse

from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.shortcuts import render, redirect
# from django.urls import resolve
# from django.urls.base import reverse
from social_django.models import UserSocialAuth

from .forms import UsersRegisterForm, UsersLoginForm
from workshop.models import Subscription, Workshop, Pricing
# from social_core.pipeline
import stripe


def login_view(request):
    form = UsersLoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(username=email, password=password)
        backend = 'users.backends.EmailBackend'
        login(request, user, backend=backend)
        return redirect('website:index')

    context = {'form': form}
    return render(request, 'users/login.html', context)


def register(request, workshop_slug, pricing_slug):
    session_id = request.GET.get('session_id', None)
    initial_data = {}
    if session_id is not None:
        session = stripe.checkout.Session.retrieve(session_id)
        customer = stripe.Customer.retrieve(session.customer)
        initial_data['email'] = customer.email
        initial_data['confirm_email'] = customer.email

    form = UsersRegisterForm(request.POST or None, initial=initial_data)
    workshop = Workshop.objects.get(slug__contains=workshop_slug)
    pricing = Pricing.objects.get(slug__contains=pricing_slug)
    if form.is_valid():
        user = form.save()
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        subscription = Subscription.objects.create(user=user, pricing=pricing)
        if session_id is not None:
            session = stripe.checkout.Session.retrieve(session_id)
            subscription.status = session["payment_status"]  # trialing
            subscription.stripe_session_id = session["id"]
            subscription.payment_intent_id = session["payment_intent"]
        subscription.save()
        workshop.members.add(user)
        return redirect("workshop:eventspace", workshop_slug=workshop.slug)

    context = {}
    context["form"] = form
    context["workshop"] = workshop
    context['pricing'] = pricing
    return render(request, "users/register.html", context)


@login_required
def profile_settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        linkedin_login = user.social_auth.get(provider='linkedin')
    except UserSocialAuth.DoesNotExist:
        linkedin_login = None

    try:
        google_login = user.social_auth.get(provider='google')
    except UserSocialAuth.DoesNotExist:
        google_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'users/profile_settings.html', {
        'github_login': github_login,
        'linkedin_login': linkedin_login,
        'google_login': google_login,
        'can_disconnect': can_disconnect
    })

@login_required
def profile_password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'users/profile_password.html', {'form': form})

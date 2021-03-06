from django.core.mail import send_mail
from urllib.parse import urlencode

from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.urls.base import reverse
from django.shortcuts import redirect
# from django.urls import resolve

from workshop.models import Workshop, Pricing, Subscription


def require_email(strategy, backend, details, is_new=False, user=None, *args, **kwargs):
    if user and user.email:
        return

    elif is_new and not details.get('email'):
        email = strategy.request_data().get('email')
        if email:
            details['email'] = email
            return

        action_type = strategy.session_get('action_type')

        if action_type == 'login':
            base_url = reverse('users:login')
            query_string = urlencode({'show_social_error': True,
                                      'backend': backend.name})
            return redirect(f'{base_url}?{query_string}')

        elif action_type == 'register':
            workshop_id = strategy.session_get('workshop_id')
            pricing_id = strategy.session_get('pricing_id')

            workshop = Workshop.objects.get(id=workshop_id)
            pricing = Pricing.objects.get(id=pricing_id)

            base_url = reverse('users:register',
                               kwargs={'workshop_slug': workshop.slug,
                                       'pricing_slug': pricing.slug})
            query_string = urlencode({'show_social_error': True,
                                      'backend': backend.name})

            return redirect(f'{base_url}?{query_string}')


def add_to_workshop(strategy, backend, details, user=None, *args, **kwargs):
    action_type = strategy.session_get('action_type')
    if action_type == 'register':
        workshop_id = strategy.session_get('workshop_id')
        pricing_id = strategy.session_get('pricing_id')

        workshop = Workshop.objects.get(id=workshop_id)
        pricing = Pricing.objects.get(id=pricing_id)

        subs = Subscription.objects.filter(user=user)
        if not subs.exists():
            subscription = Subscription.objects.create(user=user, pricing=pricing)
            subscription.save()
        # else:
        #     # Todo: manage multiple subscription
        #     subs[0].pricing = pricing
        #     subs[0].save()
        strategy.session_set('is_new_to_workshop', False)
        if user not in workshop.members.all():
            workshop.members.add(user)
            strategy.session_set('is_new_to_workshop', True)

    return


def send_welcome_email(strategy, backend, details, user=None, *args, **kwarg):
    # https://blog.mailtrap.io/django-send-email/
    # https://github.com/leemunroe/responsive-html-email-template
    action_type = strategy.session_get('action_type')
    if action_type == 'register':
        workshop_id = strategy.session_get('workshop_id')
        pricing_id = strategy.session_get('pricing_id')

        workshop = Workshop.objects.get(id=workshop_id)
        _ = Pricing.objects.get(id=pricing_id)

        if user.email:
            context = {'mail_content': workshop.welcome_email_html,
                       'workshop_year': str(workshop.year),
                       'workshop_space_url': workshop.slug,
                       }
            html_message = render_to_string('workshop/welcome_email.html', context)
            plain_message = strip_tags(html_message)
            send_mail(
                subject="Welcome to DIPY Workshop {}".format(workshop.year),
                message=plain_message,
                html_message=html_message,
                recipient_list=[user.email],
                from_email="garyfallidis@gmail.com",
                fail_silently=False,
                )
    return

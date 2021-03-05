from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from workshop.models import Workshop, Pricing, Subscription


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

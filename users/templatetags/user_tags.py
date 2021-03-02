
from django import template
# from django.conf import settings
from users.forms import UsersLoginForm

register = template.Library()


@register.inclusion_tag('users/login.html', takes_context=True)
def show_login(context):
    request = context['request']
    # TODO: check the content of request.POST
    form = UsersLoginForm(request.POST or None)

    print(request.POST)
    print(form.errors)
    return {'form': form}

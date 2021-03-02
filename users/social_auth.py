"""More information: https://rahmonov.me/posts/introduction-to-python-social-auth/ """
from django.conf import settings
from website.views.tools import has_commit_permission

USER_FIELDS = ['username', 'email']


def create_user(strategy, backend, details, user=None, *args, **kwargs):
    if user:
        return {'is_new': False}

    action_type = strategy.session_get('action_type')
    if action_type == 'login':

        if backend.name != 'github':
            return

        try:
            access_token = kwargs.get('response', {}).get('access_token', '')
        except Exception:
            access_token = ''

        has_permission = has_commit_permission(
            access_token, settings.DOCUMENTATION_REPO_NAME)

        if not has_permission:
            return

    fields = dict((name, kwargs.get(name, details.get(name)))
                  for name in backend.setting('USER_FIELDS', USER_FIELDS))
    if not fields:
        return

    return {'is_new': True,
            'user': strategy.create_user(**fields)
            }

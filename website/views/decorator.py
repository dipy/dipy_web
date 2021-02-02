"""Useful decorator function."""

__all__ = []

from .tools import has_commit_permission
from django.conf import settings
from django.core.exceptions import PermissionDenied


def github_permission_required(view_function):
    """
    Decorator for checking github commit permission of users
    """
    def wrapper(request, *args, **kwargs):
        try:
            social = request.user.social_auth.get(provider='github')
            access_token = social.extra_data['access_token']
        except Exception:
            access_token = ''
        has_permission = has_commit_permission(
            access_token, settings.DOCUMENTATION_REPO_NAME)
        if has_permission:
            return view_function(request, *args, **kwargs)
        raise PermissionDenied

    return wrapper

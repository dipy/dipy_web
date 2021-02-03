import re

from django import template
from django.conf import settings
import markdown
from website.views.tools import has_commit_permission

register = template.Library()


# converts all youtube URLs in the text to embed HTML
@register.filter(name='youtube_embed_url')
def youtube_embed_url(value):
    exp = re.compile(r'((http|https)\:\/\/www\.youtube\.com\/watch\?v=([a-zA-Z0-9]*))')
    matches = exp.findall(value)
    processed_str = value
    template = '<div class="youtube-wrapper"><iframe class="youtube-embed" width="640" height="360" \
                src="https://www.youtube.com/embed/%s?rel=0&modestbranding=1" \
                frameborder="0" allowfullscreen></iframe></div>'
    for match in matches:
        processed_str = processed_str.replace(match[0], template % match[2])
    return processed_str


# converts Markdown to HTML
@register.filter(name='markdown_to_html')
def markdown_to_html(value):
    processed_str = markdown.markdown(value, extensions=['codehilite'])
    return processed_str


@register.filter(name='has_gh_permission')
def gh_permission(user):
    try:
        social = user.social_auth.get(provider='github')
        access_token = social.extra_data['access_token']
    except Exception:
        access_token = ''

    has_permission = has_commit_permission(access_token,
                                           settings.DOCUMENTATION_REPO_NAME)
    return has_permission



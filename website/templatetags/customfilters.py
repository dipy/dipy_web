from django import template
import re

register = template.Library()


@register.filter(name='youtube_embed_url')
# converts all youtube URLs in the text to embed HTML
@register.filter(name='youtube_embed_url')
def youtube_embed_url(value):
    exp = re.compile(r'((http|https)\:\/\/www\.youtube\.com\/watch\?v=([a-zA-Z0-9]*))')
    matches = exp.findall(value)
    processed_str = value
    template = '<iframe width="420" height="315" \
                src="https://www.youtube.com/embed/%s" \
                frameborder="0" allowfullscreen></iframe>'
    for match in matches:
        processed_str = processed_str.replace(match[0], template % match[2])
    return processed_str

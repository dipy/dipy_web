import re

from django import template
import markdown

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

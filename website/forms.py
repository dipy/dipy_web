from django.forms import ModelForm
from .models import *


class EditFixedSectionForm(ModelForm):
    class Meta:
        model = WebsiteSection
        fields = ['title', 'body_markdown']


class AddEditPageSectionForm(ModelForm):
    class Meta:
        model = WebsiteSection
        fields = ['title', 'body_markdown',
                  'website_position_id',
                  'show_in_nav']


class AddEditNewsPostForm(ModelForm):
    class Meta:
        model = NewsPost
        fields = ['title', 'body_markdown', 'post_date', 'description']


class AddEditPublicationForm(ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'url', 'author', 'doi', 'entry_type',
                  'published_in', 'publisher', 'year_of_publication',
                  'month_of_publication', 'bibtex']


class AddEditCarouselImageForm(ModelForm):
    class Meta:
        model = CarouselImage
        fields = ['image_url', 'image_caption',
                  'image_description', 'target_url']

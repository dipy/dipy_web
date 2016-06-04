from django.forms import ModelForm
from .models import *


class EditWebsiteSectionForm(ModelForm):
    class Meta:
        model = WebsiteSection
        fields = ['title', 'body_markdown']


class AddWebsiteSectionForm(ModelForm):
    class Meta:
        model = WebsiteSection
        fields = ['title', 'body_markdown',
                  'website_position_id',
                  'website_page']


class AddEditNewsPostForm(ModelForm):
    class Meta:
        model = NewsPost
        fields = ['title', 'body_markdown', 'post_date']


class AddEditPublicationForm(ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'url', 'author', 'doi', 'journal', 'publisher',
                  'year_of_publication', 'month_of_publication', 'bibtex']

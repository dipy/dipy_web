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

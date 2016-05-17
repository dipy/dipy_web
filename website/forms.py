from django.forms import ModelForm
from .models import *


class EditWebsiteSectionForm(ModelForm):
    class Meta:
        model = WebsiteSection
        fields = ['title', 'body_markdown']

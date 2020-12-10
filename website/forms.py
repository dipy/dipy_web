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

    def __init__(self, *args, **kwargs):
        super(AddEditPageSectionForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].widget.attrs.update({
                'style': 'width:80%',
                'class': 'col-lg-10',
            })

class AddEditNewsPostForm(ModelForm):
    class Meta:
        model = NewsPost
        fields = ['title', 'body_markdown', 'post_date', 'description']

    def __init__(self, *args, **kwargs):
        super(AddEditNewsPostForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].widget.attrs.update({
                'style': 'width:80%',
                'class': 'col-lg-10',
            })

class AddEditPublicationForm(ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'url', 'author', 'doi', 'entry_type',
                  'published_in', 'publisher', 'year_of_publication',
                  'month_of_publication', 'bibtex']

    def __init__(self, *args, **kwargs):
        super(AddEditPublicationForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].widget.attrs.update({
                'style': 'width:80%',
                'class': 'col-lg-10',
            })

class AddEditCarouselImageForm(ModelForm):
    class Meta:
        model = CarouselImage
        fields = ['image_url', 'image_caption', 'is_visible', 'priority',
                  'image_description', 'target_url']

    def __init__(self, *args, **kwargs):
        super(AddEditCarouselImageForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].widget.attrs.update({
                'style': 'width:80%',
                'class': 'col-lg-10',
            })

class AddEditSponsorImageForm(ModelForm):
    class Meta:
        model = SponsorImage
        fields = ['image_url', 'image_caption', 'is_visible',
                  'image_description', 'target_url']

    def __init__(self, *args, **kwargs):
        super(AddEditSponsorImageForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].widget.attrs.update({
                # 'style': 'width:80%',
                'class': 'col-lg-4',
            })

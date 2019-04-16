import pytest
from ..forms import EditFixedSectionForm, AddEditPageSectionForm, \
    AddEditNewsPostForm, AddEditPublicationForm, AddEditCarouselImageForm
from django.utils import timezone

# Todo: test POST and submit button


def test_init_form():
    assert EditFixedSectionForm()
    assert AddEditPageSectionForm()
    assert AddEditNewsPostForm()
    assert AddEditPublicationForm()
    assert AddEditCarouselImageForm()  # entry=self.entry)


@pytest.mark.django_db(transaction=False)
def test_edit_fixed_section_form():

    # Test Valid Data
    form = EditFixedSectionForm({
        'title': 'My test',
        'body_markdown': 'This is a test!',
    })
    assert form.is_valid()

    section = form.save()
    assert section.title == 'My test'
    assert section.body_markdown == 'This is a test!'

    # Test Empty Data
    form = AddEditPageSectionForm({})
    assert not form.is_valid()
    assert form.errors == {'title': ['This field is required.'],
                           'body_markdown': ['This field is required.'],
                           'website_position_id': ['This field is required.']
                           }


@pytest.mark.django_db(transaction=False)
def test_add_edit_page_section_form():
    # Test Valid Data
    form = AddEditPageSectionForm({
        'title': 'My test',
        'body_markdown': 'This is a test!',
        'show_in_nav': True,
        'website_position_id': '1'
    })
    assert form.is_valid()

    section = form.save()
    assert section.title == 'My test'
    assert section.body_markdown == 'This is a test!'
    assert section.show_in_nav
    assert section.website_position_id == '1'

    # Test Empty Data
    form = AddEditPageSectionForm({})
    assert not form.is_valid()
    assert form.errors == {'title': ['This field is required.'],
                           'body_markdown': ['This field is required.'],
                           'website_position_id': ['This field is required.']
                           }


@pytest.mark.django_db(transaction=False)
def test_add_edit_news_post_form():
    # Test Valid Data
    now = timezone.now()
    form = AddEditNewsPostForm({
        'title': 'My test',
        'body_markdown': 'This is a test!',
        'post_date': now,
        'description': 'a short test description'
    })
    assert form.is_valid()

    section = form.save()
    assert section.title == 'My test'
    assert section.body_markdown == 'This is a test!'
    assert section.post_date == now
    assert section.description == 'a short test description'

    # Test Empty Data
    form = AddEditNewsPostForm({})
    assert not form.is_valid()
    assert form.errors == {'title': ['This field is required.'],
                           'body_markdown': ['This field is required.'],
                           'post_date': ['This field is required.'],
                           'description': ['This field is required.'],
                           }


@pytest.mark.django_db(transaction=False)
def test_add_edit_publication_form():
    # Test Valid Data
    form = AddEditPublicationForm({
        'title': 'My test',
        'url': 'my/publication/test.pdf',
        'author': 'me',
        'doi': '1',
        'entry_type': 'pdf',
        'published_in': 'fontiers',
        'publisher': 'IEEE',
        'year_of_publication': '2017',
        'month_of_publication': 'August',
        'bibtex': 'test.bib'
    })
    assert form.is_valid()

    section = form.save()
    assert section.title == 'My test'
    assert section.url == 'my/publication/test.pdf'
    assert section.author == 'me'
    assert section.doi == '1'
    assert section.entry_type == 'pdf'
    assert section.published_in == 'fontiers'
    assert section.publisher == 'IEEE'
    assert section.year_of_publication == '2017'
    assert section.month_of_publication == 'August'
    assert section.bibtex == 'test.bib'

    # Test Empty Data
    form = AddEditPublicationForm({})
    assert not form.is_valid()
    assert form.errors == {'title': ['This field is required.'],
                           'url': ['This field is required.'],
                           'author': ['This field is required.']
                           }


@pytest.mark.django_db(transaction=False)
def test_add_edit_carousel_image_form():
    # Test Valid Data
    form = AddEditCarouselImageForm({
        'image_url': 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_120x44dp.png',
        'image_caption': 'My test',
        'image_description': 'a short test description',
        'target_url': 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_120x44dp.png',
    })
    assert form.is_valid()

    section = form.save()
    assert section.image_caption == 'My test'
    assert section.image_url == 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_120x44dp.png'
    assert section.target_url == 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_120x44dp.png'
    assert section.image_description == 'a short test description'

    # Test Empty Data
    form = AddEditCarouselImageForm({})
    assert not form.is_valid()
    assert form.errors == {'image_caption': ['This field is required.'],
                           'image_url': ['This field is required.'],
                           }


# def test_init_form_without_entry():
#     with pytest.raises(KeyError) as e_info:
#         assert EditFixedSectionForm()
#         assert AddEditPageSectionForm()
#         assert AddEditNewsPostForm()
#         assert AddEditPublicationForm()
#         assert AddEditCarouselImageForm()
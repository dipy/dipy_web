import pytest
import time
from distutils.version import LooseVersion
from django.utils import timezone
from ..models import Profile, WebsiteSection, NewsPost, \
    Publication, CarouselImage, DocumentationLink


def test_string_representation(random_user):
    entry = WebsiteSection(title="My entry title")
    assert str(entry) == entry.title

    entry = NewsPost(title="My entry title")
    assert str(entry) == entry.title

    entry = Publication(title="My entry title")
    assert str(entry) == entry.title

    entry = CarouselImage(image_url="/my/image/url/test.png")
    assert str(entry) == entry.image_url

    entry = DocumentationLink(url="/my/doc/url/test.html")
    assert str(entry) == entry.url

    entry = Profile(user=random_user)
    assert str(entry) == random_user.get_username()


@pytest.mark.django_db(transaction=False)
def test_profile(random_user):
    random_user.save()
    custom_profile = Profile.objects.create(user=random_user)

    assert custom_profile.user.get_full_name() == 'John Doe'
    assert custom_profile.user.get_username() == 'J-D'
    assert custom_profile.user.get_short_name() == 'John'
    assert custom_profile.user.check_password('pwd_test2!')

    # Todo: create other profile and compare them


@pytest.mark.django_db(transaction=False)
def test_website_section():
    now = timezone.now()
    section_2 = WebsiteSection.objects.create(title='test1',
                                              body_markdown='useful test',
                                              website_position_id='start 1',
                                              section_type='page',
                                              show_in_nav=True)

    assert section_2.title == 'test1'
    assert section_2.body_markdown == 'useful test'
    assert section_2.body_html == '<p>useful test</p>'
    assert section_2.section_type == 'page'
    assert section_2.show_in_nav
    time.sleep(1)
    section_3 = WebsiteSection.objects.create(title='test2',
                                              body_markdown='another test',
                                              website_position_id='start 2',
                                              section_type='page',
                                              show_in_nav=False)
    assert section_2.created.date() == now.date()
    assert section_3.created.date() == now.date()
    assert section_3.created.date() == section_2.created.date()
    assert section_3.created > section_2.created
    assert len(WebsiteSection.objects.all()) == 2
    assert WebsiteSection.objects.get(title='test1').show_in_nav
    assert not WebsiteSection.objects.get(title='test2').show_in_nav

    time.sleep(1)
    # check modified
    assert section_2.modified < section_3.modified
    assert section_2.created < section_3.created
    section_2.title = 'test1 modified'
    section_2.body_markdown = 'another test'
    section_2.save()
    assert section_2.modified > section_3.modified
    assert section_2.created < section_3.created
    assert section_2.body_html == section_3.body_html
    assert WebsiteSection.objects.get(website_position_id='start 1').title == section_2.title


@pytest.mark.django_db(transaction=False)
def test_news_post():
    now = timezone.now()
    post_1 = NewsPost.objects.create(title='Welcome',
                                     body_markdown='useful post',
                                     description='start 1',
                                     )

    assert post_1.title == 'Welcome'
    assert post_1.body_markdown == 'useful post'
    assert post_1.body_html == '<p>useful post</p>'
    assert post_1.description == 'start 1'
    assert post_1.post_date.date() == now.date()
    assert post_1.created.date() == now.date()
    assert post_1.modified.date() == now.date()

    time.sleep(1)

    post_2 = NewsPost.objects.create(title='Good Morning',
                                     body_markdown='another test',
                                     description='start 2',
                                     )
    assert post_2.created.date() == now.date()
    assert post_2.created.date() == now.date()
    assert post_2.created.date() == post_1.created.date()
    assert post_2.created > post_1.created
    assert len(NewsPost.objects.all()) == 2

    time.sleep(1)
    # check modified
    assert post_1.modified < post_2.modified
    assert post_1.created < post_2.created
    post_1.title = 'Welcome modified'
    post_1.body_markdown = 'another test'
    post_1.save()
    assert post_1.modified > post_2.modified
    assert post_1.created < post_2.created
    assert post_1.body_html == post_2.body_html
    assert NewsPost.objects.get(description='start 1').title == post_1.title


def test_publication():
    pass


@pytest.mark.django_db(transaction=False)
def test_carousel_image():
    now = timezone.now()
    im_1 = CarouselImage.objects.create(image_caption='Welcome',
                                        image_description='useful image',
                                        target_url='/my/image/test.pmg',
                                        image_url='../../test.png',
                                        display_description='hey',
                                        )

    assert im_1.image_caption == 'Welcome'
    assert im_1.image_description == 'useful image'
    assert im_1.target_url == '/my/image/test.pmg'
    assert im_1.display_description == 'hey'
    assert im_1.image_url == '../../test.png'
    assert im_1.created.date() == now.date()
    assert im_1.modified.date() == now.date()

    time.sleep(1)

    im_2 = CarouselImage.objects.create(image_caption='Good Morning',
                                        image_description='another test',
                                        target_url='',
                                        image_url='',
                                        display_description='hey you',
                                        )
    assert im_2.created.date() == now.date()
    assert im_2.created.date() == now.date()
    assert im_2.created.date() == im_1.created.date()
    assert im_2.created > im_1.created
    assert len(CarouselImage.objects.all()) == 2

    time.sleep(1)
    # check modified
    assert im_1.modified < im_2.modified
    assert im_1.created < im_2.created
    im_1.image_caption = 'Welcome modified'
    im_1.image_description = 'another test'
    im_1.save()
    assert im_1.modified > im_2.modified
    assert im_1.created < im_2.created


@pytest.mark.django_db(transaction=False)
def test_documentation_link():
    doc_1 = DocumentationLink.objects.create(version='0.1.0',
                                             url='/my/url/local.html',
                                             displayed=True,
                                             )

    assert doc_1.version == '0.1.0'
    assert doc_1.url == '/my/url/local.html'
    assert doc_1.displayed

    doc_2 = DocumentationLink.objects.create(version='0.2.0',
                                             url='/my/url/local_2.html',
                                             displayed=False,
                                             )
    assert len(DocumentationLink.objects.all()) == 2

    doc_1.version = '0.3.0'
    doc_1.save()
    assert LooseVersion(doc_1.version) > LooseVersion(doc_2.version)
    assert DocumentationLink.objects.get(url='/my/url/local.html').version == doc_1.version

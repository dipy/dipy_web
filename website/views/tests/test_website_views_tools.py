import pytest
from django.utils import timezone
from ...models import Profile, WebsiteSection, NewsPost, \
    Publication, CarouselImage, DocumentationLink

import website.views.tools as tools


@pytest.mark.django_db(transaction=False)
def test_get_website_section():

    section = WebsiteSection.objects.create(title='test2',
                                            body_markdown='another test',
                                            website_position_id='start 2',
                                            section_type='page',
                                            show_in_nav=False)

    desired_section = tools.get_website_section('start 2')
    assert section.title == desired_section.title
    assert section.body_markdown == desired_section.body_markdown
    assert section.section_type == desired_section.section_type
    assert section.show_in_nav == desired_section.show_in_nav

    # Test if we get an error when section does not exist
    desired_section = tools.get_website_section('')
    assert desired_section is None
    desired_section = tools.get_website_section('Not existing section')
    assert desired_section is None


@pytest.mark.django_db(transaction=False)
def test_get_latest_news_posts():

    # Try to get news from empty database.
    latest_news = list(tools.get_latest_news_posts(2))
    assert not latest_news

    # fill database with many fake news
    news_post_list = [NewsPost.objects.create(title='Welcome {}'.format(i),
                                              body_markdown='useful post {}'.format(i),
                                              description='start {}'.format(i),
                                              post_date=(timezone.now()+timezone.timedelta(days=i)),
                                              )
                      for i in range(10)]

    # Check consistency with int value
    latest_news = list(tools.get_latest_news_posts(2))
    assert latest_news[0].title == news_post_list[-1].title
    assert latest_news[1].title == news_post_list[-2].title

    # check error with negatives values
    with pytest.raises(AssertionError) as excinfo:
        _ = list(tools.get_latest_news_posts(-8))
    assert excinfo.match(r'.*Negative indexing.*')

    # check error with str values
    with pytest.raises(TypeError) as excinfo:
        _ = list(tools.get_latest_news_posts('3'))
    assert excinfo.match(r".* 'str' and 'int'.*")


def test_has_commit_permission():

    # empty token
    has_permission = tools.has_commit_permission('', 'dipy_web')
    assert not has_permission

    # Todo:  find a way to get a valid token
    # access_token = ?
    # has_permission = tools.has_commit_permission(access_token, 'dipy_web')
    # assert not has_permission


def test_get_google_plus_activity():
    # Todo: define a random public user activity
    pass


def test_get_facebook_page_feed():
    # Todo: get a random public user page
    pass


def test_get_twitter_bearer_token():
    # Todo: get a random public user twitter account
    pass


def test_get_twitter_feed():
    # Todo: get a random public user twitter account
    pass


@pytest.mark.django_db(transaction=False)
def test_update_documentations():
    # Check if we have at least one doc version
    _ = tools.update_documentations()
    all_doc_links = DocumentationLink.objects.all()
    assert all_doc_links

    # Todo: Add random doc in databases


def test_get_meta_tags_dict(settings):
    default_meta = tools.get_meta_tags_dict()
    assert default_meta.title == settings.DEFAULT_TITLE
    assert default_meta.description == settings.DEFAULT_DESCRIPTION
    assert default_meta.keywords == settings.DEFAULT_KEYWORDS
    assert default_meta.url == "{}://{}{}".format(settings.META_SITE_PROTOCOL, settings.META_SITE_DOMAIN, "/")
    assert default_meta.image == settings.DEFAULT_LOGO_URL
    assert default_meta.object_type == "website"
    assert default_meta.use_og
    assert default_meta.use_twitter
    assert default_meta.use_facebook
    assert default_meta.use_googleplus
    assert default_meta.use_title_tag

    new_meta = tools.get_meta_tags_dict(title="my meta",
                                        description="random description",
                                        keywords=["TEST", "META"],
                                        url="/images/",
                                        object_type="page"
                                        )
    assert new_meta.title == "my meta"
    assert new_meta.description == "random description"
    assert "TEST" in new_meta.keywords
    assert new_meta.url == "{}://{}{}".format(settings.META_SITE_PROTOCOL, settings.META_SITE_DOMAIN, "/images/")
    assert new_meta.image == settings.DEFAULT_LOGO_URL
    assert new_meta.object_type == "page"


def test_get_youtube_videos():
    # Todo: get a random public user youtube account
    # Todo: Check why count is not use
    pass


@pytest.mark.django_db(transaction=False)
def test_get_examples_list_from_li_tags():
    # _ = tools.update_documentations()
    # base_url = 'https://raw.githubusercontent.com/ghoshbishakh/dipy_web/gh-pages/'
    # version = '0.12.0.dev'
    # path = 'examples_index'
    # Todo: create a beautifull soup element instead of the following all_li
    # all_li = ['<li><a class="reference internal" href="../examples_built/quick_start/#example-quick-start">'
    #           '<span class="std std-ref">Getting started with Dipy</span></a></li>',
    #          '<li><a class="reference internal" href="../examples_built/tracking_quick_start/#example-tracking-quick-start">'
    #          '<span class="std std-ref">Tracking Quick Start</span></a></li>']
    #
    # example = tools.get_examples_list_from_li_tags(base_url, version, path, all_li)
    # print(example)
    pass


@pytest.mark.django_db(transaction=False)
def test_get_doc_examples():
    # Check with empty databases
    example = tools.get_doc_examples()
    assert not example

    _ = tools.update_documentations()
    examples = tools.get_doc_examples()
    assert len(examples) > 10
    # Check if we have 2 quickstart
    assert len(examples[0]) == 4
    assert 'quick start' in examples[0]['title'].lower()
    assert 'getting started' in examples[0]['examples_list'][0]['title'].lower()
    assert 'tracking' in examples[0]['examples_list'][1]['title'].lower()


@pytest.mark.django_db(transaction=False)
def test_get_doc_examples_images():
    example = tools.get_doc_examples_images()
    assert not example

    _ = tools.update_documentations()
    examples = tools.get_doc_examples()
    examples_images = tools.get_doc_examples_images()
    assert len(examples) < len(examples_images)

import pytest
import website.views.pages as wvp
import website.models as models
from django.core.urlresolvers import reverse, resolve


def test_index(rf, client, admin_client):
    response = client.post(reverse('index'), data={})
    assert response.status_code == 200

    defaults_key_list = ['home_header', 'getting_started', 'latest_news', 'highlighted_publications', 'all_carousel',
                         'gplus_feed', 'fb_posts', 'tweets', 'meta']

    current_key_list = response.context.keys()
    for k in defaults_key_list:
        assert k in current_key_list


@pytest.mark.django_db(transaction=False)
def test_page(client):
    response = client.post(reverse('section_page', args=('start 1', )), data={})
    assert response.status_code == 400  # it should be a 404 error

    section = models.WebsiteSection.objects.create(title='test1',
                                                   body_markdown='useful test',
                                                   website_position_id='start 1',
                                                   section_type='page',
                                                   show_in_nav=True)

    response = client.post(reverse('section_page', args=('start 1', )), data={})
    assert response.status_code == 200
    assert response.context['section'].title == section.title


def test_cite():
    pass


def test_honeycomb():
    pass


def test_tutorials():
    pass


def test_support():
    pass


def test_follow_us():
    pass


def test_news_page():
    pass


def test_contributors():
    pass


def test_dashboard():
    pass


def test_dashboard_login():
    pass


def test_custom404():
    pass


def test_custom500():
    pass

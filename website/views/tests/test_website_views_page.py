import website.views.pages as wvp
from django.core.urlresolvers import reverse, resolve


def test_index(rf, client, admin_client):
    response = client.post(reverse('index'), data={})
    assert response.status_code == 200

    defaults_key_list = ['home_header', 'getting_started', 'latest_news', 'highlighted_publications', 'all_carousel',
                         'gplus_feed', 'fb_posts', 'tweets', 'meta']

    current_key_list = response.context.keys()
    for k in defaults_key_list:
        assert k in current_key_list


def test_page():
    pass


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

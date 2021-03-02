import pytest
from django.core.urlresolvers import reverse, resolve


def test_home_page_url(client, admin_client):
    response = admin_client.get(reverse('index'))
    assert response.status_code == 200

    response = client.get(reverse('index'))
    assert response.status_code == 200

    assert resolve('/').view_name == 'index'


def test_section_page_url(client, admin_client):
    # Todo: use db to test with a existing page or create it
    # Todo : Understand why we get a 400 instead of 404

    response = admin_client.get(reverse('section_page', args=['installation', ]))
    assert response.status_code == 400

    response = client.get(reverse('section_page', args=['installation', ]))
    assert response.status_code == 400

    assert resolve('/page/installation/').view_name == 'section_page'


def test_cite_page_url(client, admin_client):
    response = admin_client.get(reverse('cite'))
    assert response.status_code == 200

    response = client.get(reverse('cite'))
    assert response.status_code == 200

    assert resolve('/cite/').view_name == 'cite'


def test_news_page_url(client, admin_client):
    # Todo: use db to test with a existing news or create it
    # Todo : Understand why we get a 400 instead of 404

    response = admin_client.get(reverse('news_page', args=['01', ]))
    assert response.status_code == 400

    response = client.get(reverse('news_page', args=['01', ]))
    assert response.status_code == 400

    assert resolve('/news/01/').view_name == 'news_page'


def test_support_page_url(client, admin_client):
    response = admin_client.get(reverse('support'))
    assert response.status_code == 200

    response = client.get(reverse('support'))
    assert response.status_code == 200

    assert resolve('/support/').view_name == 'support'


def test_follow_us_page_url(client, admin_client):
    response = admin_client.get(reverse('follow_us'))
    assert response.status_code == 200

    response = client.get(reverse('follow_us'))
    assert response.status_code == 200

    assert resolve('/follow/').view_name == 'follow_us'


def test_contributors_page_url(client, admin_client):
    response = admin_client.get(reverse('contributors'))
    assert response.status_code == 200

    response = client.get(reverse('contributors'))
    assert response.status_code == 200

    assert resolve('/contributors/').view_name == 'contributors'


def test_dashboard_page_url(client, admin_client):
    response = admin_client.get(reverse('dashboard'))
    assert response.status_code == 200

    response = client.get(reverse('dashboard'))
    assert response.status_code == 302

    assert resolve('/dashboard/').view_name == 'dashboard'


# Todo: Add tutorial and examples on databases for this both test
# @pytest.mark.django_db(transaction=False)
# def test_honeycomb_gallery_url(client, admin_client):
#     response = admin_client.get(reverse('gallery'))
#     assert response.status_code == 200
#
#     response = client.get(reverse('gallery'))
#     assert response.status_code == 200
#
#     assert resolve('/gallery/').view_name == 'gallery'
#
#
# @pytest.mark.django_db(transaction=False)
# def test_tutorials_page_url(client, admin_client):
#     response = admin_client.get(reverse('website:tutorials'))
#     assert response.status_code == 200
#
#     response = client.get(reverse('website:tutorials'))
#     assert response.status_code == 200
#
#     assert resolve('/tutorials/').view_name == 'tutorials'


def test_documentation_pages_url(client, admin_client):
    response = admin_client.get(reverse('documentation', args=['0.12.0.dev', 'documentation']))
    assert response.status_code == 200

    response = client.get(reverse('documentation', args=['0.12.0.dev', 'documentation']))
    assert response.status_code == 200

    assert resolve('/documentation/0.12.0.dev/documentation/').view_name == 'documentation'


def test_login_page_url(client, admin_client):
    response = admin_client.get(reverse('dashboard_login'))
    assert response.status_code == 200

    response = client.get(reverse('dashboard_login'))
    assert response.status_code == 200

    assert resolve('/dashboard/login/').view_name == 'dashboard_login'


def test_section_page_management_url(client, admin_client):
    # Todo: more tests with logged user
    # Test Edit page
    response = admin_client.get(reverse('edit_website_section', args=['fixed', '01']))
    assert response.status_code == 403  # Forbidden -> not in github super user

    response = client.get(reverse('edit_website_section', args=['fixed', '01']))
    assert response.status_code == 302  # redirect to login page

    assert resolve('/dashboard/sections/edit/fixed/01/').view_name == 'edit_website_section'

    # Test Add page
    response = admin_client.get(reverse('add_website_page'))
    assert response.status_code == 403  # Forbidden -> not in github super user

    response = client.get(reverse('add_website_page'))
    assert response.status_code == 302  # redirect to login page

    assert resolve('/dashboard/sections/add/').view_name == 'add_website_page'

    # Test Delete Page
    response = admin_client.get(reverse('delete_website_page', args=['01']))
    assert response.status_code == 403  # Forbidden -> not in github super user

    response = client.get(reverse('delete_website_page', args=['01']))
    assert response.status_code == 302  # redirect to login page

    assert resolve('/dashboard/sections/delete/01/').view_name == 'delete_website_page'

    # Test sections page
    response = admin_client.get(reverse('dashboard_sections', args=['01']))
    assert response.status_code == 400

    response = client.get(reverse('dashboard_sections', args=['01']))
    assert response.status_code == 302  # redirect to login page

    assert resolve('/dashboard/sections/01/').view_name == 'dashboard_sections'


def test_news_management_url(client, admin_client):
    # Todo: more tests with logged user
    # Test Edit page
    response = admin_client.get(reverse('edit_news_post', args=['01']))
    assert response.status_code == 403  # Forbidden -> not in github super user

    response = client.get(reverse('edit_news_post', args=['01']))
    assert response.status_code == 302  # redirect to login page

    assert resolve('/dashboard/news/edit/01/').view_name == 'edit_news_post'

    # Test Add page
    response = admin_client.get(reverse('add_news_post'))
    assert response.status_code == 403  # Forbidden -> not in github super user

    response = client.get(reverse('website:add_news_post'))
    assert response.status_code == 302  # redirect to login page

    assert resolve('/dashboard/news/add/').view_name == 'add_news_post'

    # Test Delete Page
    response = admin_client.get(reverse('delete_news_post', args=['01']))
    assert response.status_code == 403  # Forbidden -> not in github super user

    response = client.get(reverse('delete_news_post', args=['01']))
    assert response.status_code == 302  # redirect to login page

    assert resolve('/dashboard/news/delete/01/').view_name == 'delete_news_post'

    # Test news page
    response = admin_client.get(reverse('dashboard_news'))
    assert response.status_code == 403  # Forbidden -> not in github super user

    response = client.get(reverse('dashboard_news'))
    assert response.status_code == 302  # redirect to login page

    assert resolve('/dashboard/news/').view_name == 'dashboard_news'


def test_publication_management_url(client, admin_client):
    # Todo: more tests with logged user
    # Test Edit page
    response = admin_client.get(reverse('edit_publication', args=['01']))
    assert response.status_code == 403  # Forbidden -> not in github super user

    response = client.get(reverse('edit_publication', args=['01']))
    assert response.status_code == 302  # redirect to login page

    assert resolve('/dashboard/publications/edit/01/').view_name == 'edit_publication'

    # Test Add page
    response = admin_client.get(reverse('add_publication', args=['bibtex']))
    assert response.status_code == 403  # Forbidden -> not in github super user

    response = client.get(reverse('add_publication', args=['bibtex']))
    assert response.status_code == 302  # redirect to login page

    assert resolve('/dashboard/publications/add/bibtex/').view_name == 'add_publication'

    # Test Delete Page
    response = admin_client.get(reverse('delete_publication', args=['01']))
    assert response.status_code == 403  # Forbidden -> not in github super user

    response = client.get(reverse('delete_publication', args=['01']))
    assert response.status_code == 302  # redirect to login page

    assert resolve('/dashboard/publications/delete/01/').view_name == 'delete_publication'

    # Test publication page
    response = admin_client.get(reverse('dashboard_publications'))
    assert response.status_code == 403  # Forbidden -> not in github super user

    response = client.get(reverse('dashboard_publications'))
    assert response.status_code == 302  # redirect to login page

    assert resolve('/dashboard/publications/').view_name == 'dashboard_publications'

    # Test highlight page
    response = admin_client.get(reverse('highlight_publications'))
    assert response.status_code == 403  # Forbidden -> not in github super user

    response = client.get(reverse('highlight_publications'))
    assert response.status_code == 302  # redirect to login page

    assert resolve('/dashboard/publications/highlight/').view_name == 'highlight_publications'


def test_carousel_management_url(client, admin_client):
    # Todo: more tests with logged user
    # Test Edit page
    response = admin_client.get(reverse('edit_carousel_image', args=['01']))
    assert response.status_code == 403  # Forbidden -> not in github super user

    response = client.get(reverse('edit_carousel_image', args=['01']))
    assert response.status_code == 302  # redirect to login page

    assert resolve('/dashboard/carousel/edit/01/').view_name == 'edit_carousel_image'

    # Test Add page
    response = admin_client.get(reverse('add_carousel_image'))
    assert response.status_code == 403  # Forbidden -> not in github super user

    response = client.get(reverse('add_carousel_image'))
    assert response.status_code == 302  # redirect to login page

    assert resolve('/dashboard/carousel/add/').view_name == 'add_carousel_image'

    # Test Delete Page
    response = admin_client.get(reverse('delete_carousel_image', args=['01']))
    assert response.status_code == 403  # Forbidden -> not in github super user

    response = client.get(reverse('delete_carousel_image', args=['01']))
    assert response.status_code == 302  # redirect to login page

    assert resolve('/dashboard/carousel/delete/01/').view_name == 'delete_carousel_image'

    # Test carousel page
    response = admin_client.get(reverse('dashboard_carousel'))
    assert response.status_code == 403  # Forbidden -> not in github super user

    response = client.get(reverse('dashboard_carousel'))
    assert response.status_code == 302  # redirect to login page

    assert resolve('/dashboard/carousel/').view_name == 'dashboard_carousel'


def test_documentation_management(client, admin_client):
    # Todo: more tests with logged user
    # Test documentation page
    response = admin_client.get(reverse('dashboard_documentation'))
    assert response.status_code == 403  # Forbidden -> not in github super user

    response = client.get(reverse('dashboard_documentation'))
    assert response.status_code == 403  # redirect to login page

    assert resolve('/dashboard/documentation/').view_name == 'dashboard_documentation'

    # Test update documentation page
    response = admin_client.get(reverse('update_documentation'))
    assert response.status_code == 302  # Forbidden -> not in github super user

    response = client.get(reverse('update_documentation'))
    assert response.status_code == 302  # redirect to login page

    assert resolve('/dashboard/documentation/update/').view_name == 'update_documentation'


#
# # social login urls(client, admin_client):
# url('', include('social.apps.django_app.urls', namespace='social')),
#
# # logout url(client, admin_client):
# url(r'^dashboard/logout/$', logout,
#     {'next_page': '/'})

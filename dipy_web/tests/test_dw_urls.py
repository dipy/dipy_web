import pytest
from django.core.urlresolvers import reverse

def test_an_admin_url(client, admin_client):
    response = admin_client.get('/admin/')
    assert response.status_code == 200

    response = client.get('/admin/')
    assert response.status_code == 302


@pytest.mark.django_db(transaction=False)
def test_home_url(client, admin_client):
    response = client.get('/')
    assert response.status_code == 200

    response = admin_client.get('/')
    assert response.status_code == 200


@pytest.mark.django_db(transaction=False)
def test_home_url(client, admin_client):
    response = client.get('/pagedoesnotexist/')
    assert response.status_code == 400

    response = admin_client.get('/pagedoesnotexist/')
    assert response.status_code == 400

# @pytest.mark.django_db(transaction=False)
# def test_language_using_cookie(settings, client):
#     client.cookies.load({settings.LANGUAGE_COOKIE_NAME: 'fr'})
#     response = client.get('/')
#     print(response['meta'])
#     assert response.content == b"Bienvenue sur mon site."

# def test_language_using_header(settings, client):
#     response = client.get('/', HTTP_ACCEPT_LANGUAGE='fr')
#     print(response)
#     assert response.content == b"Bienvenue sur mon site."

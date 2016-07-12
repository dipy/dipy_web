import base64
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
import os
import requests
from meta.views import Meta

from website.models import *


# Definition of functions:

def get_website_section(requested_website_position_id):
    """
    Fetch WebsiteSection with website_position_id

    Parameters
    ----------
    website_position_id : string

    Output
    ------
    returns WebsiteSection object or None if not found
    """
    try:
        section = WebsiteSection.objects.get(
            website_position_id=requested_website_position_id)
    except ObjectDoesNotExist:
        section = None
    return section


def get_latest_news_posts(limit):
    """
    Fetch Latest NewsPosts according to post_date

    Parameters
    ----------
    limit : string

    Output
    ------
    returns a list of NewsPost objects
    """
    return NewsPost.objects.order_by('-post_date')[0:limit]


def has_commit_permission(access_token, repository_name):
    """
    Determine if user has commit access to the repository in nipy organisation.

    Parameters
    ----------
    access_token : string
        GitHub access token of user.
    repository_name : string
        Name of repository to check if user has commit access to it.
    """
    if access_token == '':
        return False
    response = requests.get('https://api.github.com/orgs/nipy/repos',
                            params={'access_token': access_token})
    response_json = response.json()
    for repo in response_json:
        if(repo["name"] == repository_name):
            permissions = repo["permissions"]
            if(permissions["admin"] and
               permissions["push"] and
               permissions["pull"]):
                return True
    return False


def get_google_plus_activity(user_id, count):
    """
    Fetch google plus activity list of a user

    Parameters
    ----------
    user_id : string
        The ID of the user to get activities for.

    count: int
        Maximum number of activities to fetch.
    """
    url = "https://www.googleapis.com/plus/v1/people/" + user_id + "/activities/public?maxResults=" + str(count) + "&fields=etag%2Cid%2Citems%2Ckind%2CnextLink%2CnextPageToken%2CselfLink%2Ctitle%2Cupdated&key=AIzaSyA0dPfkGKCzEWJz9INBYslY25MC-M4NG7s"
    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        return {}
    json_response = r.json()
    if 'error' not in json_response:
        return json_response['items']
    else:
        print(json_response)
        return {}


def get_facebook_page_feed(page_id, count):
    """
    Fetch the feed of posts published by this page, or by others on this page.

    Parameters
    ----------
    page_id : string
        The ID of the page.
    count: int
        Maximum number of posts to fetch.
    """
    app_id = settings.FACEBOOK_APP_ID
    app_secret = settings.FACEBOOK_APP_SECRET

    params = (page_id, count, app_id, app_secret)
    url = ("https://graph.facebook.com/%s/feed?limit=%s&access_token=%s|%s" %
           params)
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        return {}
    response_json = response.json()
    if 'data' in response_json:
        return response_json["data"]
    else:
        return {}


def get_twitter_bearer_token():
    """
    Fetch the bearer token from twitter and save it to TWITER_TOKEN
    environment variable
    """
    consumer_key = settings.TWITTER_CONSUMER_KEY
    consumer_secret = settings.TWITTER_CONSUMER_SECRET

    bearer_token_credentials = "%s:%s" % (consumer_key, consumer_secret)

    encoded_credentials = base64.b64encode(
        str.encode(bearer_token_credentials)).decode()
    auth_header = "Basic %s" % (encoded_credentials,)

    headers = {'Authorization': auth_header,
               'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
    try:
        response = requests.post('https://api.twitter.com/oauth2/token',
                                 headers=headers,
                                 data={'grant_type': 'client_credentials'})
        response_json = response.json()
    except requests.exceptions.ConnectionError:
        response_json = {}
    if 'access_token' in response_json:
        token = response_json['access_token']
    else:
        token = ''
    os.environ["TWITER_TOKEN"] = token
    return token


def get_twitter_feed(screen_name, count):
    """
    Fetch the most recent Tweets posted by the user indicated
    by the screen_name

    Parameters
    ----------
    screen_name : string
        The screen name of the user for whom to return Tweets for.

    count: int
        Maximum number of Tweets to fetch.
    """
    try:
        token = os.environ["TWITER_TOKEN"]
    except KeyError:
        token = get_twitter_bearer_token()
    parms = (screen_name, str(count))
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=%s&count=%s" % (parms)
    headers = {'Authorization': 'Bearer %s' % (token,)}
    try:
        response = requests.get(url, headers=headers)
    except requests.exceptions.ConnectionError:
        return {}
    response_json = response.json()
    return response_json


def update_documentations():
    """
    Check list of documentations from gh-pages branches of the dipy_web
    repository and update the database (DocumentationLink model).

    To change the url of the repository in which the documentations will be
    hosted change the DOCUMENTATION_REPO_OWNER and DOCUMENTATION_REPO_NAME
    in settings.py
    """
    url = "https://api.github.com/repos/%s/%s/contents/?ref=gh-pages" % (
        settings.DOCUMENTATION_REPO_OWNER, settings.DOCUMENTATION_REPO_NAME)
    base_url = "http://%s.github.io/%s/" % (
        settings.DOCUMENTATION_REPO_OWNER, settings.DOCUMENTATION_REPO_NAME)
    response = requests.get(url)
    response_json = response.json()
    all_versions_in_github = []

    # add new docs to database
    for content in response_json:
        if content["type"] == "dir":
            version_name = content["name"]
            all_versions_in_github.append(version_name)
            page_url = base_url + version_name
            try:
                DocumentationLink.objects.get(version=version_name)
            except ObjectDoesNotExist:
                d = DocumentationLink(version=version_name,
                                      url=page_url)
                d.save()
    all_doc_links = DocumentationLink.objects.all()

    # remove deleted docs from database
    for doc in all_doc_links:
        if doc.version not in all_versions_in_github:
            doc.delete()


def get_meta_tags_dict(title=settings.DEFAULT_TITLE,
                       description=settings.DEFAULT_DESCRIPTION,
                       keywords=settings.DEFAULT_KEYWORDS,
                       url="/", image=settings.DEFAULT_LOGO_URL,
                       object_type="website"):
    """
    Get meta data dictionary for a page

    Parameters
    ----------
    title : string
        The title of the page used in og:title, twitter:title, <title> tag etc.
    description : string
        Description used in description meta tag as well as the
        og:description and twitter:description property.
    keywords : list
        List of keywords related to the page
    url : string
        Full or partial url of the page
    image : string
        Full or partial url of an image
    object_type : string
        Used for the og:type property.
    """
    meta = Meta(title=title,
                description=description,
                keywords=keywords + settings.DEFAULT_KEYWORDS,
                url=url,
                image=image,
                object_type=object_type,
                use_og=True, use_twitter=True, use_facebook=True,
                use_googleplus=True, use_title_tag=True)
    return meta

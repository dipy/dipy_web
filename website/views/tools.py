from website.models import *
import requests
from django.core.exceptions import ObjectDoesNotExist


# Definition of functions:

def get_website_section(requested_website_position_id):
    """
    Fetch WebsiteSection with website_position_id

    Input
    -----
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

    Input
    -----
    limit : string

    Output
    ------
    returns a list of NewsPost objects
    """
    return NewsPost.objects.order_by('-post_date')[0:limit]


def has_commit_permission(access_token, repository_name):
    """
    Determine if user has commit access to the repository in nipy organisation.

    Input
    -----
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


def get_google_plus_activity(user_id):
    """
    Fetch google plus activity list of a user

    Input
    -----
    user_id : string
        The ID of the user to get activities for.
    """
    url = "https://www.googleapis.com/plus/v1/people/" + user_id + "/activities/public?maxResults=10&fields=etag%2Cid%2Citems%2Ckind%2CnextLink%2CnextPageToken%2CselfLink%2Ctitle%2Cupdated&key=AIzaSyCKyDJwNQUD7mIz_WK_Gfn-XHwFg3ZOr5g"
    r = requests.get(url)
    json_response = r.json()
    if 'error' not in json_response:
        return json_response['items']
    else:
        return {}

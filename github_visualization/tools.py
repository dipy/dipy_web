import requests


def fetch_all_contributors(user, repo):
    try:
        response = requests.get(
            "https://api.github.com/repos/%s/%s/contributors" %
            (user, repo))
        if response.status_code != 200:
            return None
        response = response.text
        return response
    except:
        return None

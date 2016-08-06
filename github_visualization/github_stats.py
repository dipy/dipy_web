import requests


class GithubStatFetcher:
    """A GitHub statistics fetcher for github repositories
    """

    def __init__(self, user_name, repositoty_name):
        ''' Initialize GithubStatFetcher Object

        Parameters
        -------------
        user_name : str
           Name of the user or organization of the repository owner
        repositoty_name : str
           Name of repository
        '''
        self.user_name = user_name
        self.repositoty_name = repositoty_name

        self.baseurl = "https://api.github.com/repos/%s/%s" % (
            self.user_name, self.repositoty_name)

    def total_contributions(self, weeks):
        ''' Helper function to calculate total additions
        and total deletions from a list of weeks of contributions
        of a contributor

        Parameters
        -------------
        weeks : list
           List of weeks of contributions. Example:
           [
            {'w': 1254009600, 'a': 5, 'c': 2, 'd': 9},
           ]

        '''
        total_additions = 0
        total_deletions = 0
        for week in weeks:
            total_additions += week['a']
            total_deletions += week['d']
        return total_additions, total_deletions

    def fetch_basic_stats(self):
        ''' Fetch the basic stats

        Returns
        -------
        basic_stats : dict
            A dictionary containting basic statistics. For Example:
            { 'response_code': 200,
              'repo_name': 'dipy',
              'repo_description': 'Diffusion MR Imaging in Python',
              'html_url': 'https://github.com/nipy/dipy',
              'subscribers': 41,
              'forks': 142,
              'watchers': 94,
              'open_issues': 154,
              'is_private': False,
              'stars': 94
            }

        '''
        basic_stats = {}
        url = self.baseurl
        try:
            response = requests.get(url)
            basic_stats["response_code"] = response.status_code

            # check response code
            if response.status_code != 200:
                return basic_stats

            # parse response
            r_json = response.json()
            basic_stats["repo_name"] = r_json["name"]
            basic_stats["repo_description"] = r_json["description"]
            basic_stats["is_private"] = r_json["private"]
            basic_stats["html_url"] = r_json["html_url"]
            basic_stats["stars"] = r_json["stargazers_count"]
            basic_stats["watchers"] = r_json["watchers_count"]
            basic_stats["forks"] = r_json["forks_count"]
            basic_stats["open_issues"] = r_json["open_issues_count"]
            basic_stats["subscribers"] = r_json["subscribers_count"]

            return basic_stats
        except:
            raise

    def fetch_contributor_stats(self):
        ''' Fetch stats of contributors

        Returns
        -------
        contributor_stats : dict
            A dictionary containting contributor statistics. For Example:
            { 'response_code': 200,
              'contributors': [ {
                                "user_name": "Garyfallidis"
                                "avatar_url": "https://avatars.githubusercontent.com/u/134276?v=3",
                                "html_url": "https://github.com/Garyfallidis",
                                "total_commits": 1389,
                                "total_additions": 116712,
                                "total_deletions": 70340,
                                "weekly_commits": [
                                          {
                                            "w": "1367712000",
                                            "a": 6898,
                                            "d": 77,
                                            "c": 10
                                          },
                                        ]
                                },
                            ]
            }

        '''
        contributor_stats = {}
        contributor_stats["contributors"] = []

        url = self.baseurl + "/stats/contributors"
        try:
            response = requests.get(url)
            contributor_stats["response_code"] = response.status_code

            # check response code
            if response.status_code != 200:
                return contributor_stats

            # parse response
            r_json = response.json()

            for contributor in r_json:
                contributor_dict = {}
                contributor_dict["user_name"] = contributor["author"]["login"]
                contributor_dict["avatar_url"] = contributor[
                    "author"]["avatar_url"]

                contributor_dict["html_url"] = contributor[
                    "author"]["html_url"]

                contributor_dict["total_commits"] = contributor["total"]

                total_additions, total_deletions = self.total_contributions(
                    contributor["weeks"])

                contributor_dict["total_additions"] = total_additions
                contributor_dict["total_deletions"] = total_deletions
                contributor_dict["weekly_commits"] = contributor["weeks"]
                contributor_stats["contributors"].append(contributor_dict)

            return contributor_stats
        except:
            raise

    def fetch_weekly_contributions(self):
        ''' Fetch the number of additions and deletions per week
        and the number of commits per week upto one year.

        Returns
        -------
        weekly_contributions : dict
            Example:
            {
            "response_code": 200,
            "changes":    [
                            [
                                1469923200,
                                2,
                                -3
                            ],
                        ]
            "commits":    [
                                1469923200,
                                50
                        ]
            }
        '''
        weekly_contributions = {}
        weekly_contributions["changes"] = []
        weekly_contributions["commits"] = []

        url1 = self.baseurl + "/stats/code_frequency"
        url2 = self.baseurl + "/stats/participation"

        try:
            response1 = requests.get(url1)
            response2 = requests.get(url2)

            if response1.status_code != 200:
                weekly_contributions["response_code"] = response1.status_code
            elif response2.status_code != 200:
                weekly_contributions["response_code"] = response2.status_code
            else:
                weekly_contributions["response_code"] = 200

            # check response code
            if weekly_contributions["response_code"] != 200:
                return weekly_contributions

            # parse response
            r1_json = response1.json()
            r2_json = response2.json()
            weekly_contributions["changes"] = r1_json

            offset = len(weekly_contributions["changes"]) - len(r2_json["all"])
            for i, commit in enumerate(r2_json["all"]):
                commit_info = []
                commit_info.append(weekly_contributions["changes"][offset + i])
                commit_info.append(commit)
                weekly_contributions["commits"].append(commit_info)
            return weekly_contributions
        except:
            raise

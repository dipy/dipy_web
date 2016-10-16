from time import sleep
import requests

from django.conf import settings


class GithubStatFetcher:
    """A GitHub statistics fetcher for Github repositories
    """

    def __init__(self, user_name, repository_name):
        ''' Initialize GithubStatFetcher Object

        Parameters
        -------------
        user_name : str
           Name of the user or organization of the repository owner
        repository_name : str
           Name of repository
        '''
        self.user_name = user_name
        self.repository_name = repository_name

        self.baseurl = "https://api.github.com/repos/%s/%s" % (
            self.user_name, self.repository_name)

    def construct_url(self, path):
        '''Construct url from baseurl

        Parameters
        ----------
        path : str
            Path of API endpoint after /repos/username/reponame
            Eg: /stats/contributors

        Returns
        -------
        url : full canonical url of the API endpoint
        '''
        credentials = ""
        if(len(settings.GITHUB_VIZ_CLIENT_ID) and
           len(settings.GITHUB_VIZ_CLIENT_SECRET)):
            credentials = "?client_id=%s&client_secret=%s" % (
                settings.GITHUB_VIZ_CLIENT_ID,
                settings.GITHUB_VIZ_CLIENT_SECRET)

        url = self.baseurl + path + credentials
        return url

    def __fetch_url(self, url):
        response = requests.get(url)
        if response.status_code == "202":
            tries = 3
            while tries >= 0:
                tries -= 1
                response = requests.get(url)
                if response.status_code == "200":
                    break
                sleep(0.1)
        return response

    def __get_total_contributions(self, weeks):
        ''' Helper function to calculate total additions
        and total deletions from a list returned from GitHub API

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

    def __get_cumulative_contributors(self, contributors_list):
        ''' Helper function to calculate total contributors as
        new contributors join with time

        Parameters
        -------------
        contributors_list : list
           List of contributors with weeks of contributions. Example:
           [
               {
                    'weeks': [
                            {'w': 1254009600, 'a': 5, 'c': 2, 'd': 9},
                        ],
                    .....
                },
            ]

        '''
        contributors_join_date = {}

        for contributor in contributors_list:
            for week in contributor["weeks"]:
                if(week["c"] > 0):
                    join_date = week['w']
            if join_date not in contributors_join_date:
                contributors_join_date[join_date] = 0
            contributors_join_date[join_date] += 1

        cumulative_join_date = {}
        cumulative = 0
        for time in sorted(contributors_join_date):
            cumulative += contributors_join_date[time]
            cumulative_join_date[time] = cumulative

        cumulative_list = list(cumulative_join_date.items())
        cumulative_list.sort()

        return cumulative_list

    def fetch_basic_stats(self):
        ''' Fetch the basic stats

        Returns
        -------
        basic_stats : dict
            A dictionary containing basic statistics. For example:
            { 'response_code': 200,
              'repo_name': 'dipy',
              'repo_description': 'Diffusion MR Imaging in Python',
              'html_url': 'https://github.com/nipy/dipy',
              'subscribers': 41,
              'forks': 142,
              'forks_url': 'https://github.com/nipy/dipy/network'
              'watchers': 94,
              'open_issues': 154,
              'is_private': False,
              'stars': 94,
              'stars_url': 'https://github.com/nipy/dipy/stargazers'
            }

        '''
        basic_stats = {}
        url = self.construct_url("")
        try:
            response = self.__fetch_url(url)
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
            basic_stats["stars_url"] = r_json["html_url"] + "/stargazers"
            basic_stats["watchers"] = r_json["watchers_count"]
            basic_stats["forks"] = r_json["forks_count"]
            basic_stats["forks_url"] = r_json["html_url"] + "/network"
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
            A dictionary containing contributor statistics. For example:
            { 'response_code': 200,
              'total_contributors': 50,
              'total_commits': 6031,
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
              'cumulative_contributors': [
                                (
                                    1367712000, // timestamp
                                    20 // total number of contributions
                                       // upto this time
                                ),
                            ]
            }

        '''
        contributor_stats = {}
        contributor_stats["contributors"] = []

        url = self.construct_url("/stats/contributors")
        try:
            response = self.__fetch_url(url)
            contributor_stats["response_code"] = response.status_code

            # check response code
            if response.status_code != 200:
                return contributor_stats

            # parse response
            r_json = response.json()
            contributor_stats["total_contributors"] = len(r_json)

            grand_total_commits = 0
            for contributor in r_json:
                contributor_dict = {}

                # check if "author" is null
                if not contributor["author"]:
                    continue
                contributor_dict["user_name"] = contributor["author"]["login"]
                contributor_dict["avatar_url"] = contributor[
                    "author"]["avatar_url"]

                contributor_dict["html_url"] = contributor[
                    "author"]["html_url"]

                contributor_dict["total_commits"] = contributor["total"]
                grand_total_commits += contributor["total"]

                total_additions, total_deletions = self.__get_total_contributions(
                    contributor["weeks"])

                contributor_dict["total_additions"] = total_additions
                contributor_dict["total_deletions"] = total_deletions
                contributor_dict["weekly_commits"] = contributor["weeks"]
                contributor_stats["contributors"].insert(0, contributor_dict)

            contributor_stats["total_commits"] = grand_total_commits

            cumulative_contributors = self.__get_cumulative_contributors(
                r_json)
            contributor_stats[
                "cumulative_contributors"] = cumulative_contributors

            return contributor_stats
        except:
            raise

    def fetch_weekly_contributions(self):
        ''' Fetch the number of additions and deletions and total lines of
        code per week from beginning; and the number of commits per week upto
        one year.

        Returns
        -------
        weekly_contributions : dict
            Example:
            {
            "response_code": 200,
            "changes":    [
                            [
                                1469923200, // timestamp
                                2, // additions
                                -3, // deletions
                                506 // total lines of code
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

        url1 = self.construct_url("/stats/code_frequency")
        url2 = self.construct_url("/stats/participation")

        try:
            response1 = self.__fetch_url(url1)
            response2 = self.__fetch_url(url2)

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

            weekly_contributions["changes"] = []
            lines = 0
            for changes in r1_json:
                change_list = []
                change_list.append(changes[0])
                change_list.append(changes[1])
                change_list.append(changes[2])
                lines = lines + changes[1] + changes[2]
                change_list.append(lines)
                weekly_contributions["changes"].append(change_list)

            offset = len(weekly_contributions["changes"]) - len(r2_json["all"])
            for i, commit in enumerate(r2_json["all"]):
                commit_info = []
                commit_info.append(weekly_contributions["changes"][offset + i])
                commit_info.append(commit)
                weekly_contributions["commits"].append(commit_info)
            return weekly_contributions
        except:
            raise

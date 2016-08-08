from django import template
from github_visualization import github_stats
register = template.Library()


# display partial template containting github statistics for a repository
@register.inclusion_tag('github_visualization/github_stats_partial.html')
def github_stats_block(user_name, repository_name):
    context = {}
    github_stat_fetcher = github_stats.GithubStatFetcher(
        user_name, repository_name)
    context["contributors"] = github_stat_fetcher.fetch_contributor_stats()
    context["basic_stats"] = github_stat_fetcher.fetch_basic_stats()
    return context

from datetime import datetime
import tweepy
from django.conf import settings
from django.utils import timezone as tz

from workshop.models import Video


def get_workshop_tweet(tags, max_tweet=15):
    if not tags:
        return []

    auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY,
                               settings.TWITTER_CONSUMER_SECRET)
    # auth.set_access_token(keys['access_token'], keys['access_token_secret'])
    api = tweepy.API(auth)

    # Define Keywords
    keywords = ' OR '.join(tags) + '  -filter:retweets'
    return [tweet for tweet in tweepy.Cursor(api.search_tweets, q=(keywords),
                                             tweet_mode="extended").items(max_tweet)]

    # print(tags)
    # tweets = []
    # for tweet in tweepy.Cursor(api.search_tweets, q=(keywords), lang='en', tweet_mode="extended").items(max_tweet):
    #     # print(tweet)
    #     tweets.append(tweet)

    # import ipdb; ipdb.set_trace()
    # print(len(tweets))
    # return tweets


def str2date(date_str):
    """The date should be in the following form: 12-03-2021."""
    date = datetime.strptime(date_str, '%d-%m-%Y')
    return date.strftime("%A, %B %d")


def generate_calendar(workshop):
    events = workshop.events.all()
    calendar = {}
    for evt in events:
        date = evt.start_date.replace(minute=1, hour=1, second=1,
                                      tzinfo=tz.get_current_timezone())
        time = evt.start_date.replace(tzinfo=tz.get_current_timezone()).strftime("%-H:%M %p")
        videos = Video.objects.filter(workshops=workshop, lesson=evt.session)
        author = []
        if videos:
            author = set([(sp.fullname, sp.avatar_url) for vid in videos
                          for sp in vid.speakers.all()])
        elif hasattr(evt.session, 'qa'):
            panel = evt.session.qa.panel.all()
            author = set([(sp.fullname, sp.avatar_url) for sp in panel])

        # print(date, evt.session.name, date in calendar)
        if date in calendar:
            calendar[date].append((evt.session.name, time, author))
        else:
            calendar[date] = [(evt.session.name, time, author)]

    # cal = sorted(calendar.items())
    # cal = [(str2date(cal[0]), sorted(cal[1], key=lambda val: val[1]))
    #        for cal in sorted(calendar.items())]
    cal = [(cal[0], sorted(cal[1], key=lambda val: val[1]))
           for cal in sorted(calendar.items())]
    # print(cal)s
    return cal
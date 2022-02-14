from datetime import datetime
import tweepy
from django.conf import settings

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
        #.strftime("%d-%m-%Y")
        date = evt.start_date.replace(minute=00, hour=00, second=00)
        time = evt.start_date.strftime("%H:%M:%S")
        videos = Video.objects.filter(workshops=workshop, lesson=evt.session)
        author = set([sp.fullname for vid in videos
                      for sp in vid.speakers.all()])

        author = "by " + ", ".join(author) if author else ""
        print(date, evt.session.name, date in calendar)
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
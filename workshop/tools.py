import tweepy
from django.conf import settings


def get_workshop_tweet(tags, max_tweet=15):
    if not tags:
        return []

    auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY,
                               settings.TWITTER_CONSUMER_SECRET)
    # auth.set_access_token(keys['access_token'], keys['access_token_secret'])
    api = tweepy.API(auth)

    # Define Keywords
    keywords = ' OR '.join(tags) + '  -filter:retweets'
    return [tweet for tweet in tweepy.Cursor(api.search, q=(keywords),
                                             tweet_mode="extended").items(max_tweet)]

    # print(tags)
    # tweets = []
    # for tweet in tweepy.Cursor(api.search, q=(keywords), lang='en', tweet_mode="extended").items(max_tweet):
    #     # print(tweet)
    #     tweets.append(tweet)

    # import ipdb; ipdb.set_trace()
    # print(len(tweets))
    # return tweets


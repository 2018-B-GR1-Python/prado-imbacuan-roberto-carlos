import twitter
from twitter.models import Status

ck = 'Se0qknGFej0Q9IKP1yPLE6QLp'
cs = 'kg6SO6F4BYfBIPLWEwgH7wo5DJ34kQ67EjmUF2aIu3CkgK89Jj'
at = '992482632213712896-RLGNU01sJ5PFiPzzXOI6M2qVaRx3WXf'
ats = 'l5vPBD53GxZRREjqLWRfWaIAkRwgAM0lu1lqwXWLwH56j'

api = twitter.Api(consumer_key=ck,
                  consumer_secret=cs,
                  access_token_key=at,
                  access_token_secret=ats)

# print(api.VerifyCredentials())

tweets = api.GetUserTimeline(screen_name="steam_games", count=20)

for tweet in tweets:
    print('\n Tweet:')
    print(f"ID: {tweet.id}")
    print(f"Retweet count: {tweet.retweet_count}")
    print(f"TEXT: {tweet.text}")
    print(f"LIKES: {tweet.favorite_count}")

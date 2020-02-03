import twitter
import json

TEST_HANDLE = "twitter_handle"
KEYWORDS = ["commission", "comm", "slot", "badge", "request", "ych"]

def initialize_api():
    api = None
    with open('keys.json') as key_file:
        key_data = json.load(key_file)
        twitter_keys = key_data["twitter"]
        api = twitter.Api(consumer_key=twitter_keys['consumer_key'],
                  consumer_secret=twitter_keys['consumer_secret'],
                  access_token_key=twitter_keys['access_token'],
                  access_token_secret=twitter_keys['access_token_secret'])
    return api

def get_latest_tweets(api=None, screen_name=None, num_tweets=100):
    tweets = api.GetUserTimeline(screen_name=screen_name, count=num_tweets)
    return tweets

def find_commission_info_in_latest_tweets(api=None, screen_name=None, num_tweets=100):
    tweets = get_latest_tweets(api=api, screen_name=screen_name, num_tweets=num_tweets)
    for tweet in tweets:
        if tweet.text.startswith("@") or tweet.text.startswith("RT @"):
            continue
        if "open" in tweet.text.lower() and [k for k in KEYWORDS if k in tweet.text.lower()]:
            print("[[OPEN " + tweet.created_at + "]]: \n" + tweet.text.replace("\n", " "))
        # if "full" in tweet.text.lower() and [k for k in KEYWORDS if k in tweet.text.lower()]:
        #     print("[CLOSED]: " + tweet.text)

def get_user_data(api=None, screen_name=None):
    user = api.GetUser(screen_name=screen_name)
    description = user.description
    name = user.name
    print(screen_name, name, description)

if __name__ == "__main__":
    api = initialize_api()
    get_user_data(api=api, screen_name=TEST_HANDLE)
    find_commission_info_in_latest_tweets(api=api, screen_name=TEST_HANDLE)
    
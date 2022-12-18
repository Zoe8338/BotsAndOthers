import Mastodon
import tweepy

# Mastodon API keys
mastodon_client_id = "YOUR_CLIENT_ID"
mastodon_client_secret = "YOUR_CLIENT_SECRET"
mastodon_access_token = "YOUR_ACCESS_TOKEN"

# Twitter API keys
twitter_consumer_key = "YOUR_CONSUMER_KEY"
twitter_consumer_secret = "YOUR_CONSUMER_SECRET"
twitter_access_token = "YOUR_ACCESS_TOKEN"
twitter_access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Create a Mastodon client object
mastodon = Mastodon.Mastodon(
    client_id=mastodon_client_id,
    client_secret=mastodon_client_secret,
    access_token=mastodon_access_token,
    api_base_url="https://YOUR_INSTANCE.com"
)

# Create a Twitter client object
auth = tweepy.OAuth1UserHandler(
    twitter_consumer_key,
    twitter_consumer_secret,
    twitter_access_token,
    twitter_access_token_secret
)
twitter = tweepy.API(auth)

# Retrieve the tweets of a specific user
tweets = twitter.user_timeline(screen_name="USERNAME")

# For each tweet, create a new toot on Mastodon with the same content
for tweet in tweets:
    mastodon.toot(tweet.text)

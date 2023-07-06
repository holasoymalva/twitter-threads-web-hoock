import tweepy
import requests

# Twitter credentials
TWITTER_API_KEY = "YOUR_TWITTER_API_KEY"
TWITTER_API_SECRET = "YOUR_TWITTER_API_SECRET"
TWITTER_ACCESS_TOKEN = "YOUR_TWITTER_ACCESS_TOKEN"
TWITTER_ACCESS_TOKEN_SECRET = "YOUR_TWITTER_ACCESS_TOKEN_SECRET"

# Facebook access token
FACEBOOK_ACCESS_TOKEN = "YOUR_FACEBOOK_ACCESS_TOKEN"

# Create a Tweepy API object for Twitter
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
twitter_api = tweepy.API(auth)

# Function to post on Twitter
def post_on_twitter(message):
    try:
        twitter_api.update_status(message)
        print("Posted on Twitter successfully!")
    except tweepy.TweepError as e:
        print("Error posting on Twitter:", str(e))

# Function to post on Facebook
def post_on_facebook(message):
    try:
        url = f"https://graph.facebook.com/me/feed?access_token={FACEBOOK_ACCESS_TOKEN}"
        data = {"message": message}
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("Posted on Facebook successfully!")
        else:
            print("Error posting on Facebook:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error posting on Facebook:", str(e))

# Main program
if __name__ == "__main__":
    message = "Hello world! This is a simultaneous post on Twitter and Facebook."
    post_on_twitter(message)
    post_on_facebook(message)

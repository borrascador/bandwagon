import tweepy
import time
from write import write_message
from secret import *

line = write_message()
while len(line) > 140:
    line = write_message()

auth = tweepy.OAuthHandler(KEY, KEY_SECRET)
auth.set_access_token(TOKEN, TOKEN_SECRET)
api = tweepy.API(auth)
api.update_status(line)

print("@{} tweeted @ {}:\n{}".format(api.me().screen_name, time.ctime(),line))
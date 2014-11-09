import tweepy
import json

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'w7Q5Ln3GwhPbNDnbCd2LGvkSQ'
consumer_secret = 'Z4eiQrctjJr2nzdtc9S8D8uWDmUUY7ftEQ5O5d2cg93TqRUYyk'
access_token = '1054546747-AKTRVj28mKd7EUDVEpkgVVqkeQK8NjfjqzktvHw'
access_token_secret = 'waktXyQ8tgXwiQgbilAy6mwORo1qeoQSwBIo5EYCCUVEN'

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        print ''
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    print "Showing all new tweets for #programming:"

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    stream = tweepy.Stream(auth, l)
    san_fransisco = [-122.75,36.8,-121.75,37.8]
    #stream.filter(track=['programming'])
    stream.filter(locations=san_fransisco)

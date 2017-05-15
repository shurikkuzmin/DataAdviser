import oauth2 as oauth
import json
import urllib2

# Create your consumer with the proper key/secret.
ckey = "q6yVAbqSByGhmajnf79terBi7"
csecret = "9QcXdybsisDuRRrDARgnATWqY4qQR9d8dV5f422y6lM0OekwTz"
akey = "119277384-9TxxQPXdL9ZqY14644wNz8gVtdw8ljVDAOL6nKC2"
asecret = "VbYVfGdmZyTQeykd441Q3PjciQQHV3i8lbiXV6hAmX8Xj"

token = oauth.Token(key=akey, secret=asecret)
consumer = oauth.Consumer(key = ckey, secret = csecret)
client = oauth.Client(consumer, token)

timeline_endpoint = "https://api.twitter.com/1.1/statuses/home_timeline.json"
search_endpoint = "https://api.twitter.com/1.1/search/tweets.json"
#search_parameters = r'''?q=problem near:"Chicago, IL" within:15mi&count=10'''
search_parameters='''?q=problem%20near%3A"Chicago%2C%20IL"%20within%3A15mi'''
search_url = search_endpoint + search_parameters
print search_url
# The OAuth Client request works just like httplib2 for the most part.
response, data = client.request(timeline_endpoint)
response, data = client.request(search_url)

###req = oauth.Request(method="GET", url=search_endpoint, parameters=params)
###signature_method = oauth.SignatureMethod_HMAC_SHA1()
###req.sign_request(signature_method, consumer, token)
###headers = req.to_header()
###url = req.to_url()
###response = urllib2.Request(url)
###data = json.load(urllib2.urlopen(response))

tweets = json.loads(data)
print(json.dumps(tweets, indent = 4))
#print tweets['statuses']
for tweet in tweets['statuses']:
    print tweet['text']

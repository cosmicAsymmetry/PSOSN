import json
from pymongo import MongoClient
from twython import Twython


client = MongoClient('localhost', 27017) #connect to the mongo instance running on the system

db = client['psosm_data_collection']	#connect to the required data base
collection = db['twitterdb']		#connect to the required collection


api_key = {
	'api_key': 'zhbCYEbsZWdijh92qQLOiRE6D',
	'api_secret': 'PnIwL7r5S2cOvpZ03HFRaInqkSBSE6KMRrdEdplOcLDNk0sVKV',
	'access_token': '600824988-UXRwqLHsTHNnlbV8jGOR7wqlI5OB0ZyTGo1xVEBW',
	'access_token_secret': 'LClRJjARMUvK1Q65S30sjcDaHDu7BP03C3YYLuhZh1Ys0'
}

twitter= Twython(api_key['api_key'],
				api_key['api_secret'],
				api_key['access_token'],
				api_key['access_token_secret']
				)


tweetCount = 0
search_phrase = 'modi'

# ID of the most recent tweet
max_id = -1

new_statuses = twitter.search(q=search_phrase, count="100", include_entities= True)  #include entities - urls, hashtags and user mentions

for item in new_statuses:
	print item

#exit()

for tweet in new_statuses['statuses']:
	tweetCount += 1
	post = tweet

	with open('modi_twitter/tweet'+str(tweetCount)+'.json', 'w') as outfile:
			json.dump(post,outfile)


print "Total tweets: ", tweetCount

import json
# import sys
import time
# import os
from pymongo import MongoClient
from twython import Twython

api_key = {
	'api_key': 'Yv7R4cwPF0F8TutGZznRJ1yhr',
	'api_secret': '5ZLzXb9IY0aKhzIGvCmIjqN3TX37VhpGSPSUdTiVwaQFPGtoop',
	'access_token': '1024544526-VzhUh2VDuODF1xNyys0P202aAcVyMoHzVBlP2FP',
	'access_token_secret': 'S2EvvqO3GAzeCB0d3vcEJaCRBomkkJZcky9AdJqIvzew4'
}

twitter= Twython(api_key['api_key'],
				api_key['api_secret'],
				api_key['access_token'],
				api_key['access_token_secret']
				)

# Insert data in a MongoDB database
 def insert_data(post):
 	client = MongoClient()
 	db = client.summerschool

 	post['_id'] = post['id']
 	try:
 		db.tweets_collected.insert(post)
 	except Exception as e:
 		print e

def search_tweets(search_phrase, maxTweets):
	# ID of the earliest tweet
	id_of_earliest_tweet = -1

	# ID of the earliest tweet in the list
	id_of_earliest_tweet = None

	count = 0
	tweetCount = 0

	while tweetCount < maxTweets:
		list_of_tweets = []

		if id_of_earliest_tweet <= 0:
			new_statuses = twitter.search(q=search_phrase, count="100", include_entities= True)

		else:
			new_statuses = twitter.search(q=search_phrase, count="100", include_entities = True, max_id=id_of_earliest_tweet - 1)

		tweetCount += len(new_statuses['statuses'])

		print tweetCount

		for tweet in new_statuses['statuses']:
			count += 1
			post = tweet
			list_of_tweets.append(post['id'])

			# Saving data in a MongoDB collection
			insert_data(post)

			# Saving data in files

#			with open('/home/kushagra/modi_twitter/tweet'+str(count)+'.json', 'w') as outfile:
#					json.dump(post,outfile)

		id_of_earliest_tweet = sorted(list_of_tweets)[0]


		# print tc

	print "Total tweets: ", tweetCount

# First parameter: The keyword we wish to search for
# Second parameter: Total tweets you wish to collect
search_tweets('modi',10000)

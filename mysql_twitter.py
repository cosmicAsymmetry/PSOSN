import json
import sys, time
import os
from twython import Twython

import MySQLdb

db = MySQLdb.connect(host="127.0.0.1",    # your host, usually localhost
                     user="root",         # your username
                     passwd="sidhantB27",  		  # your password
                     port = 3306,
                     db="psosm_data_collection")          # name of the data base

# you must create a Cursor object. It will let you execute all the queries you need

cursor = db.cursor()

# query = "Create table twitterdb ( tweet_text varchar(20) NOT NULL,id INT NOT NULL, followers INT NOT NULL, followings INT NOT NULL, username varchar(20))"


# # query = "Create table twitterdb ( tweet_text varchar(150), id NOT NULL , followers INT NOT NULL, followings INT NOT NULL, username varchar(20) )"
# cursor.execute(query)
# db.commit()
# cursor.close()



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

maxTweets = 10000
tweetCount = 0

# ID of the most recent tweet
max_id = -1

# ID of the earliest tweet in the list
sinceId = None

count = 0

while tweetCount < maxTweets:
	list_of_tweets = []

	if (max_id <= 0):
		new_statuses = twitter.search(q='modi', count="100", include_entities= True)
		print(1)

	else:
		new_statuses = twitter.search(q='modi', count="100", include_entities = True, max_id=max_id - 1)
		print(3)

	tweetCount += len(new_statuses['statuses'])

	print tweetCount

	for tweet in new_statuses['statuses']:
		count += 1
		post = tweet
		list_of_tweets.append(post['id'])

		post['_id'] = post['id']

		Text = post['text'].encode('utf8')
		followers = post['user']['followers_count']
		followings = post['user']['friends_count']

		username = post['user']['screen_name']


		query = "INSERT into twitterdb (tweet_text,id, followers, followings, username) values (%s,%s,%s,%s,%s)"
		print "Done: ", count
		cursor.execute(query,( str(Text),post['id'], followers, followings, username))
		db.commit()


		# with open('/home/kushagra/narendramodi_fbpage/tweet'+str(count)+'.json', 'w') as outfile:
		# 		json.dump(post,outfile)

	max_id = sorted(list_of_tweets)[0]

	# print tc

print "Total tweets: ", tweetCount

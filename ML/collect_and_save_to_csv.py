import json
from twython import Twython
import csv


with open('training_dataset.csv','a') as f:  #change filename accordingly
	writer = csv.writer(f)
	writer.writerow(['tweetID', 'followers', 'listed', 'followings', 'verified', 'Total_favourite_count', 'tweet_favorite_count' ])



with open('test_dataset.csv','a') as f:  #change filename accordingly
	writer = csv.writer(f)
	writer.writerow(['tweetID', 'followers', 'listed', 'followings', 'verified', 'Total_favourite_count', 'tweet_favorite_count'])



api_key = {
	'api_key': 'kP9p8OH8OtwQuHnajRfoBsxVJ',
	'api_secret': 'EcTKwFN7pmU0Y6XT0g9uoRgNOqzOomrtUUFAxg2b3vpj0lI5sO',
	'access_token': '881461410588315648-zqI8cP4B6j6a2u6TnltaeuBfCNxOsQc',
	'access_token_secret': 'EzJ29x97aUbhl6RB0ektiHevZVYcCt3ZO2lJ6U5bx2lmn'
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
		fav_count = post['user']['favourites_count']  #total favourites
		listed = post['user']['listed_count']
		favorite_count = post['favorite_count']  #favourites received

		# print post['user']['verified']

		if post['user']['verified'] == False:
			ver = 0
		else:
			ver = 1


		username = post['user']['screen_name']



		if count >= 5000:

			with open('test_dataset.csv','a') as f:  #change filename accordingly
				writer = csv.writer(f)
				writer.writerow([post['id'], int(followers), listed, followings, ver, fav_count, favorite_count ])

		else:

			with open('training_dataset.csv','a') as f:  #change filename accordingly
				writer = csv.writer(f)
				writer.writerow([post['id'], int(followers), listed, followings, ver, fav_count, favorite_count ])

	max_id = sorted(list_of_tweets)[0]

	# print tc

print "Total tweets: ", tweetCount


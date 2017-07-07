import facebook
import simplejson
import urllib2
import json
from pymongo import MongoClient

api_key = {
			'api_key': '1535920509797363',
			'api_secret': 'beb45fdfe862cb0eff46b53d5cf97a35',
			'access_token':	'EAAV06VxjwZCMBAKHU8hsOaC35Ecr2HNGCSh36u6fABrPzvlSgQ6nfxWw9xsE5i4olNpKa9HZC2VVnZCpgUfSoqKgNZAdxazvvUeLgUDg2ZCMN0Bc3ojF3SDafmki2n6A1cgHxyPNXQXFMXstt4mQ5P6vmRmIBOvOA13n2cr11J6ZCKFQUM3XjX8kOjOFBEWQ8ZD'
		}

# # Insert data in a MongoDB database
# def insert_data(post):
# 	client = MongoClient()
# 	db = client.summerschool

# 	post['_id'] = post['id']
# 	try:
# 		db.fb_posts.insert(post)
# 	except Exception as e:
# 		print e

# Get all posts for a public page
def search_user(api_key, search_phrase, older_data_url, newer_data_url):

	# Initializing the Facebook Graph API object
	graph = facebook.GraphAPI(access_token= api_key['access_token'])

	# The first iteration for collecting most recent posts
	if newer_data_url == '0':
		post = graph.get_object(search_phrase+'/feed',fields='caption,description,from,message,created_time,full_picture,id,link,status_type,story,story_tags,type,updated_time,with_tags,is_popular,actions')

	# Executed if there is any newer data on tha page.
	else:
		post_pre = urllib2.urlopen(newer_data_url,timeout=30)
		post = simplejson.load(post_pre)
		post_pre.close()


	# Executed if there is any older data
	if older_data_url != '0':
		post_pre = urllib2.urlopen(older_data_url,timeout=30)
		post = simplejson.load(post_pre)
		post_pre.close()

	return post

def start_data_collection(search_phrase, number_of_posts):
	older_data_url = '0'
	newer_data_url = '0'

	count=0
	while count < number_of_posts:
		# Collecting the first 25 posts from the page.
		post = search_user(api_key, search_phrase, older_data_url, newer_data_url)


		if (len(post['data']) > 0):
			# This condition checks for any newer data that has come.
			if newer_data_url == '0':
				if 'paging' in post and 'previous' in post['paging']:
					print 'Previous key is there.'
					newer_data_url = post['paging']['previous']

			# This condition checks for older data that was posted.
			if 'paging' in post and 'next' in post['paging']:
				print 'Next key is there.'
				older_data_url = post['paging']['next']


		for status in post['data']:
			count+=1

			# # Saving data in a MongoDB collection
			# insert_data(status)

			# Saving data in files

			with open('/home/sidhant/Documents/PSOSM/narendramodi/post'+str(count)+'.json', 'w') as outfile:
				json.dump(status,outfile)


# First parameter: Facebook page handle
# Second parameter: Total posts you wish to collect
start_data_collection('narendramodi', 2000)

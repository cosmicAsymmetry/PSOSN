from sklearn.ensemble import RandomForestClassifier
import pandas as pd 
import csv

df = pd.read_csv('annotations_maliciousposts_data.csv')


#Splitting data into training and test set
from sklearn.model_selection import train_test_split
training_partition, test_partition = train_test_split(df, test_size = 0.2)


'''
Building the training set
'''

train = training_partition[['L_http','L_https','L_numHyphens','L_numParams','L_numSubDomains','L_paramLen','L_pathLen','M_hasFBUrl','M_hasFBappURL',
'M_hasFBeventURL','M_hasLink','M_hasMessage','M_hasPicture','M_hasStory','M_length_of_link','M_postType',
'T_!','T_!!','T_:(','T_:)','T_?','T_??','T_avgSentLen','T_avgWordLen','T_engDictWords','T_hashtagsPerWord',
'T_numChars','T_numHashtags','T_numSentences','T_numUrls','T_numWords','T_textRepFactor','T_upperCaseChars',
'T_urlsPerWord','U_category','U_gender','U_hasUsername','U_isPage','U_lenName','U_lenUsername','U_locale',
 'U_pageLikes','U_wordsInName', 'M_app']]


#Feature engineering
def convert_to_bool(x):
	return 1 if x == 'Spam' else 0

labels = training_partition['Z_CLASS'].apply(convert_to_bool)



app_to_num_lookup = dict(mobile=0, web=1, thirdparty=2, contentsharing=3, other=4)

def app_to_num(x):
	return app_to_num_lookup[x]

train['M_app'] = train['M_app'].apply(app_to_num)


'''
Building the training set
'''


test_set = test_partition[['L_http','L_https','L_numHyphens','L_numParams','L_numSubDomains','L_paramLen','L_pathLen','M_hasFBUrl','M_hasFBappURL',
'M_hasFBeventURL','M_hasLink','M_hasMessage','M_hasPicture','M_hasStory','M_length_of_link','M_postType',
'T_!','T_!!','T_:(','T_:)','T_?','T_??','T_avgSentLen','T_avgWordLen','T_engDictWords','T_hashtagsPerWord',
'T_numChars','T_numHashtags','T_numSentences','T_numUrls','T_numWords','T_textRepFactor','T_upperCaseChars',
'T_urlsPerWord','U_category','U_gender','U_hasUsername','U_isPage','U_lenName','U_lenUsername','U_locale',
 'U_pageLikes','U_wordsInName', 'M_app']]

#Feature engineering
def convert_to_bool(x):
	return 1 if x == 'Spam' else 0

true_labels = test_partition['Z_CLASS'].apply(convert_to_bool)



app_to_num_lookup = dict(mobile=0, web=1, thirdparty=2, contentsharing=3, other=4)

def app_to_num(x):
	return app_to_num_lookup[x]

test_set['M_app'] = test_set['M_app'].apply(app_to_num)


#Shape of the training and test set
print "Length of training data: ",train.shape
print "Length of training labels: ",labels.shape
print "Length of the test partition: ",test_partition.shape
print "Length of the test set: ",test_set.shape

# exit()

#Appying the classifier from sklearn
from sklearn.ensemble import  RandomForestClassifier

alg = RandomForestClassifier()   #Load the estimator

alg.fit(train, labels)			#Fit the estimator



result = alg.predict(test_set)

#Results of the prediction
print result

#Predicting the values from the test set
print alg.predict_proba(test_set)

#The order of classes
#0 -> NotSpam		1 -> Spam
print alg.classes_


#Get accuracu score
from sklearn.metrics import accuracy_score
print "Accuracy score: ",accuracy_score(true_labels,result)
import csv
import requests
import pandas as pd
import numpy as numpy

url = 'http://text-processing.com/api/sentiment/'

def sentiment(data):
	sentURL = 'http://text-processing.com/api/sentiment/'
	sentData = {'text':data}
	r = requests.post(sentURL, data=sentData)
	return r.json()

bigDict = {}
count = 0
with open('gDoorRev.csv') as f:
	reader = csv.DictReader(f)
	# reader = csv.reader(f)
	# next(reader)
	for row in reader:
		index = row['']
		overview = row['summary']
		positive = row['pro']
		negative = row['con']
		totalstars = row['overallStar']
		posSent = sentiment(positive)
		negSent = sentiment(negative)
		print('Positive review sentiment analysis == {}\n'\
		      'Positive = {}% ,\nNegative = {}%\n'.
		      format(posSent['label'], posSent['probability']['pos']*100,
		             posSent['probability']['neg']*100))
		print('Negative review sentiment analysis == {} \n'\
		      'Positive = {}%,\nNegative = {}%'
		      .format(negSent['label'], negSent['probability']['pos']*100,
		             negSent['probability']['neg']*100))
		print('{} Stars for recommending\n\n'.format(totalstars))
		print('-----------------')

#		print(posSent['label'])


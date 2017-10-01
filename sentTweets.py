import json
import requests

fileJSON = json.load(open('tTweets.json'))

sentURL = 'http://text-processing.com/api/sentiment/'

for data in fileJSON:
	tweet = json.dumps(data['text'])#.strip('"')
	sentData = {'text':tweet}
	r = requests.post(sentURL, data=sentData)
	sentD = r.json()
	negSentProb = sentD['probability']['neg']
	posSentProb = sentD['probability']['pos']
	neutralSentProb = sentD['probability']['neutral']

	print(tweet)
	print('Negative %: {}'.format(negSentProb*100))
	print('Positive %: {}'.format(posSentProb*100))
	print('API guesses its {}'.format(sentD['label']))
	print('------------')

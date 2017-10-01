import csv
import requests

wordList = []

url = 'http://text-processing.com/api/sentiment/'

with open('gDoorRev.csv', 'rb') as csv_file:
	# for x in csv_file:#.readlines():
	# 	print x[0]
	myFile = csv.reader(csv_file)
	count = 0
	while count < 2:
		for row in myFile:
			# print(row[6])
			review = row[6]
			data = {'text':review}
			r = requests.post(url, data=data)
			print(review)
			print(r.content)
			count += 1
		# words = review.split()
		# wordList.append(words)

# print wordList[1]

# url = 'http://text-processing.com/api/sentiment/'

# for text in wordList[1]:
# 	data = {'text':text}
# 	r = requests.post(url, data=data)
# 	print(r.content)
# 	# print(text)

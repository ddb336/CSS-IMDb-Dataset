import nltk
nltk.download('vader_lexicon')
import csv
import csv
import operator
import os.path
from os import path

from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

csv_file = open("all_reviews_filtered_10000.csv")
csv_reader = csv.reader(csv_file, delimiter=",")

ids = []
first = True
for row in csv_reader:
    if first:
        first = False
        continue
    ids.append(row[0])

csv_file.close()

for movie_id in ids:

    if path.exists('filtered-with-sentiment/' + movie_id + '_reviews_sentiment.csv'):
        continue

    print('doing' + movie_id)

    csv_file = open('filtered-reviews/'+movie_id+'_reviews_filtered.csv')
    csv_reader = csv.reader(csv_file, delimiter=",")

    with open('filtered-with-sentiment/'+movie_id+'_reviews_sentiment.csv', mode='w') as data_file:
        data = csv.writer(data_file, delimiter=',')

        first = True
        for row in csv_reader:
            if first:
                data.writerow(row[:1] + ['title_sentiment_score','text_sentiment_score'] + row[1:])
                first = False
                continue
            data.writerow(row[:1] + [sia.polarity_scores(row[0])['compound'],sia.polarity_scores(row[3])['compound']] + row[1:])











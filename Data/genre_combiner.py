
import csv

csv_file = open("all_reviews_filtered_10000.csv")
csv_reader = csv.reader(csv_file, delimiter=",")

genre_dict = {}
first = True
for row in csv_reader:
    if first:
        first = False
        continue
    genres = row[2].split(",")
    for genre in genres:
        if genre in genre_dict:
            genre_dict[genre].append(row[0])
        else:
            genre_dict[genre] = [row[0]]

csv_file.close()

for genre in genre_dict:

    with open('genres-combined/'+genre+'_reviews_combined.csv', mode='w') as data_file:
        data = csv.writer(data_file, delimiter=',')

        data.writerow(['title','title_sentiment_score','text_sentiment_score','date','rating'])
        for movie in genre_dict[genre]:
        
            csv_file = open("filtered-with-sentiment/"+ movie +"_reviews_sentiment.csv")
            csv_reader = csv.reader(csv_file, delimiter=",")
            
            first = True
            for row in csv_reader:
                if first:
                    first = False
                    continue
                data.writerow(row[:5])

            csv_file.close()

    print('done with ', genre)





















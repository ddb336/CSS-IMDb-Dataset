import csv
import operator
import os.path
from os import path

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

num_movies = 0
num_reviews = 0

with open('movie_stats.csv', mode='w') as data_file:
    data = csv.writer(data_file, delimiter=',')
    data.writerow(['title_id', 'num_reviews', 'avg_rating'])
    
    for movie_id in ids:
        if not path.exists('filtered-reviews/' + movie_id + '_reviews_filtered.csv'):
            continue

        num_movies += 1

        individual_num = 0
        cumulative_rating = 0
        
        csv_file = open('filtered-reviews/' + movie_id + "_reviews_filtered.csv")
        csv_reader = csv.reader(csv_file, delimiter=",")

        first = True
        for row in csv_reader:
            if first:
                first = False
                continue
            individual_num += 1
            cumulative_rating += int(row[2])
            num_reviews += 1

        data.writerow([movie_id,individual_num,cumulative_rating/individual_num])

        csv_file.close()


print("Number of movies: ", num_movies)
print("Number of reviews total: ", num_reviews)
print("Average reviews per movie: ", num_reviews/num_movies)
















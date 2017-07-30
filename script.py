#run this script to import the csv data

from classification.models import Tweet
import csv

with open("output_got_clean.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        try:
            tweet_id = int(row['id'])
        except ValueError:
            tweet_id = 00000000
        tweet = Tweet(tweet_id=tweet_id, tweet_username=row['username'], tweet_text=row['text'])
        tweet.save()


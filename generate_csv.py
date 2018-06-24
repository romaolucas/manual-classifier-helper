import csv
import django
import os
import codecs
from classification.models import Tweet, Review

with open('output_clam.csv', mode='w') as output:
    reviewed_tweets = Tweet.objects.filter(review__isnull=False) \
            .filter(review__ironic=False)
    fieldnames = ['username', 'tweet', 'review']
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    for tweet in reviewed_tweets:
        writer.writerow({'username': tweet.tweet_username, 'tweet': tweet.tweet_text.encode('utf-8').decode('utf-8'), 'review': tweet.review_set.all()[0].review})



import csv
import locale
import random

import time
import datetime
import pymongo

# configuration
import time

MONGODB_HOST = '192.168.50.10'
MONGODB_PORT = 27017

connection = pymongo.MongoClient(MONGODB_HOST, MONGODB_PORT)
tweets = connection["musiccity"].get_collection("tweets")
#start = datetime.datetime.now()
tweet = {}
with open("Berlin_tweets_example.csv", "rU") as data_file:
    spamreader = csv.reader(data_file, delimiter=',', quotechar='|')
    for row in spamreader:
        tweet['timestamp'] = long("1491062819123") - random.randrange(0, 100001, 2)
        tweet['text'] = row[2]
        tweet['geo_coordinates'] = [row[4], row[3]]
        print tweet
    tweets.insert_one(tweet)

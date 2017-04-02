from flask import Flask, render_template, make_response, json
import pymongo

# configuration
from flask_cors import CORS

MONGODB_HOST = '192.168.50.10'
MONGODB_PORT = 27017

app = Flask(__name__)
app.config.from_object(__name__)
cors = CORS(app)


@app.route("/")
def index():
    connection = pymongo.MongoClient(MONGODB_HOST, MONGODB_PORT)
    db = connection['musiccity']
    tweets = db.tweets
    #start = datetime.datetime.now()
    tweets_cursor = tweets.find({"geo_coordinates": {"$type": "double"},
                                 "$text": {"$search": "music party concert orchestra bar club piano theatre show vibes"
                                                      "vinyl hiphop rap video guitar voice festival remix housemusic"
                                                      "live song singing musician knorkator techno electro electronic"
                                                      "rave berlin spring bvg"}},
                                {"_id": 0, "timestamp": 1, "text": 1, "geo_coordinates": 1}).sort("timestamp")
    tweets = []
    for tweet in tweets_cursor:
        print tweet
        tweets.append(tweet)
    results = json.dumps(tweets)
    #results = {"results": tweets}
    #print tweets_cursor[0]
    output = make_response(results)
    output.headers['Content-Type'] = 'application/json'
    return output


@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
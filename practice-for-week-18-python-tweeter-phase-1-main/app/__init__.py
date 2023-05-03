# !!START
from flask import Flask, render_template, redirect
from .config import Config
from .tweets import tweets
from random import choice
from .form.tweet_form import NewTweetForm
from datetime import datetime


app = Flask(__name__)

app.config.from_object(Config)

@app.route('/')
def index():
    tweet = choice(tweets)
    return render_template("index.html", tweet=tweet)

@app.route('/feed')
def all_tweets():
    return render_template("feed.html", tweets=tweets)

@app.route('/new', methods=['GET', 'POST'])
def post_tweet():
    form = NewTweetForm()

    if form.validate_on_submit():
        new_tweet = {
            'id': len(tweets),
            'author': form.data['author'],
            'tweet': form.data['tweet'],
            'date': datetime.today().strftime('%Y-%m-%d'),
            'likes': 0
        }
        print(new_tweet)
        tweets.append(new_tweet)

        return redirect('/feed')

    if form.errors:
        return redirect('/')

    return render_template('new_tweet.html', form=form)
# !!END

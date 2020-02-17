from flask import Flask, render_template
import praw
import pandas as pd  
import datetime as dt  

app = Flask(__name__)

SECRET_14 = "4NcuhiVc1XT2lQ"
SECRET_27 = "CqgdWlimZCadgIYnxKRCrSva3EA"

reddit = praw.Reddit(
	client_id = SECRET_14, 
	client_secret = SECRET_27,
	user_agent = "jojo",
	username = 'CrazyDiamondDorara',
	password = 'YoshikageKira'
	)

subreddit = reddit.subreddit('ShitPostCrusaders')

top_posts = subreddit.top(limit = 100)

LST = []

for post in top_posts:
	LST.append(post)

top_posts = LST


@app.route("/")
@app.route("/home")
def test():
	return render_template('test.html', posts = top_posts, length = len(top_posts))


#@app.route("/about")
#def about():
#	return render_template('about.html', title='About')



if __name__ == '__main__':
	app.run(debug=True)

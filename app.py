from flask import Flask, render_template
app = Flask(__name__)

SECRET_14 = "MOw9i0pU3SPF9A"
SECRET_23 = "4uV_pssc9L7ZYsBBEVVlXwroOhk"

posts = [
	{
		'author': 'Araki',
		'title': 'JOJO',
		'content': 'JOJO IS ART',
		'date_posted': 'February 16, 2020'
	},
	{
		'author': 'Araki',
		'title': 'JOJO2',
		'content': 'JOJO IS ART',
		'date_posted': 'February 16, 2020'
	}
]


@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts = posts)


@app.route("/about")
def about():
	return render_template('about.html', title='About')



if __name__ == '__main__':
	app.run(debug=True)

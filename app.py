from flask import Flask, render_template,url_for

app = Flask(__name__)

posts = [{
		"name":"Name: Jayasurya Karthikeyan",
		"runs_scored": "Runs Scored: 25364",
		"average":"Average : 63",
		"batting":"Batting: Left hand batsman",
		},
		{
		"name":"Name : Virat Kohli",
		"runs_scored": "Runs Scored: 65764",
		"average":"Average: 55",
		"batting":"Batting: Right hand batsman",
		},
]

@app.route('/')
def home():
	return render_template("home.html", posts = posts)

@app.route('/about')
def about():
	return render_template("about.html", title = 'ABOUT')

if __name__ == "__main__":
	app.run(debug = True)
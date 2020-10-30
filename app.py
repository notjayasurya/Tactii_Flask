from flask import Flask, render_template

app = Flask(__name__)

posts = [{
		"name":"jayasurya",
		"runs_scored": "25364",
		"average":"63",
		"batting":"Left hand batsman",
		},
		{
		"name":"Virat Kohli",
		"runs_scored": "65764",
		"average":"55",
		"batting":"Right hand batsman",
		},
]

@app.route('/')
def home():
	return render_template("home.html", posts = posts)

@app.route('/about')
def about():
	return render_template("about.html")

if __name__ == "__main__":
	app.run(debug = True)
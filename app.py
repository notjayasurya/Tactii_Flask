from flask import Flask, render_template,url_for,flash,redirect
from regform import RegistrationForm
from loginform import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'jayasurya'

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


@app.route('/register' , methods = ['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!','success')
		return redirect(url_for('home'))
	return render_template("register.html", title = 'REGISTER',form = form)

@app.route('/login')
def login():
	form = LoginForm()
	return render_template("login.html", title = 'LOGIN', form = form)

if __name__ == "__main__":
	app.run(debug = True)
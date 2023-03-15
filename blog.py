from flask import Flask, render_template




# Create a Flask Instance

app = Flask(__name__)


# Create a decorator
@app.route('/')

def index():
	first_name = "Mambwe"
	return render_template('index.html', first_name=first_name)


# localhost:5000/user/Mambwe
@app.route('/user/<name>')

def user(name):
	return render_template('user.html', user_name=name)



#  Invalid URL
@app.errorhandler(404)

def page_not_found(e):
	return render_template("404.html"), 404


@app.errorhandler(500)

def page_not_found(e):
	return render_template("500.html"), 500



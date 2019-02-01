from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	increment()
	return render_template('index.html', counter = session["counter"])
   
@app.route('/double')
def double():
	increment()
	return redirect('/')

@app.route('/reset')
def reset():
	session["counter"] = 0
	return redirect('/')
	
def increment():
 	try:
		session["counter"] = session["counter"] + 1
	except KeyError:
		session["counter"] = 1

		
app.run(debug=True) # run our server
from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	newRand()
		
	return render_template('index.html', flag = "none")
   
@app.route('/checkAnswer', methods=['POST'])
def checkAnswer():
	guess = int(request.form['guess'])
	
	if guess > int(session["rand"]):
		return render_template('index.html', flag = "high", guess = guess, ans = session["rand"])
	elif guess < int(session["rand"]):
		return render_template('index.html', flag = "low", guess = guess, ans = session["rand"])
	elif guess == int(session["rand"]):
		newRand()
		return render_template('index.html', flag = "correct", guess = guess, ans = session["rand"])
	else:
		return redirect("/")

def newRand():
	session["rand"] = random.randrange(0, 101)
	
app.run(debug=True) # run our server
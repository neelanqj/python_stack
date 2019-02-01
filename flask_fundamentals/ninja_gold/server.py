from flask import Flask, render_template, request, redirect, session
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
 	try:
		if (session['gold'] == None):
			session["gold"] = 0
			session["activities"] = []
	except KeyError:
		session["gold"] = 0
		session["activities"] = []
	
	return render_template('index.html', money = session["gold"], activities = session["activities"])
   
@app.route('/process_money', methods=['POST'])
def process_money():
	activities_list = session["activities"]
	
	if request.form['building'] == "farm":
		goldEarned = random.randrange(10, 20)
		session["gold"] += goldEarned
		session["activities"].append( { 'color': 'green', 'comment': perform_action("farm", goldEarned), 'value': goldEarned } )

	elif request.form['building'] == "cave":
		goldEarned = random.randrange(5, 10)
		session["gold"] += goldEarned
		session["activities"].append( { 'color': 'green', 'comment': perform_action("cave", goldEarned), 'value': goldEarned } )
	
	elif request.form['building'] == "house":
		goldEarned = random.randrange(2, 5)
		session["gold"] += goldEarned
		session["activities"].append( { 'color': 'green', 'comment': perform_action("house", goldEarned), 'value': goldEarned } )
	
	elif request.form['building'] == "casino":	
		goldEarned = random.randrange(-50, 50)
		session["gold"] += goldEarned

		if goldEarned > 0:
			session["activities"].append( { 'color': 'green', 'comment': perform_action("casino", goldEarned), 'value': goldEarned } )
		else:
			session["activities"].append( { 'color': 'red', 'comment': perform_action("casino", goldEarned), 'value': goldEarned } )
	
	session["activities"] = activities_list
	
	return render_template('index.html', money = session["gold"], activities = activities_list)

def perform_action(building, money):
	if money > 0:
		return 'Earned ' + str(money) + ' from the ' + building + '(' + str(datetime.now().time()) +')'
	else: 
		return 'Entered a casino and lost ' + str(money) + ' golds... Ouch ...' + '(' + str(datetime.now().time()) +')'
		
app.run(debug=True) # run our server
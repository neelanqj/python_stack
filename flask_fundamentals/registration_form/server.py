from flask import Flask, render_template, request, redirect, flash
import re
app = Flask(__name__)

app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	return render_template('index.html') 

@app.route('/submit', methods=['POST'])
def submit_form():		
	email = request.form['email']
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	password = request.form['password']	
	confirm_password = request.form['confirm_password']	
	
	errors = 0

	if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
		flash("Invalid email.")
		errors += 1
		
	if not re.match(r"^[a-zA-Z]+$", first_name):
		flash("Invalid first name.")
		errors += 1
		
	if not re.match(r"^[a-zA-Z]+$", last_name):
		flash("Invalid last name.")
		errors += 1
	
	if email == "":
		flash("Name is not allowed to be empty.")
		errors += 1
		
	if first_name == "":
		flash("Location is not allowed to be empty.")
		errors += 1
		
	if last_name == "":
		flash("Language is not allowed to be empty.")
		errors += 1
		
	if password == "":
		flash("Comment is not allowed to be empty.")
		errors += 1
	
	if len(password) <= 8:
		flash("Password is too short.")
		errors += 1
	
	if password !=  confirm_password:
		flash("Passwords do not match.")
		errors += 1
		
	if errors == 0:
		flash("All inputs are great!.")
		return redirect('/')
	else:
		return redirect('/')

app.run(debug=True)
from flask import Flask, render_template, request, redirect, session, flash
import re
from mysqlconnection import MySQLConnector
import hashlib
app = Flask(__name__)
mysql = MySQLConnector(app,'login')

app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	return render_template('login.html') 
	
@app.route('/login', methods=['POST'])
def login_user():
	email = request.form['email']
	password = request.form['password']
	hashed_password = hashlib.md5(password).hexdigest()
	
	query = "SELECT * FROM user WHERE email = '" + email + "' AND password = '" + hashed_password + "'"
    	user = mysql.query_db(query)

	if len(user) == 0:
		flash("Invalid username or password.")
		return redirect('/')
	else:		
		session['email'] = email
		session['password'] = hashed_password
		return redirect('/success')
		
@app.route('/register')
def register():
	return render_template('register.html') 
	
@app.route('/success')
def success():
	return render_template('success.html') 

@app.route('/register_user', methods=['POST'])
def register_user():		
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
		
	if first_name == "" and len(first_name) > 1:
		flash("First name is not allowed to be empty.")
		errors += 1
		
	if last_name == "" and len(last_name) > 1:
		flash("Last name is not allowed to be empty.")
		errors += 1
		
	if password == "":
		flash("Password is not allowed to be empty.")
		errors += 1
	
	if len(password) < 8:
		flash("Password is too short.")
		errors += 1
	
	if password != confirm_password:
		flash("Passwords do not match.")
		errors += 1
	
	hashed_password = hashlib.md5(password).hexdigest()
	
	if errors == 0:
		flash("Registration Successful! Please Log In.")
		query = "INSERT INTO user (first_name, last_name, email, password) VALUES (:first_name, :last_name, :email, :password)"
		# We'll then create a dictionary of data from the POST data received.
		data = {
				 'first_name': first_name,
				 'last_name':  last_name,
				 'email': email,
				 'password': hashed_password
			   }
		# Run query, with dictionary values injected into the query.
		mysql.query_db(query, data)
		return redirect('/')
	else:
		return redirect('/register')

		
		
app.run(debug=True)
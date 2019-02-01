from flask import Flask, render_template, request, redirect, session, flash
import re
from mysqlconnection import MySQLConnector
import hashlib
app = Flask(__name__)
mysql = MySQLConnector(app,'the_wall')

app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	return render_template('login.html') 
	
@app.route('/login', methods=['POST'])
def login_user():
	email = request.form['email']
	password = request.form['password']
	
	hashed_password = hashlib.md5(password).hexdigest()
	
	query = "SELECT * FROM users WHERE email = '" + email + "' AND password = '" + hashed_password + "'"
    	user = mysql.query_db(query)
		# user.itervalues().next().id

	if len(user) == 0:
		flash("Invalid username or password.")
		return redirect('/')
	else:		
		print user
		session['name'] = user[0]['first_name'] + " " +user[0]['last_name']
		session['id'] =  user[0]['id']
		print session['id'] 
		return redirect('/wall')

@app.route('/logoff')
def logoff_user():
	session.clear()
	return redirect('/')

@app.route('/register')
def register():
	return render_template('register.html') 

@app.route('/wall')
def wall():
	user_name = session["name"]
	query = "SELECT m.id, m.message, u.first_name, u.last_name, DATE_FORMAT(m.created_at, '%M %d %Y') as created_at FROM messages m inner join users u on m.user_id = u.id"
    	messages = mysql.query_db(query)
	print messages
	query = "SELECT m.message_id, m.comment, u.first_name, u.last_name, DATE_FORMAT(m.created_at, '%M %d %Y') as created_at FROM comments m inner join users u on m.user_id = u.id"
	comments = mysql.query_db(query)
	return render_template("wall.html", all_messages = messages, all_comments = comments, current_user = user_name)
	
@app.route('/add_message', methods=['POST'])
def add_message():
	query = "INSERT INTO messages (user_id, message) VALUES (:user_id, :message)"
	# We'll then create a dictionary of data from the POST data received.
	data = {
			 'user_id': session['id'],
			 'message':  request.form['message']
		}
	# Run query, with dictionary values injected into the query.
	mysql.query_db(query, data)	
	return redirect('/wall')
	
@app.route('/reply_message', methods=['POST'])
def reply_message():
	query = "INSERT INTO comments (user_id, message_id, comment) VALUES (:user_id, :message_id, :comment)"
	# We'll then create a dictionary of data from the POST data received.
	data = {
			 'user_id': session['id'],
			 'message_id':  request.form['message_id'],
			 'comment': request.form['comment']
		}
	# Run query, with dictionary values injected into the query.
	mysql.query_db(query, data)	
	return redirect('/wall')
	
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
		query = "INSERT INTO users (first_name, last_name, email, password) VALUES (:first_name, :last_name, :email, :password)"
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
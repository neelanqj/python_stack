from flask import Flask, render_template, request, redirect, session, flash
import re
from mysqlconnection import MySQLConnector
import hashlib
app = Flask(__name__)
mysql = MySQLConnector(app,'rest')

app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	return redirect('/users') 
	
@app.route('/users', methods=['GET'])
def users():
	query = "SELECT * FROM users"
    	users = mysql.query_db(query)

	return render_template('users.html', all_users = users)
	
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
	query = "SELECT * FROM users WHERE id = " + str(id)
    	users = mysql.query_db(query)

	return render_template('show_user.html', first_name = users[0]['first_name'], last_name = users[0]['last_name'], email = users[0]['email'], created_at = users[0]['created_at'], id = id)
		
@app.route('/users/new', methods=['GET'])
def put_user():
	return render_template('new_user.html')

@app.route('/users/<id>/edit', methods=['GET'])
def edit_user(id):
	query = "SELECT * FROM users WHERE id = " + str(id)
    	users = mysql.query_db(query)

	return  render_template('edit_user.html', first_name = users[0]['first_name'], last_name = users[0]['last_name'], email = users[0]['email'], created_at = users[0]['created_at'], id = id)
	
@app.route('/users/<id>', methods=['POST'])
def post_user(id):
	query = "UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email WHERE id =" + str(id)
	print query
	# We'll then create a dictionary of data from the POST data received.
	data = {
			 'first_name': request.form['first_name'],
			 'last_name':  request.form['last_name'],
			 'email': request.form['email']
		}
	# Run query, with dictionary values injected into the query.
	mysql.query_db(query, data)	

	return  redirect('/users/' + str(id))

@app.route('/users/create', methods=['POST'])
def new_user():
	query = "INSERT INTO users (first_name, last_name, email) VALUES (:first_name, :last_name, :email)"
	# We'll then create a dictionary of data from the POST data received.
	data = {
			 'first_name': request.form['first_name'],
			 'last_name':  request.form['last_name'],
			 'email': request.form['email']
		}
	# Run query, with dictionary values injected into the query.
	id = mysql.query_db(query, data)	
	
	return redirect('/users/'+str(id))

@app.route('/users/<id>/destroy')
def delete(id):
	query = "DELETE FROM users WHERE id = "+str(id)
	mysql.query_db(query)
	return redirect('/')
	
app.run(debug=True)
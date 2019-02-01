from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

mysql = MySQLConnector(app,'emails')

@app.route('/')
def index():
    return render_template('index.html')
	
@app.route('/check', methods=['POST'])
def check():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
	query = "SELECT * FROM emails WHERE email = :check_email"
	data = {
             'check_email': request.form['email']
           }
		   
	# Run query, with dictionary values injected into the query.
	result = mysql.query_db(query, data)

	query = "SELECT * FROM emails"
	result2 = mysql.query_db(query)

    	if len(result) == 0:
        	flash("Email does not exist!")
		return redirect('/')
	else:
		message = "The email you entered " + data['check_email'] + " is a VALID email address! Thank You!"
		flash(message)
		return render_template('success.html', emails = result2)	
	
app.run(debug=True)
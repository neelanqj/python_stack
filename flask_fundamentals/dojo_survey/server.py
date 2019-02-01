from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)

app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	return render_template('index.html') 

@app.route('/result', methods=['POST'])
def ninjas():		
	name = request.form['name']
	location = request.form['location']	
	language = request.form['language']	
	comment = request.form['comment']
	
	errors = 0
	
	if len(comment) > 120:
		flash("Comments are too long!")
		errors += 1

	if name == "":
		flash("Name is not allowed to be empty.")
		errors += 1
		
	if location == "":
		flash("Location is not allowed to be empty.")
		errors += 1
		
	if language == "":
		flash("Language is not allowed to be empty.")
		errors += 1
		
	if comment == "":
		flash("Comment is not allowed to be empty.")
		errors += 1

	if errors == 0:
		return render_template('results.html', name=name, location=location, language=language, comment=comment)
	else:
		return redirect('/')

app.run(debug=True)
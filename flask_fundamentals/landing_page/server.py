from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return "No ninjas here" 

@app.route('/ninja')
def ninjas():
  return render_template('ninjas.html')
  

@app.route('/ninja/<ninja>')
def ninjas(ninja):
  return render_template('ninjas.html')
  
@app.route('/dojos/new')
def dojo():
  return render_template('dojos.html')
  
app.run(debug=True)
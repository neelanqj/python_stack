from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return "No ninjas here."

@app.route('/ninja/', methods=['GET'])
@app.route('/ninja/<image>', methods=['GET'])
def ninjas_colored(image=""):
	if image == "blue":
		picture = "/static/img/leonardo.jpg"
	elif image == "orange":
		picture = "/static/img/michelangelo.jpg"
	elif image == "purple":
		picture = "/static/img/donatello.jpg"
	elif image == "red":
		picture = "/static/img/raphael.jpg"
	elif image == "":
		picture = "/static/img/tmnt.png"
	else:
		picture = "/static/img/notapril.jpg"
		
	return render_template('ninjas.html', picture = picture)
   
app.run(debug=True) # run our server
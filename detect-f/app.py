from flask import Flask, request, render_template, jsonify, redirect, make_response
import base64
import pickle
import pred


app = Flask(__name__)

prediction=""
citation1=""
citation2=""


def checkfor(query):
	listoftrustedsites = ["www.bbc.com","www.nytimes.com","www.hindustantimes.com","www.thehindu.com"]	
	if query in listoftrustedsites:
		return "Trusted"
	else:
		return "Untrusted"
@app.route('/')
def home():

	if request.method=='GET':
		return render_template('index.html')

@app.route('/check', methods=['POST','GET'])
def check():
	if request.method == 'POST':
		query = request.form['query']
		res,citations = pred.predict(query)
		if res == 1:
			prediction="Probably Fake"
		elif res == 0:
			prediction="Probably Real"
		else :
			prediction="Argueable"
		print(res)
		return render_template('index.html', prediction_text='The news is {}'.format(prediction), citation = citations )
	else:
		return render_template('index.html')


@app.route("/checkjs", methods=["POST","GET"])
def checkjs():
	query = request.args.get("query")
	'''
	if validators.url(query):
		valid=checkfor(query)
		print(valid)
		response = make_response(jsonify({"validation":valid}))
		return response
		
	else:
 	'''
	res,citation, = pred.predict(query)
	res,_ = pred.predict(query)
	if res == 1:
		prediction="Probably Fake"
	elif res == 0:
		prediction="Probably Real"
	else :
		prediction="Argueable"
	response = make_response(jsonify({"prediction":prediction, "citations":citation}))
	return response
	
@app.route("/checkvalidation", methods=["POST","GET"])
def checkval():

	query = request.args.get("query")
	valid=checkfor(query)
	print(valid)
	response = make_response(jsonify({"validation":valid}))
	return response
if __name__ == "__main__":
	app.run(debug = False)

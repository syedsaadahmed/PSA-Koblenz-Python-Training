from app import app
from flask import render_template, request
from pymongo import MongoClient
import json
from bson import json_util


@app.route('/hello')
@app.route('/')
def helloworld():
	return 'hello world'

@app.route('/info')
@app.route('/index')
def info():
	return {
		"user":"Saad",
		"city":"koblenz",
		"country":"Germany",
	}

@app.route('/user/<name>', methods=['GET'])
def givename(name):
	return '{}\'s Hello'.format(name)

@app.route('/login')
def mynewpage():
	return render_template('index.html')

#templating, Python-flask uses JINJA templating
@app.route('/templating')
@app.route('/template/<name>')
def templating_func(name):
	return render_template('temp.html', title='home page', name=name)


#for creating connection to mongoDB
uri = 'mongodb://saadahmed20940:syed2saad@ds241968.mlab.com:41968/fullstack?retryWrites=false'
client = MongoClient(uri,connectTimeoutMS=30000, socketTimeoutMS=None, socketKeepAlive=True)
db = client.get_default_database()

#route to retrieve data from DB
@app.route('/records')
def get_all_records():
	try:
		all_data = list(db.test.find())
		#db.test.find() is equivalent to select * from test
		return json.dumps(all_data, default=json_util.default)
	except Exception as e:
		return json.dumps({'error':str(e)})


#route to submit data to DB
@app.route('/submit',methods=['POST'])
def submitdata():
	#get the data from user (POSTMAN, PROGRAM. LANGUAGE, HTML FORM)
	data = request.get_json()
	#functionality to submit the data into DB
	if request.method == 'POST':
		data_insertion = [{
			"name":data['name'],
			"class":data['class']
		}]
		db.test.insert_many(data_insertion)
		return json.dumps(True)
	else:
		return 'Get request not allowed on the resource'


#TODO
#Try to use some SQL DB with this basic application.
#Try to explore some concepts related to jinja templating.



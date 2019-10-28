#!flask/bin/python
import json
import requests
import datetime
from flask import Flask, Response
from chucknorris.flaskrun import flaskrun

#Just trigger a deployment pipeline
application = Flask(__name__)

@application.route('/', methods=['GET'])
def get():
	response = requests.get("https://api.chucknorris.io/jokes/random")
	joke = response.json()["value"]
	data = {
		'joke': joke,
		'timestamp': datetime.datetime.utcnow().isoformat()
	}
	return Response(json.dumps(data), mimetype='application/json', status=200)


if __name__ == '__main__':
    flaskrun(application)

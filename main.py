import flask
import requests
from flask import jsonify

app = flask.Flask(__name__)


@app.route('/hello/<name>', methods=['GET'])
def hello(name):
    message = {
        "greeting": 'Hello',
        "name": name
    }
    return jsonify(message)

@app.route('/distance/<frm>/<to>', methods=['GET'])
def distance(frm, to):
    apiKey = "EgCY4hR3CMStzP5taEAT4xRT0cMW392a18rKTZQjNV7YHjdrpaQaiIeMtHshpYsr"
    zipCodeURL = 'https://www.zipcodeapi.com/rest/'

    req = requests.get(zipCodeURL + apiKey + '/distance.json/' + frm + '/' + to + '/mile')
    if (req.status_code == 200):
        return req.json()
    else:
        print(req.status_code + req.text)
        return jsonify({distance: -1})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

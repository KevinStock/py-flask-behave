import flask
import json

app = flask.Flask(__name__)


@app.route('/hello/<name>', methods=['GET'])
def hello(name):
    message = {
        "greeting": 'Hello',
        "name": name
    }
    return json.dumps(message)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
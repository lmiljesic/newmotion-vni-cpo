import flask

app = flask.Flask(__name__)

@app.route('/health_check', methods=['GET'])
def health_check():
    return {"status":"pass"}

@app.route('/', methods=['GET'])
def share_data():
    return "You just received a package of data."

app.run(host='0.0.0.0', port=80)
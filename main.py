from utils.constants import DATA, VALUE_P, TEST
from utils.process import Process
from threading import Thread
import json

from flask import Flask, Response, request
app = Flask(__name__)
Proc = Process()
@app.route('/maximin', methods=['POST'])
def maximin():
    req_data = request.get_json()
    Proc.set_table(req_data['data'])
    return Response(json.dumps(Proc.get_results_maximin()), status=200, mimetype='application/json')

@app.route('/maximax', methods=['POST'])
def maximax():
    req_data = request.get_json()
    Proc.set_table(req_data['data'])
    return Response(json.dumps(Proc.get_results_maximax()), status=200, mimetype='application/json')

@app.route('/laplace', methods=['POST'])
def laplace():
    req_data = request.get_json()
    Proc.set_table(req_data['data'])
    return Response(json.dumps(Proc.get_results_laplace()), status=200, mimetype='application/json')

@app.route('/optimist_pesimist', methods=['POST'])
def optimist_pesimist():
    req_data = request.get_json()
    Proc.set_table(req_data['data'])
    return Response(json.dumps(Proc.get_optimist_pesimist(req_data['valueP'])), status=200, mimetype='application/json')

@app.route('/minimax', methods=['POST'])
def minimax():
    req_data = request.get_json()
    Proc.set_table(req_data['data'])
    return Response(json.dumps(Proc.get_results_minimax()), status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)
        



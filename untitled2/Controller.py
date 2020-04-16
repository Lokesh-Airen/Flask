from flask import Flask, jsonify , request
import pickle
import lightgbm
import numpy as np
from Handler import HandlerClass
from mlmodel import mlmodel
import json
app = Flask(__name__)


# model = pickle.load(open('/Users/lokesh/Desktop/final_prediction1.pickle', 'rb'))

@app.route('/getprediction', methods=['POST'])
def func():
	raw_data = request.get_json(force=True)
	#print(raw_data)
	#result = {}
	op= HandlerClass.getrequest(raw_data)
	resp = mlmodel.pred(op)
	op1=HandlerClass.buildresp(raw_data,resp)
	return op1


# @app.route('/getprediction', methods=['POST'])
# def func(jsonobj):
# 	prediction = model.predict(jsonobj)
# 	return prediction


if __name__ == '__main__':
    app.run()



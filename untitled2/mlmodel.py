import json
import numpy as np
import pickle
import lightgbm
from flask import Flask, jsonify

model = pickle.load(open('/Users/lokesh/Desktop/final_prediction1.pickle', 'rb'))


class mlmodel:

    @staticmethod
    def pred(jsonobj):
        # jsonobj=HandlerClass.getrequest()
        prediction = model.predict(jsonobj)
        return prediction




    #return {'P0':prediction[0][0],'P1':prediction[0][1], 'P2':prediction[0][2]}


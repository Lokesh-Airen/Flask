from mlmodel import  mlmodel
import json
import lightgbm
import numpy as np
import pickle
from flask import Flask, jsonify


class HandlerClass:


    @staticmethod
    def getrequest(raw_data):
        #json1 = { 'f1':0.296296, 'f2':0.079564, 'f3':0.5, 'f4':0.107942, 'f5':0.208333, 'f6':0.588235, 'f7':0.636039, 'f8':0.306832, 'f9':0.189399, 'f10':0.024747, 'f11':0.070483 }
       # model = pickle.load(open('/Users/parikshitnarang/Desktop/task.pickle','rb'))
        dfu=[]
        hotel=raw_data['hotel']
        features=hotel['features']

        # i = 0
        # count = len(raw_data)

        # while i < count:
        #     # obj is a CkJsonObject
        #     obj = raw_data.ObjectAt(i)
        #     mylist = [obj['f1'], obj['f2'], obj['f3'], obj['f4'], obj['f5'], obj['f6'], obj['f7'], obj['f8'], obj['f9'], obj['f10'], obj['f11'],obj['f12'],obj['f13'],obj['f14'],obj['f15'],obj['f16'],obj['f17'],obj['f18'],obj['f19']]
        #     dfu.append(mylist)
        #     i = i + 1




        # for hid,fi in raw_data.items():
        #     mylist = [fi['fprice'], fi['hoteltype'], fi['user_abp'], fi['discount_per'], fi['hotel_btod'], fi['hotel_user_br'], fi['hotel_user_ctr'], fi['hotel_user_btod'], fi['avg_hotel_btod'],fi['abp_price_diff'], fi['recom_score'], fi['ratingcount'],fi['hotel_placeid_ctr'],fi['hotel_placeid_br'],fi['hotel_placeid_dtob'],fi['user_cat_ctr'],fi['user_cat_br'],fi['user_cat_dtob'],fi['distance']]
        #     dfu.append(mylist)


        # mylis=[]
        # for i in hotel:
        #     for key in i:
        #         mylis.append(i[key])
        #     dfu.append(mylis)
        #     mylis=[]


        for i in features:
            dfu.append(i)


        return dfu



    @staticmethod
    def buildresp(raw_data,resp):
        result={}
        newlist=[]
        # count = len(raw_data)
        # while x < count:
        #     # obj is a CkJsonObject
        #     obj = raw_data.ObjectAt(x)
        #     result["hotelid"] = obj['f0']
        #     result["score"]=resp[x]
        #     x= x + 1



        x = 0
        hotel=raw_data['hotel']
        features=hotel['features']
        length=len(features)


        # for hid,fi in raw_data.items():
        #     result[hid]=resp[x]
        #     x= x + 1
        for i in range(length):
            # result[i]=resp[x]
            newlist.append(resp[x])
            x=x+1

        result["score"]=newlist
        return result








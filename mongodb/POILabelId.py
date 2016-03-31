#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient


class POILabelId:
    # 定义旧集合的名字
    collection_old = ''

    # 定义新集合的名字
    collection_new = ''

    # 定义参数字典,其中键为旧集合的字段名,值为新集合的字段名
    # 注意:这里只定义不需要做特殊处理的字段
    params_map = {}

    def __init__(self):
        pass

    @staticmethod
    def attraction_label(address_new, port_new):
        
        client = MongoClient(address_new, port_new)
        travel2 = client.travel2

        label_new = travel2.label
        attraction_new = travel2.attraction
        restaurant_new = travel2.restaurant
        shopping_new =  travel2.shopping
        
        for attraction_document in attraction_new.find():
            if attraction_document['master_label'] is not None and len(attraction_document['master_label']) > 0:
                master_label =  attraction_document['master_label']
                for i in range(len(master_label)):
                        temp = label_new.find_one({'name': master_label[i]['label']})
                        print temp
                        if temp is not None:
                            attraction_new.update({'_id':attraction_document['_id']},{'$set':{'master_label.' + str(i) +'._id': temp['_id'] }})
        print('attraction label id changed')
      
        for restaurant_document in restaurant_new.find():
            if restaurant_document['master_label'] is not None and len(restaurant_document['master_label']) > 0:
                master_label =  restaurant_document['master_label']
                for i in range(len(master_label)):
                        temp = label_new.find_one({'name': master_label[i]['label']})
                        print temp
                        if temp is not None:
                            restaurant_new.update({'_id':restaurant_document['_id']},{'$set':{ 'master_label.' + str(i) +'._id': temp['_id'] }})
        print('restaurant label id changed')
        
        for shopping_document in shopping_new.find():
            if shopping_document['master_label'] is not None and len(shopping_document['master_label']) > 0:
                master_label =  shopping_document['master_label']
                for i in range(len(master_label)):
                        temp = label_new.find_one({'name': master_label[i]['label']})
                        print temp
                        if temp is not None:
                            shopping_new.update({'_id':shopping_document['_id']},{'$set':{ 'master_label.' + str(i) +'._id': temp['_id'] }})
        print('shopping label id changed')
        
        
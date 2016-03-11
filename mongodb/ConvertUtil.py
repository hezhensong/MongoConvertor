#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId


class ConvertUtil:
    def __init__(self):
        pass

    @staticmethod
    def convert_util(address_old, port_old, address_new, port_new, 
                     params_old, params_new):
      
        # old database connection
        client = MongoClient(address_old, port_old)
        travel1 = client.travel1

        # new database connection
        client = MongoClient(address_new, port_new)
        travel2 = client.travel2
      
        # old collection latest city
        db_old = travel1.shoppings
        db_new = travel2.shopping

        # clean former data
        db_new.remove()

        temp = [None] * len(params_old)
        
        print(db_old.find().count())
        for row in db_old.find():
            for i in range(len(params_old)):
                if params_old[i] in row: 
                   temp[i] = row[ params_old[i] ]
                 
            post = {}      
            for i in range(len(params_new)):
                post.update({params_new[i]:temp[i]})
            result = db_new.insert(post)
            print post

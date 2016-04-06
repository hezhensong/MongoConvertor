#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import HTMLParser
import datetime

import pytz
from bson import ObjectId
from pymongo import MongoClient

class Brands:
    def __init__(self):
        pass

    @staticmethod
    def convert_Brands(address_old, port_old, address_new, port_new):
        # old database connection
        client = MongoClient(address_old,port_old)
        travel1 = client.travel1

        # new database connection
        client = MongoClient(address_new, port_new)
        travel3 = client.travel3
        
        # get old collection and create new collection
        oldBrands = travel1.brands
        newBrands = travel3.brands

        # clean former data
        newBrands.remove()
        
        for old_Brands in oldBrands.find():
            post = {'_id': old_Brands['_id']}
            
            # 品牌类型
            if 'advice' in old_Brands:
                post['advice'] = old_Brands['advice']
            else:
                post['advice'] = ''
                
            if 'title' in old_Brands:
                post['title'] = old_Brands['title']
            else:
                post['title'] = ''
            
            if 'desc' in old_Brands:
                post['desc'] = old_Brands['desc']
            else:
                post['desc'] = ''
            
            if 'cover_image' in old_Brands:
                post['cover_image'] = old_Brands['cover_image']
            else:
                post['cover_image'] = ''
            
            
            # 插入数据库
            newBrands.insert(post)
            print(post)
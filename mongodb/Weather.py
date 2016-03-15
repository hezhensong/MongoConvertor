#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient


class Weather:
    
    database_old = 'weathers'
    
    database_new = 'weather'
    
    params_map = {'_id':'_id',                          # 天气 ID
                  'city_id':'city_id',                  # 城市 ID 
                  'cityname':'city_name',               # 城市名字
                  'cityname_en':'city_name_en',         # 城市英文名字
                  'timestamp':'timestamp',             # 更新时间
                  'yahoo_weather':'yahoo_weather'      # Yahoo天气详情
                  }
    
    def __init__(self):
        pass
    
    
    @staticmethod
    def convert_weather(address_old, port_old, address_new, port_new, database_old, database_new,
                     params_map):
      
        # old database connection
        client = MongoClient(address_old, port_old)
        travel1 = client.travel1

        # new database connection
        client = MongoClient(address_new, port_new)
        travel2 = client.travel2
      
        # get old collection and coeate new collection
        db_old = travel1[database_old]
        db_new = travel2[database_new]

        # clean former data
        db_new.remove()

        # 临时数组
        temp = [None] * len(params_map.keys())
        
        # 判断当前文档是否含有某个字段,若有则取出后赋值给临时数组,否则为 None
        for document in db_old.find():
            for i in range(len(params_map.keys())):
                if params_map.keys()[i] in document: 
                   temp[i] = document[ params_map.keys()[i] ]
            
            # 需要特殊处理的字段,处理后以字典的形式添加到 other 中
            other = {}       
            
            post = {}      
            post.update(other)
            for i in range(len(params_map.keys())):
                post.update({params_map.values()[i]:temp[i]})
            db_new.insert(post)
            print post
        

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId
from ConvertUtil import ConvertUtil

class Shopping:
    
    database_old = 'shoppings'
     
    database_new = 'shopping'
    
    params_map = {'_id':'_id',                    # 购物 ID
                  'address':'address',            # 购物地址
                  'city_id':'city_id',            # 城市 ID 
                  'city_name':'city_name',        # 城市名  
                  'comments':'comments',          # 评论
                  'cover_image':'cover_image',    # 背景图片
                  'create_at':'create_at',        # 创建时间
                  'image':'image',                # 图片
                  'introduce':'introduce',        # 介绍
                  'latitude':'latitude',          # 纬度
                  'longitude':'longitude',        # 经度
                  'name':'name',                  # 名字
                  'open_time':'open_time',        # 开放时间
                  'price_desc':'price_desc',      # 价格描述
                  'postal_code':'postal_code',    # 邮编 
                  'ranking':'ranking',            # 排行
                  'rating':'rating',              # 评分
                  'recommand_flag':'is_recommand',# 是否推荐  
                  'tel':'tel',                    # 电话
                  'url':'url',                    # 网址 
                  'image_url':'image_url'         # 图片 url
                }

    def __init__(self):
        pass
    
    @staticmethod
    def convert_shopping(address_old, port_old, address_new, port_new, database_old, database_new,
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
            
            # 需要特殊处理的字段,以字典的形式添加到 other 中
            other = {}       
            
            post = {}      
            post.update(other)
            for i in range(len(params_map.keys())):
                post.update({params_map.values()[i]:temp[i]})
            db_new.insert(post)
            print post
      
       

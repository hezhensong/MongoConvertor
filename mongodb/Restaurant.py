#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId
from ConvertUtil import ConvertUtil

class Restaurant:
    def __init__(self):
        pass
    
    database_old = 'restaurants'
    
    database_new = 'restaurant'
    
    params_map = {'_id':'_id',                           # 餐厅ID
                  'address':'address',                   # 餐厅地址
                  'brief_introduce':'brief_introduce',   # 餐厅简介
                  'city_id':'city_id',                   # 城市 ID 
                  'city_name':'city_name',               # 城市名字
                  'comments':'comments',                 # 评论
                  'comments_from':'comments_from',       # 评论来源
                  'cover_image':'cover_image',           # 背景图片
                  'create_at':'create_at',               # 创建时间
                  'image':'image',                       # 图片
                  'image_url':'image_url',               # 图片 url
                  'info':'info',                         # 餐厅的相关信息    
                  'introduce':'introduce',               # 餐厅介绍
                  'latitude':'latitude',                 # 纬度
                  'longitude':'longitude',               # 经度
                  'menu':'menu',                         # 菜品推荐
                  'name':'name',                         # 名字
                  'openTable_url':'openTable_url',       # 服务预订 url
                  'open_time':'open_time',               # 开放时间
                  'price_desc':'price_desc',             # 价格描述
                  'ranking':'ranking',                   # 排行
                  'rating':'rating',                     # 评分
                  'tags':'tags',                         # 标签
                  'tags_zh':'tags_zh',                   # 中文标签
                  'tel':'tel',                           # 电话
                  'tips':'tips',                         # 提示
                  'website':'website',                   # 网址
                  'price_level':'price_level'            # 价格水平
                  }
    
    @staticmethod
    def convert_restaurant(address_old, port_old, address_new, port_new, database_old, database_new,
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
            result = db_new.insert(post)
            print post
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient
# from bson.objectid import ObjectId


class Attraction:
    def __init__(self):
        pass
    
    database_old = 'latestattractions'
    
    database_new = 'attraction'
    
    params_map = {'_id':'_id',                         # 景点 ID
                  'activities':'activities',           # 景点活动 
                  'address':'address',                 # 景点地址
                  'attractions':'name',                # 景点名
                  'attractions_en':'name_en',          # 景点英文名
                  'city_id':'city_id',                 # 城市 ID
                  'cityname':'city_name',              # 城市名    
                  'comments':'comments',               # 评论 
                  'comments_from':'comments_from',     # 评论来源
                  'coverImageName':'cover_image',      #　封面图片
                  'createPerson':'createPerson',       # 创建者
                  'created':'create_at',               # 创建时间
                  'rank':'ranking',                    # 排行 
                  'image':'image',                     # 图片 
                  'image_url':'image_url',             # 图片 url 
                  'introduce':'introduce',             # 介绍
                  'latitude':'latitude',               # 纬度
                  'longitude':'longitude',             # 经度
                  'masterLabelNew':'master_label',     # 景点所属主题
                  'opentime':'open_time',              # 开放时间
                  'price':'price_desc',                # 价格描述
                  'short_introduce':'brief_introduce', # 简介
                  'telno':'tel',                       # 电话
                  'tips':'tips',                       # 提示
                  'traffic_info':'traffic_info',       # 交通信息
                  'website':'website'                  # 网站
                  }
    
    @staticmethod
    def convert_attraction(address_old, port_old, address_new, port_new, database_old, database_new,
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
            
            # 是否线上展示
            if 'show_flag' in document:
                show_flag = document['show_flag']
                if show_flag == u'1':
                    is_show = True
                else:
                    is_show = False
            else:
                is_show = False
                
            # 是否推荐
            if 'recommand_flag' in document:
                is_recommand = document['recommand_flag']
                if is_recommand == u'1':
                    is_recommand = True
                else:
                    is_recommand = False
            else:
                is_recommand = False

            other.update({'is_show':is_show, 'is_recommand':is_recommand})
            
            post = {}      
            post.update(other)
            for i in range(len(params_map.keys())):
                post.update({params_map.values()[i]:temp[i]})
            db_new.insert(post)
            print post
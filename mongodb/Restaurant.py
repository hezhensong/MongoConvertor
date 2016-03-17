#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId
from ConvertUtil import ConvertUtil

class Restaurant:
    def __init__(self):
        pass
    
    collection_old = 'restaurants'
    
    collection_new = 'restaurant'
    
    params_map = {'_id':'_id', # 餐厅ID
                  'activities': 'activities',  # 餐厅活动
                  'address': 'address',  # 餐厅地址地址
                  'name': 'name',  # 餐厅名
                  'name_en': 'name_en',  # 餐厅英文名
                  'city_id': 'city_id',  # 城市 ID
                  'city_name': 'city_name',  # 城市名
                  'comments': 'comments',  # 评论
                  'comments_from': 'comments_from',  # 评论来源
                  'comments_url': 'comments_url',  # 评论 url
                  'cover_image': 'cover_image',  # 背景图片
                  'image': 'image',  # 图片
                  'introduce': 'introduction',  # 介绍
                  'category': 'master_label',  # 餐厅主标签
                  'tags_zh': 'sub_label',        # 餐厅次标签  
                  'price_desc': 'price_desc',  # 价格描述
                  'brief_introduce': 'brief_introduction',  # 简介
                  'tel': 'tel',  # 电话
                  'tips': 'tips',  # 提示
                  'website': 'website',  # 网站
                  'rating': 'rating',  # 评分
                  'openTable_url':'open_table_url'  # 服务预订 url
                  
                  
                  
#                  'address':'address', # 餐厅地址
#                  'brief_introduce':'brief_introduction', # 餐厅简介
#                  'city_id':'city_id', # 城市 ID 
#                  'city_name':'city_name', # 城市名字
#                  'comments':'comments', # 评论
#                  'comments_from':'comments_from', # 评论来源
#                  'cover_image':'cover_image', # 背景图片
#                  'image':'image', # 图片
#                  'info':'info', # 餐厅的相关信息    
#                  'introduce':'introduce', # 餐厅介绍
#                  'latitude':'latitude', # 纬度
#                  'longitude':'longitude', # 经度
#                  'menu':'menu', # 菜品推荐
#                  'name':'name', # 名字
#                  'openTable_url':'open_table_url', # 服务预订 url
#                  'open_time':'open_time', # 开放时间
#                  'price_desc':'price_desc', # 价格描述
#                  'rating':'rating', # 评分
#                  'tags':'tags', # 标签
#                  'tags_zh':'tags_zh', # 中文标签
#                  'tel':'tel', # 电话
#                  'tips':'tips', # 提示
#                  'website':'website', # 网址
                  }
    
    @staticmethod
    def convert_restaurant(address_old, port_old, address_new, port_new, collection_old, collection_new,
                     params_map):
      
        # old database connection
        client = MongoClient(address_old, port_old)
        travel1 = client.travel1

        # new database connection
        client = MongoClient(address_new, port_new)
        travel2 = client.travel2
      
        # get old collection and coeate new collection
        db_old = travel1[collection_old]
        db_new = travel2[collection_new]

        # clean former data
        db_new.remove()

        # 临时数组
        temp = [None] * len(params_map.keys())
        
        # 判断当前文档是否含有某个字段,若有则取出后赋值给临时数组,否则为 None
        for document in db_old.find().limit(50):
            for i in range(len(params_map.keys())):
                if params_map.keys()[i] in document: 
                   temp[i] = document[ params_map.keys()[i] ]
            
            # 需要特殊处理的字段,处理后以字典的形式添加到 other 中
            coordination = None
            latitude = None
            longitude = None
            open_time = []
            cover_image = None
            title = None
            desc = None
            advice = None
            newdish = []
            facilities = {}
            alcohol = None
            noise = None
            waiter = False
            tv = False
            outseat = False 
            group = False
            kid = False
            card = False
            takeout = False
            delivery = False
            reserve = False
            wifi = False

            other = {}

            if 'latitude' in document:
                latitude =  str(document['latitude'])
            if 'longitude' in document:
                longitude =  str(document['longitude'])
                coordination = latitude + ',' + longitude
                
            if 'open_time' in document:
                temp_open_time = document['open_time']
                if type(temp_open_time) == list:
                    for i in range(len(temp_open_time)):
                        open_time.append(temp_open_time[i]['desc'])
                else:
                    open_time.append(temp_open_time)
            
            
            if 'menu' in document:
                dish = document['menu']
                for i in range(len(dish)):
                    temp_dish = {}
                    cover_image = dish[i]['cover_image']
                    desc = dish[i]['desc']
                    advice = dish[i]['advice']
                    temp_dish.update({'cover_image':cover_image,'desc':desc,
                                      'advice': advice, 'title': title})
                    newdish.append(temp_dish)
            
            if 'info' in document:
                temp_facilities = document['info']
                if 'alcohol' in temp_facilities:
                    alcohol = temp_facilities['alcohol']
                if 'noise' in temp_facilities:
                    noise = temp_facilities['noise']
                if 'waiter' in temp_facilities:
                    waiter = temp_facilities['waiter']
                if 'tv' in temp_facilities:
                    tv = temp_facilities['tv']
                if 'out_seat' in temp_facilities:
                    outseat = temp_facilities['out_seat'] 
                if 'g_f_group' in temp_facilities:
                    group = temp_facilities['g_f_group']
                if 'g_f_kid' in temp_facilities:
                    kid = temp_facilities['g_f_kid']
                if 'card' in temp_facilities:
                    card = temp_facilities['card']
                if 'take_out' in temp_facilities:
                    takeout = temp_facilities['take_out']
                if 'delivery' in temp_facilities:
                    delivery = temp_facilities['delivery']
                if 'yu_ding' in temp_facilities:
                    reserve = temp_facilities['yu_ding']
                if 'wifi' in temp_facilities:
                    wifi = temp_facilities['wifi']
                
                facilities.update({'alcohol': alcohol,'noise': noise, 'waiter': waiter,
                                   'tv': tv, 'outseat': outseat, 'group': group, 'kid': kid,
                                   'card': card, 'takeout': takeout, 'delivery': delivery,
                                   'reserve': reserve, 'wifi': wifi})
                
            other.update({'coordination': coordination ,'open_time': open_time,
                          'dish': newdish, 'facilities': facilities,
                          'last_modified_person': None, 'last_modified_time': None})
            
            post = {}      
            post.update(other)
            for i in range(len(params_map.keys())):
                post.update({params_map.values()[i]:temp[i]})
            db_new.insert(post)
            print post

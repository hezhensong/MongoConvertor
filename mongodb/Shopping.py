#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient


class Shopping:
    collection_old = 'shoppings'

    collection_new = 'shopping'
    
    params_map = {'_id':'_id', # 购物 ID
                  'activities': 'activities', # 购物活动
                  'address': 'address', # 购物地址
                  'name': 'name', # 购物名
                  'name_en': 'name_en', # 购物英文名
                  'city_id': 'city_id', # 城市 ID
                  'city_name': 'city_name', # 城市名
                  'comments': 'comments', # 评论
                  'comments_from': 'comments_from', # 评论来源
                  'comments_url': 'comments_url', # 评论 url
                  'cover_image': 'cover_image', # 背景图片
                  'image': 'image', # 图片
                  'introduce': 'introduction', # 介绍
                  'category': 'sub_tag', # 购物次标签  
                  'price_desc': 'price_desc', # 价格描述
                  'brief_introduce': 'brief_introduction', # 简介
                  'tel': 'tel', # 电话
                  'tips': 'tips', # 提示
                  'url': 'website', # 网站
                  'rating': 'rating', # 评分
                  'brand': 'brand'    # 品牌
                }

    def __init__(self):
        pass

    @staticmethod
    def convert_shopping(address_old, port_old, address_new, port_new, collection_old, collection_new,
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
        for document in db_old.find():
            for i in range(len(params_map.keys())):
                if params_map.keys()[i] in document:
                    temp[i] = document[params_map.keys()[i]]

            # 需要特殊处理的字段,以字典的形式添加到 other 中
            coordination = None
            latitude = None
            longitude = None
            open_time = []
            master_tag = {}
            other = {}
            
            if 'category' in document:
                category = document['category']
                if len(category) > 0:
                    master_tag.update({'_id':category[0]['_id'],'name':category[0]['name']})
                
            if 'latitude' in document:
                latitude = str(document['latitude'])
            if 'longitude' in document:
                longitude = str(document['longitude'])
                coordination = longitude + ',' + latitude
                
            if 'open_time' in document:
                temp_open_time = document['open_time']
                if type(temp_open_time) == list:
                    for i in range(len(temp_open_time)):
                        open_time.append(temp_open_time[i]['desc'])
                else:
                    open_time.append(temp_open_time)
            
            # 是否线上展示
            if 'show_flag' in document:
                show_flag = document['show_flag']
                if show_flag == u'1':
                    is_show = True
                else:
                    is_show = False
            else:
                is_show = False
            
            other.update({'coordination': coordination , 'open_time': open_time,
                          'master_tag': master_tag, 'is_show': is_show,
                          'last_modified_person': None, 'last_modified_time': None})

            post = {}
            post.update(other)
            for i in range(len(params_map.keys())):
                post.update({params_map.values()[i]: temp[i]})
            db_new.insert(post)
            print post

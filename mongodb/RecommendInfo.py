#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient
import datetime
from bson.objectid import ObjectId

class RecommendInfo:
    # 定义旧集合的名字
    collection_old = 'recommendinfo'

    # 定义新集合的名字
    collection_new = 'recommend_info'

    # 定义参数字典,其中键为旧集合的字段名,值为新集合的字段名
    # 注意:这里只定义不需要做特殊处理的字段
    params_map = {
        '_id': '_id',
#        'city_id': 'city_id',
        'city_name': 'city_name',
        'recommend_poi_position': 'coordination'
    }

    def __init__(self):
        pass

    @staticmethod
    def convert_recommend_info(address_old, port_old, address_new, port_new, collection_old, collection_new,
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

            # 需要特殊处理的字段,处理后以字典的形式添加到 other 中
            other = {}

            start_time = None
            start_date = None
            end_time = None
            end_date = None
            year = 0
            month = 0
            day = 0
            new_start_time = None
            new_end_time = None
            recommend_content = None
            cover_image = None
            content_id = None
            content_title = None
            content_first = None
            content_second = None
            content_desc = None
            content_url = None
            city_id = None
            new_city_id = None
            new_type = None
            
            if 'type' in document:
                new_type = int(document['type'])
        
            if 'city_id' in document:
                city_id = document['city_id']
                if city_id != '':
                    if type(city_id) == unicode:
                        city_id = ObjectId(city_id.encode('utf-8'))

            if 'recommend_start_time' in document:
                start_time = document['recommend_start_time']
            if 'recommend_start_date' in document:
                start_date = document['recommend_start_date']
            if 'recommend_start_time' in document:
                end_time = document['recommend_end_time']
            if 'recommend_end_time' in document:
                end_date = document['recommend_end_date']
                
            year = int(start_date[0:4])
            month = int(start_date[4:6])
            day = int(start_date[6:8])
            new_start_time = datetime.datetime(year,month,day,int(start_time))
            
            year = int(end_date[0:4])
            month = int(end_date[4:6])
            day = int(end_date[6:8])
            new_end_time = datetime.datetime(year,month,day,int(end_time))
                    
            if 'recommend_content' in document:
                recommend_content = document['recommend_content']
                if 'recommend_content_id' in recommend_content:
                    content_id = recommend_content['recommend_content_id']
                if 'recommend_content_title' in recommend_content:
                    content_title = recommend_content['recommend_content_title']
                if 'recommend_content_first' in recommend_content:
                    content_first = recommend_content['recommend_content_first']
                if 'recommend_content_second' in recommend_content:
                    content_second = recommend_content['recommend_content_second']
                if 'recommend_content_desc' in recommend_content:
                    content_desc = recommend_content['recommend_content_desc']
                if 'recommend_content_url' in recommend_content:
                    content_url = recommend_content['recommend_content_url']
                if 'cover_image' in recommend_content:
                    cover_image = recommend_content['cover_image']
                            
            other.update({'type': new_type,'city_id': city_id,
                          'start_time': new_start_time, 'end_time': new_end_time,
                          'content': {'content_id': content_id,
                                      'content_title': content_title,
                                      'content_first': content_first,
                                      'content_second': content_second,
                                      'content_desc': content_desc,
                                      'content_url': content_url,
                                      'cover_image': cover_image}})

            post = {}
            post.update(other)
            for i in range(len(params_map.keys())):
                post.update({params_map.values()[i]: temp[i]})
            db_new.insert(post)
            if 'city_id' in document:
                city_id = document['city_id']
                if city_id == '':
                    db_new.remove(document['_id'])
            print post

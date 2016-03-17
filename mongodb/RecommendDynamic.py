#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId


class RecommendDynamic:
    # 定义旧集合的名字
    collection_old = 'recommendhis'

    # 定义新集合的名字
    collection_new = 'recommend_dynamic'

    # 定义参数字典,其中键为旧集合的字段名,值为新集合的字段名
    # 注意:这里只定义不需要做特殊处理的字段
    params_map = {
        '_id': '_id',
        'city_id': 'city_id'
    }

    def __init__(self):
        pass

    @staticmethod
    def convert_recommend_dynamic(address_old, port_old, address_new, port_new, collection_old, collection_new,
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

            content = None
            recommend_start_time = None
            recommend_start_date = None
            recommend_end_time = None
            recommend_end_date = None
            recommend_poi_lat = None
            recommend_poi_lon = None
            recommend_content = None

            if 'content' in document:
                print(content)
                content = document['content']
                for i in range(len(content)):
                    if content[i].has_key('recommend_start_time'):
                        recommend_start_time = content[i]['recommend_start_time']
                    if content[i].has_key('recommend_start_date'):
                        recommend_start_date = content[i]['recommend_start_date']
                    if content[i].has_key('recommend_start_time'):
                        recommend_end_time = content[i]['recommend_end_time']
                    if content[i].has_key('recommend_end_time'):
                        recommend_end_date = content[i]['recommend_end_date']
                    if content[i].has_key('recommend_poi_lat'):
                        recommend_poi_lat = content[i]['recommend_poi_lat']
                    if content[i].has_key('recommend_poi_lon'):
                        recommend_poi_lon = content[i]['recommend_poi_lon']
                    if content[i].has_key('recommend_content'):
                        recommend_content = content[i]['recommend_content']

            other.update({'content': {'recommend_start_time': recommend_start_time,
                                      'recommend_start_date': recommend_start_date,
                                      'recommend_end_time': recommend_end_time,
                                      'recommend_end_date': recommend_end_date,
                                      'recommend_poi_lat': recommend_poi_lat,
                                      'recommend_poi_lon': recommend_poi_lon,
                                      'recommend_content': recommend_content}})

            post = {}
            post.update(other)
            for i in range(len(params_map.keys())):
                post.update({params_map.values()[i]: temp[i]})
            db_new.insert(post)
            print post

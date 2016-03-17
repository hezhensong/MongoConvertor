#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient


class WeatherHistory:
    # 定义旧集合的名字
    collection_old = 'weather'

    # 定义新集合的名字
    collection_new = 'weather_history'

    # 定义参数字典,其中键为旧集合的字段名,值为新集合的字段名
    # 注意:这里只定义不需要做特殊处理的字段
    params_map = {
        'city_id': 'city_id',
        'timestamp': 'timestamp'
    }

    def __init__(self):
        pass

    @staticmethod
    def create_weather_history(address_old, port_old, address_new, port_new, collection_old, collection_new,
                               params_map):

        # old database connection
        client = MongoClient(address_old, port_old)
        travel1 = client.travel2

        # new database connection
        client = MongoClient(address_new, port_new)
        travel2 = client.travel2

        # get old collection and create new collection
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
            condition = None
            update_time = None
            description = None
            sunrise = None
            sunset = None
            low = None
            high = None
            temperature = None

            if 'condition' in document:
                condition = document['condition']
                print(condition)
                if 'update_time' in condition:
                    update_time = condition['update_time']
                if 'description' in condition:
                    description = condition['description']
                if 'sunrise' in condition:
                    sunrise = condition['sunrise']
                if 'sunset' in condition:
                    sunset = condition['sunset']
                if 'low' in condition:
                    low = int(condition['low'])
                if 'high' in condition:
                    high = int(condition['high'])
                if 'temperature' in condition:
                    temperature = condition['temperature']

                other.update({'update_time': update_time, 'description': description, 'temperature': temperature,
                              'sunrise': sunrise, 'sunset': sunset, 'low': low, 'high': high})
            post = {}
            post.update(other)
            for i in range(len(params_map.keys())):
                post.update({params_map.values()[i]: temp[i]})
            db_new.insert(post)
            print post

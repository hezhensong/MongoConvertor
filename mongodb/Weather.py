#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import time
import datetime
from bson.objectid import ObjectId
from pymongo import MongoClient


class Weather:
    collection_old = 'weathers'

    collection_new = 'weather'

    params_map = {'_id': '_id',  # 天气 ID
                  'city_id': 'city_id',  # 城市 ID
                  }

    def __init__(self):
        pass

    @staticmethod
    def convert_weather(address_old, port_old, address_new, port_new, collection_old, collection_new,
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
            yahoo_weather = None
            description = None
            temperature = None
            high = None
            low = None
            sunrise = None
            sunset = None
            update_time = None
            timestamp = None
            other = {}
            
            if 'timestamp' in document:
                temp_timestamp = document['timestamp']
                array_timestamp = time.localtime(float(temp_timestamp) / 1000)
                y,m,d,h,mm,s = array_timestamp[0:6]
                timestamp = datetime.datetime(y,m,d,h,mm,s)
            
            if 'yahooWeather' in document:
                print(document['_id'])
                yahoo_weather = document['yahooWeather']

                if document['_id'] == ObjectId('5602ae56da00caf21d010410') or document['_id'] == ObjectId(
                        '5602ba7e6c529a1d1f19efa2'):
                    jsonStr = yahoo_weather
                else:
                    jsonStr = json.loads(yahoo_weather)

                dic = jsonStr['query']['results']['channel']
                description = dic['item']['condition']['text']
                temperature = dic['item']['condition']['temp']
                sunrise = dic['astronomy']['sunrise']
                sunset = dic['astronomy']['sunset']
                
                update_time = dic['lastBuildDate']
                temp_update = update_time[0:21]
                array_update = time.strptime(temp_update, "%a, %d %b %Y %H:%M")
                y,m,d,h,mm,s = array_update[0:6]
                update_time = datetime.datetime(y,m,d,h,mm,s)

                forecast = []
                forecastTemp = dic['item']['forecast']
                for i in range(len(forecastTemp)):
                    forecastDetail = {}
                    temp_date = time.strptime(forecastTemp[i]['date'], "%d %b %Y")
                    year, month, day = temp_date[0:3]
                    forecastDetail.update({'date': datetime.datetime(year, month, day)})
                    forecastDetail.update({'description': forecastTemp[i]['text']})
                    forecastDetail.update({'high': int(forecastTemp[i]['high'])})
                    forecastDetail.update({'low': int(forecastTemp[i]['low'])})
                    forecast.append(forecastDetail)

                other.update({'date': timestamp,'condition': 
                                            {'description': description, 'temperature': int(temperature),
                                             'high': int(forecastTemp[0]['high']), 'low': int(forecastTemp[0]['low']),
                                             'sunrise': sunrise, 'sunset': sunset,
                                             'update_time': update_time}, 'forecast': forecast})

            post = {}
            post.update(other)
            for i in range(len(params_map.keys())):
                post.update({params_map.values()[i]: temp[i]})
            db_new.insert(post)
            print post

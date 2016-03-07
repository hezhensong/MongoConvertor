#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient


class Weather:
    def __init__(self):
        pass

    @staticmethod
    def convert_weather(address_old, port_old, address_new, port_new):
        # old database connection
        client = MongoClient(address_old, port_old)
        travel1 = client.travel1

        # new database connection
        client = MongoClient(address_new, port_new)
        travel2 = client.travel2

        # old collection latest city
        weather = travel1.weathers
        weather_new = travel2.weather

        # clean former data
        weather_new.remove()

        for weather_old in weather.find():
            _id = weather_old['_id']
            city_id = weather_old['city_id']
            timestamp = weather_old['timestamp']
            yahoo_weather = weather_old['yahooWeather']

            post = {
                '_id': _id,  # 天气ID
                'city_id': city_id,  # 城市ID
                'timestamp': timestamp,  # 更新时间
                'yahoo_weather': yahoo_weather  # Yahoo天气详情
            }
            weather_new.insert(post)

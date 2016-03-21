#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient


class WeatherTranslation:
    def __init__(self):
        pass

    @staticmethod
    def insert_weather_translation(address_new, port_new):
        # new database connection
        client = MongoClient(address_new, port_new)
        travel2 = client.travel2

        # get old collection and create new collection
        weather_translation = travel2.weather_translation

        # clean former data
        weather_translation.remove()

        post = {"English": "Sunny", "Chinese": "晴"}
        weather_translation.insert(post)

        post = {"English": "Clear", "Chinese": "晴"}
        weather_translation.insert(post)

        post = {"English": "Fair", "Chinese": "晴"}
        weather_translation.insert(post)

        post = {"English": "Fair", "Chinese": "晴"}
        weather_translation.insert(post)

        post = {"English": "Cloudy", "Chinese": "多云"}
        weather_translation.insert(post)

        post = {"English": "Partly Cloudy", "Chinese": "晴间多云"}
        weather_translation.insert(post)

        post = {"English": "Partly Cloudy", "Chinese": "晴间多云"}
        weather_translation.insert(post)

        post = {"English": "Mostly Cloudy", "Chinese": "大部多云"}
        weather_translation.insert(post)

        post = {"English": "Mostly Cloudy", "Chinese": "大部多云"}
        weather_translation.insert(post)

        post = {"English": "Overcast", "Chinese": "阴"}
        weather_translation.insert(post)

        post = {"English": "Shower", "Chinese": "阵雨"}
        weather_translation.insert(post)

        post = {"English": "Thundershower", "Chinese": "雷阵雨"}
        weather_translation.insert(post)

        post = {"English": "Thundershower with Hail", "Chinese": "雷阵雨伴有冰雹"}
        weather_translation.insert(post)

        post = {"English": "Light Rain", "Chinese": "小雨"}
        weather_translation.insert(post)

        post = {"English": "Moderate Rain", "Chinese": "中雨"}
        weather_translation.insert(post)

        post = {"English": "Heavy Rain", "Chinese": "大雨"}
        weather_translation.insert(post)

        post = {"English": "Storm", "Chinese": "暴雨"}
        weather_translation.insert(post)

        post = {"English": "Heavy Storm", "Chinese": "大暴雨"}
        weather_translation.insert(post)

        post = {"English": "Severe Storm", "Chinese": "特大暴雨"}
        weather_translation.insert(post)

        post = {"English": "Ice Rain", "Chinese": "冻雨"}
        weather_translation.insert(post)

        post = {"English": "Sleet", "Chinese": "雨夹雪"}
        weather_translation.insert(post)

        post = {"English": "Snow Flurry", "Chinese": "阵雪"}
        weather_translation.insert(post)

        post = {"English": "Light Snow", "Chinese": "小雪"}
        weather_translation.insert(post)

        post = {"English": "Moderate Snow", "Chinese": "中雪"}
        weather_translation.insert(post)

        post = {"English": "Heavy Snow", "Chinese": "大雪"}
        weather_translation.insert(post)

        post = {"English": "Snowstorm", "Chinese": "暴雪"}
        weather_translation.insert(post)

        post = {"English": "Dust", "Chinese": "浮尘"}
        weather_translation.insert(post)

        post = {"English": "Sand", "Chinese": "扬沙"}
        weather_translation.insert(post)

        post = {"English": "Duststorm", "Chinese": "沙尘暴"}
        weather_translation.insert(post)

        post = {"English": "Sandstorm", "Chinese": "强沙尘暴"}
        weather_translation.insert(post)

        post = {"English": "Foggy", "Chinese": "雾"}
        weather_translation.insert(post)

        post = {"English": "Haze", "Chinese": "霾"}
        weather_translation.insert(post)

        post = {"English": "Windy", "Chinese": "风"}
        weather_translation.insert(post)

        post = {"English": "Blustery", "Chinese": "大风"}
        weather_translation.insert(post)

        post = {"English": "Hurricane", "Chinese": "飓风"}
        weather_translation.insert(post)

        post = {"English": "Tropical Storm", "Chinese": "热带风暴"}
        weather_translation.insert(post)

        post = {"English": "Tornado", "Chinese": "龙卷风"}
        weather_translation.insert(post)

        post = {"English": "Cold", "Chinese": "冷"}
        weather_translation.insert(post)

        post = {"English": "Hot", "Chinese": "热"}
        weather_translation.insert(post)

        post = {"English": "Unknown", "Chinese": "未知"}
        weather_translation.insert(post)

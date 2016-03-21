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

        post = {"english": "Sunny", "chinese": "晴"}
        weather_translation.insert(post)

        post = {"english": "Clear", "chinese": "晴"}
        weather_translation.insert(post)

        post = {"english": "Fair", "chinese": "晴"}
        weather_translation.insert(post)

        post = {"english": "Fair", "chinese": "晴"}
        weather_translation.insert(post)

        post = {"english": "Cloudy", "chinese": "多云"}
        weather_translation.insert(post)

        post = {"english": "Partly Cloudy", "chinese": "晴间多云"}
        weather_translation.insert(post)

        post = {"english": "Partly Cloudy", "chinese": "晴间多云"}
        weather_translation.insert(post)

        post = {"english": "Mostly Cloudy", "chinese": "大部多云"}
        weather_translation.insert(post)

        post = {"english": "Mostly Cloudy", "chinese": "大部多云"}
        weather_translation.insert(post)

        post = {"english": "Overcast", "chinese": "阴"}
        weather_translation.insert(post)

        post = {"english": "Shower", "chinese": "阵雨"}
        weather_translation.insert(post)

        post = {"english": "Thundershower", "chinese": "雷阵雨"}
        weather_translation.insert(post)

        post = {"english": "Thundershower with Hail", "chinese": "雷阵雨伴有冰雹"}
        weather_translation.insert(post)

        post = {"english": "Light Rain", "chinese": "小雨"}
        weather_translation.insert(post)

        post = {"english": "Moderate Rain", "chinese": "中雨"}
        weather_translation.insert(post)

        post = {"english": "Heavy Rain", "chinese": "大雨"}
        weather_translation.insert(post)

        post = {"english": "Storm", "chinese": "暴雨"}
        weather_translation.insert(post)

        post = {"english": "Heavy Storm", "chinese": "大暴雨"}
        weather_translation.insert(post)

        post = {"english": "Severe Storm", "chinese": "特大暴雨"}
        weather_translation.insert(post)

        post = {"english": "Ice Rain", "chinese": "冻雨"}
        weather_translation.insert(post)

        post = {"english": "Sleet", "chinese": "雨夹雪"}
        weather_translation.insert(post)

        post = {"english": "Snow Flurry", "chinese": "阵雪"}
        weather_translation.insert(post)

        post = {"english": "Light Snow", "chinese": "小雪"}
        weather_translation.insert(post)

        post = {"english": "Moderate Snow", "chinese": "中雪"}
        weather_translation.insert(post)

        post = {"english": "Heavy Snow", "chinese": "大雪"}
        weather_translation.insert(post)

        post = {"english": "Snowstorm", "chinese": "暴雪"}
        weather_translation.insert(post)

        post = {"english": "Dust", "chinese": "浮尘"}
        weather_translation.insert(post)

        post = {"english": "Sand", "chinese": "扬沙"}
        weather_translation.insert(post)

        post = {"english": "Duststorm", "chinese": "沙尘暴"}
        weather_translation.insert(post)

        post = {"english": "Sandstorm", "chinese": "强沙尘暴"}
        weather_translation.insert(post)

        post = {"english": "Foggy", "chinese": "雾"}
        weather_translation.insert(post)

        post = {"english": "Haze", "chinese": "霾"}
        weather_translation.insert(post)

        post = {"english": "Windy", "chinese": "风"}
        weather_translation.insert(post)

        post = {"english": "Blustery", "chinese": "大风"}
        weather_translation.insert(post)

        post = {"english": "Hurricane", "chinese": "飓风"}
        weather_translation.insert(post)

        post = {"english": "Tropical Storm", "chinese": "热带风暴"}
        weather_translation.insert(post)

        post = {"english": "Tornado", "chinese": "龙卷风"}
        weather_translation.insert(post)

        post = {"english": "Cold", "chinese": "冷"}
        weather_translation.insert(post)

        post = {"english": "Hot", "chinese": "热"}
        weather_translation.insert(post)

        post = {"english": "Unknown", "chinese": "未知"}
        weather_translation.insert(post)

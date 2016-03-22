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

        weather_translation.insert({"english": "tornado", "chinese": "龙卷风"})
        weather_translation.insert({"english": "tropical storm", "chinese": "热带风暴"})
        weather_translation.insert({"english": "hurricane", "chinese": "飓风"})
        weather_translation.insert({"english": "severe thunderstorms", "chinese": "强雷暴"})
        weather_translation.insert({"english": "thunderstorms", "chinese": "雷暴"})
        weather_translation.insert({"english": "pm thunderstorms", "chinese": "雷暴"})
        weather_translation.insert({"english": "mixed rain and snow", "chinese": "雨夹雪"})
        weather_translation.insert({"english": "mixed rain and sleet", "chinese": "雨夹雪"})
        weather_translation.insert({"english": "mixed snow and sleet", "chinese": "雨夹雪"})
        weather_translation.insert({"english": "freezing drizzle", "chinese": "小雨"})
        weather_translation.insert({"english": "drizzle", "chinese": "小雨"})
        weather_translation.insert({"english": "freezing rain", "chinese": "雨夹冰雹"})
        weather_translation.insert({"english": "showers", "chinese": "阵雨"})
        weather_translation.insert({"english": "pm showers", "chinese": "阵雨"})
        weather_translation.insert({"english": "snow flurries", "chinese": "阵雪"})
        weather_translation.insert({"english": "light snow showers", "chinese": "局部小雪"})
        weather_translation.insert({"english": "blowing snow", "chinese": "飘雪"})
        weather_translation.insert({"english": "snow", "chinese": "雪"})
        weather_translation.insert({"english": "hail", "chinese": "冰雹"})
        weather_translation.insert({"english": "sleet", "chinese": "雨夹雪"})
        weather_translation.insert({"english": "dust", "chinese": "灰尘"})
        weather_translation.insert({"english": "foggy", "chinese": "雾霾"})
        weather_translation.insert({"english": "haze", "chinese": "薄雾"})
        weather_translation.insert({"english": "smoky", "chinese": "烟尘"})
        weather_translation.insert({"english": "blustery", "chinese": "大风"})
        weather_translation.insert({"english": "windy", "chinese": "有风"})
        weather_translation.insert({"english": "cold", "chinese": "冷"})
        weather_translation.insert({"english": "cloudy", "chinese": "多云"})
        weather_translation.insert({"english": "mostly cloudy", "chinese": "晴转多云"})
        weather_translation.insert({"english": "mostly cloudy (night)", "chinese": "晴转多云"})
        weather_translation.insert({"english": "mostly cloudy (day)", "chinese": "晴转多云"})
        weather_translation.insert({"english": "partly cloudy", "chinese": "晴转多云"})
        weather_translation.insert({"english": "partly cloudy (night)", "chinese": "晴转多云"})
        weather_translation.insert({"english": "partly cloudy (day)", "chinese": "晴转多云"})
        weather_translation.insert({"english": "clear", "chinese": "晴"})
        weather_translation.insert({"english": "clear (night)", "chinese": "晴"})
        weather_translation.insert({"english": "sunny", "chinese": "阳光明媚"})
        weather_translation.insert({"english": "mostly sunny", "chinese": "阳光明媚"})
        weather_translation.insert({"english": "fair", "chinese": "晴"})
        weather_translation.insert({"english": "fair (night)", "chinese": "晴"})
        weather_translation.insert({"english": "fair (day)", "chinese": "晴"})
        weather_translation.insert({"english": "mixed rain and hail", "chinese": "雨夹冰雹"})
        weather_translation.insert({"english": "hot", "chinese": "晴"})
        weather_translation.insert({"english": "isolated thunderstorms", "chinese": "局部雷暴"})
        weather_translation.insert({"english": "scattered thunderstorms", "chinese": "局部雷雨"})
        weather_translation.insert({"english": "scattered thunderstorms", "chinese": "局部雷雨"})
        weather_translation.insert({"english": "scattered showers", "chinese": "局部阵雨"})
        weather_translation.insert({"english": "heavy snow", "chinese": "大雪"})
        weather_translation.insert({"english": "scattered snow showers", "chinese": "局部阵雪"})
        weather_translation.insert({"english": "heavy snow", "chinese": "大雪"})
        weather_translation.insert({"english": "partly cloudy", "chinese": "晴转多云"})
        weather_translation.insert({"english": "thundershowers", "chinese": "雷阵雨"})
        weather_translation.insert({"english": "snow showers", "chinese": "阵雪"})
        weather_translation.insert({"english": "isolated thundershowers", "chinese": "局部雷雨"})
        weather_translation.insert({"english": "not available", "chinese": "无效"})

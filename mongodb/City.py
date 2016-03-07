#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient


class City:
    def __init__(self):
        pass

    @staticmethod
    def convert_city(address_old, port_old, address_new, port_new):
        # old database connection
        client = MongoClient(address_old, port_old)
        travel1 = client.travel1

        # new database connection
        client = MongoClient(address_new, port_new)
        travel2 = client.travel2

        # old collection latest city
        latest_city = travel1.latestcity
        city_new = travel2.city

        # clean former data
        city_new.remove()

        for city_old in latest_city.find():
            _id = city_old['_id']
            city_name = city_old['cityname']
            city_name_en = city_old['cityname_en']
            city_name_py = city_old['cityname_py']

            show_flag = city_old['show_flag']
            if show_flag == u'1':
                is_show = True
            else:
                is_show = False

            post = {
                '_id': _id,  # 城市ID
                'city_name': city_name,  # 城市中文名
                'city_name_en': city_name_en,  # 城市英文名
                'city_name_py': city_name_py,  # 城市中文名拼音
                'is_show': is_show  # 是否线上展示
            }
            city_new.insert(post)

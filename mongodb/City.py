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

        for cityOld in latest_city.find({'cityname_en': 'New York'}):
            _id = cityOld['_id']
            city_name = cityOld['cityname']
            city_name_en = cityOld['cityname_en']
            # city_name_py = cityOld['cityname_py']

            show_flag = cityOld['show_flag']
            if show_flag == u'1':
                is_show = True
            else:
                is_show = False

            post = {
                '_id': _id,  # 城市ID
                'city_name': city_name,  # 城市中文名
                'city_name_en': city_name_en,  # 城市英文名
                'is_show': is_show  # 是否线上展示
            }
            city_new.insert(post)

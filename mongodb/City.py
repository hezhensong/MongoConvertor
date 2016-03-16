#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId


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
            continent_code = city_old['continentscode']

            if 'coverImageName' in city_old:
                city_cover_image = city_old['coverImageName']
            else:
                city_cover_image = None

            # 主题ID list
            label = travel2.label
            label_dict = {}
            if 'attrlabels' in city_old:
                label_list_old = city_old['attrlabels']

                if len(label_list_old) > 0:
                    for label_old in label_list_old:
                        label_id = ObjectId(label_old['_id'])
                        if label_id != u'{{_id}}':
                            label_temp = label.find_one({"_id": label_id})
                            name = label_temp['name']

                            if str(label_temp['type']) in label_dict.keys():
                                label_dict[str(label_temp['type'])].append({"_id": label_id, "name": name})
                            else:
                                label_dict[str(label_temp['type'])] = [{"_id": label_id, "name": name}]

            area = {
                'continent': city_old['continents'],
                'country': city_old['countryname']
            }

            # 是否线上展示
            show_flag = city_old['show_flag']
            if show_flag == u'1':
                is_show = True
            else:
                is_show = False

            post = {
                '_id': _id,  # 城市ID
                'name': city_name,  # 城市中文名
                'name_en': city_name_en,  # 城市英文名
                'name_py': city_name_py,  # 城市中文名拼音
                'continent_code': continent_code,  # 城市所在大洲
                'cover_image': city_cover_image,  # 城市首页背景图片
                'label_list': label_dict,  # 主题ID列表
                'area': area,
                'is_show': is_show  # 是否线上展示
            }
            city_new.insert(post)
            print(post)

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId

timezoneMap = {
                   ObjectId('516a34f958e3511036000001'):'GMT-5:00',    # 纽约
                   ObjectId('516a34f958e3511036000002'):'GMT-8:00',    # 旧金山  
                   ObjectId('516a34f958e3511036000003'):'GMT-8:00',    # 洛杉矶
                   ObjectId('516a34fa58e3511036000004'):'GMT-6:00',    # 芝加哥
                   ObjectId('516a34fa58e3511036000005'):'GMT-5:00',    # 波士顿   
                   '516a350ec221c21236000001':'GMT-8:00',    # 温哥华
                   '516a350ec221c21236000002':'GMT-5:00',    # 多伦多
                   '516a350ec221c21236000003':'GMT+1:00',       # 巴黎
                   '516a350ec221c21236000004':'GMT+1:00',          # 里昂
                   '516a350fc221c21236000005':'GMT+1:00',          # 尼斯 
                   '516a3519f8a6461636000001':'GMT+1:00',          # 威尼斯
                   '516a3519f8a6461636000002':'GMT+1:00',      # 马德里
                   '516a3519f8a6461636000003':'GMT+1:00',          # 巴萨罗那
                   '516a3519f8a6461636000004':'Europe/Berlin',      # 柏林
                   '516a3519f8a6461636000005':'GMT+1:00',          # 法兰克福
                   '516a35208902ca1936000001':'GMT+1:00',          # 慕尼黑
                   '516a35218902ca1936000002':'Europe/Zurich',      # 苏黎世
                   '516a35218902ca1936000003':'GMT+1:00',          # 日内瓦
                   '516a35218902ca1936000004':'Europe/Amsterdam',   # 阿姆斯特丹
                   '516a35218902ca1936000005':'Europe/London',      # 伦敦
                   '516a352b625d8b1e36000001':'GMT+0:00',          # 曼彻斯特
                   '516a352b625d8b1e36000003':'GMT+9:00',          # 大阪
                   '516a352b625d8b1e36000005':'Asia/Seoul',         # 首尔（测试）
                   '516a3534dac6182136000001':'GMT+9:00',          # 釜山
                   '516a3535dac6182136000002':'Asia/Bangkok',       # 曼谷
                   '516a3535dac6182136000003':'GMT+7:00',          # 普吉岛
                   '516a3535dac6182136000004':'Asia/Singapore',     # 新加坡  
                   '516a3535dac6182136000005':'Asia/Kuala_Lumpur',  # 吉隆坡
                   '516a35427dbbf72336000002':'GMT+8:00',          # 马尼拉
                   '516a35427dbbf72336000003':'GMT+8:00',          # 长滩岛
                   '51d3d238e98bbb566a000001':'Europe/Rome',        # 罗马 
                   '52e0f1efb64f047135000003':'Australia/Sydney',   # 悉尼
                   '52e62f8e4e59f08771000009':'GMT-10:00',         # 欧胡岛
                   '530735c6d05b06507f000056':'GMT+9:00',          # 济州特别自治道
                   '53074df8d05b06507f00005e':'Asia/Dubai',         # 迪拜
                   '53077a0ed05b06507f000077':'America/Argentina/Buenos_Aires',  # 布宜诺斯艾利斯
                   '5307cf87d05b06507f000090':'Asia/Tel_Aviv',      # 特拉维夫
                   '5308cb32d05b06507f00009b':'America/Santiago',   # 圣地亚哥 
                   '5308d35dd05b06507f0000a5':'GMT+2:00',          # 圣托里尼岛
                   '53845d836b36839c04000007':'GMT+8:00',          # 巴厘岛
                   '565fa92d18a1bf1a2b000046':'Hongkong',           # 香港
                   '565fa9cd18a1bf1a2b000048':'Asia/Macau',         # 澳门（测试）
                   '5698ae4730e3611971000024':'Asia/Seoul',         # 首尔
                   '5698bec74fb72baf67000001':'Asia/Macau',         # 澳门
                   '569c86a02fedc1e719000194':'Asia/Taipei',        # 台北
                   '569c8d062fedc1e7190001ad':'Asia/Tokyo',         # 东京
                   '569c95852fedc1e7190001ea':'GMT+9:00',          # 京都
        }


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

            if 'imgforapp' in city_old:
                city_cover_image = "http://weegotest.b0.upaiyun.com/city/citypathforApp/" + city_old['imgforapp']
            else:
                city_cover_image = None

            # 景点 list
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

            # 餐厅 list
            label_dict['1'] = []
            label_list = label_dict['1']
            if city_name == u"旧金山":
                label_list.append({"_id": ObjectId("000000000000"), "name": "惬意时光"})
                label_list.append({"_id": ObjectId("000000000000"), "name": "国际风味"})
                label_list.append({"_id": ObjectId("000000000000"), "name": "人气中餐"})
                label_list.append({"_id": ObjectId("000000000000"), "name": "本地独家"})
            else:
                label_list.append({"_id": ObjectId("000000000000"), "name": "米其林推荐"})
                label_list.append({"_id": ObjectId("000000000000"), "name": "本地特色"})
                label_list.append({"_id": ObjectId("000000000000"), "name": "人气热门"})
                label_list.append({"_id": ObjectId("000000000000"), "name": "城市精选"})

            # 购物 list
            label_dict['2'] = []
            label_list = label_dict['2']
            label_list.append({"_id": ObjectId("000000000000"), "name": "购物商圈"})
            label_list.append({"_id": ObjectId("000000000000"), "name": "商圈"})

            if city_old['continents'] == u'美洲':
                city_old['continents'] = u'北美'

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
                'cover_image': city_cover_image,  # 城市首页背景图片
                'label_list': label_dict,  # label列表
                'area': area,
                'is_show': is_show  # 是否线上展示
            }
            city_new.insert(post)
            print(post)

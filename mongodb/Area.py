#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient


class Area:
    def __init__(self):
        pass

    @staticmethod
    def insert_area(address_old, port_old, address_new, port_new):
        # old database connection
        client = MongoClient(address_old, port_old)
        travel1 = client.travel1

        # new database connection
        client = MongoClient(address_new, port_new)
        travel2 = client.travel2

        # old collection latest city
        latest_city = travel1.latestcity
        area = travel2.area

        # clean former data
        area.remove()

        # 七大洲
        post = {
            'name': u'亚洲',  # 行政区中文名
            'name_en': u'Asia',  # 行政区英文名
            'name_py': u'yazhou',  # 拼音
            'aliases': [],  # 别名
            'code': u'AS',  # 行政区代码
            'type': u'continent',  # 行政区类型
            'path': u'亚洲',  # 树状行政区划
            'order': 1  # 排序
        }
        area.insert(post)
        print(post)

        post = {
            'name': u'欧洲',
            'name_en': u"Europe",
            'name_py': u'ouzhou',
            'aliases': [],
            'code': u'EU',
            'type': u'continent',
            'path': u'欧洲',
            'order': 3
        }
        area.insert(post)
        print(post)

        post = {
            'name': u'北美',
            'name_en': u'North America',
            'name_py': u'beimeizhou',
            'aliases': [],
            'code': u'NA',
            'type': u'continent',
            'path': u'北美',
            'order': 2
        }
        area.insert(post)
        print(post)

        post = {
            'name': u'南美',
            'name_en': u'South America',
            'name_py': u'nanmeizhou',
            'aliases': [],
            'code': u'SA',
            'type': u'continent',
            'path': u'南美',
            'order': 4
        }
        area.insert(post)
        print(post)

        post = {
            'name': u'大洋洲',
            'name_en': u'Oceania',
            'name_py': u'dayangzhou',
            'aliases': [],
            'code': u'OA',
            'type': u'continent',
            'path': u'大洋洲',
            'order': 5
        }
        area.insert(post)
        print(post)

        post = {
            'name': u'非洲',
            'name_en': u'Africa',
            'name_py': u'feizhou',
            'aliases': [],
            'code': u'AF',
            'type': u'continent',
            'path': u'非洲',
            'order': 6
        }
        area.insert(post)
        print(post)

        post = {
            'name': u'南极洲',
            'name_en': u'Antarctica',
            'name_py': u'nanjizhou',
            'aliases': [],
            'code': u'AN',
            'type': u'continent',
            'path': u'南极洲',
            'order': 7
        }
        area.insert(post)
        print(post)

        # 北美洲国家
        # post = {
        #     'name': u'美国',
        #     'name_en': u'United States',
        #     'name_py': u'meiguo',
        #     'aliases': [],
        #     'code': u'USA',
        #     'type': u'country',
        #     'path': u'北美.美国'
        # }
        # area.insert(post)
        # print(post)

        # 南美洲国家



        # 欧洲国家

        # 非洲国家

        # 大洋洲国家

        # 南极洲国家

        # 亚洲国家
        # post = {
        #     'name': u'中国',
        #     'name_en': u'China',
        #     'name_py': u'zhongguo',
        #     'aliases': [],
        #     'code': u'CHN',
        #     'type': u'country',
        #     'path': u'亚洲.中国'
        # }
        # area.insert(post)
        # print(post)
        #
        # post = {
        #     'name': u'日本',
        #     'name_en': u'Japan',
        #     'name_py': u'riben',
        #     'aliases': [],
        #     'code': u'JPN',
        #     'type': u'country',
        #     'path': u'亚洲.日本'
        # }
        # area.insert(post)
        # print(post)
        #
        # post = {
        #     'name': u'韩国',
        #     'name_en': u'Korea',
        #     'name_py': u'hanguo',
        #     'aliases': [],
        #     'code': u'KOR',
        #     'type': u'country',
        #     'path': u'亚洲.韩国'
        # }
        # area.insert(post)
        # print(post)
        #
        # post = {
        #     'name': u'泰国',
        #     'name_en': u'Thailand',
        #     'name_py': u'taiguo',
        #     'aliases': [],
        #     'code': u'THA',
        #     'type': u'country',
        #     'path': u'亚洲.泰国'
        # }
        # area.insert(post)
        # print(post)
        #
        # post = {
        #     'name': u'新加坡',
        #     'name_en': u'Singapore',
        #     'name_py': u'xinjiapo',
        #     'aliases': [],
        #     'code': u'SGP',
        #     'type': u'country',
        #     'path': u'亚洲.新加坡'
        # }
        # area.insert(post)
        # print(post)
        #
        # post = {
        #     'name': u'马来西亚',
        #     'name_en': u'Malaysia',
        #     'name_py': u'malaixiya',
        #     'aliases': [],
        #     'code': u'MYS',
        #     'type': u'country',
        #     'path': u'亚洲.马来西亚'
        # }
        # area.insert(post)
        # print(post)
        #
        # post = {
        #     'name': u'菲律宾',
        #     'name_en': u'Pilipinas',
        #     'name_py': u'feilvbin',
        #     'aliases': [],
        #     'code': u'PHL',
        #     'type': u'country',
        #     'path': u'亚洲.菲律宾'
        # }
        # area.insert(post)
        # print(post)
        #
        # post = {
        #     'name': u'阿拉伯联合酋长国',
        #     'name_en': u'United Arab Emtrates',
        #     'name_py': u'alabolianheqiuzhangguo',
        #     'aliases': [],
        #     'code': u'ARE',
        #     'type': u'country',
        #     'path': u'亚洲.阿拉伯联合酋长国'
        # }
        # area.insert(post)
        # print(post)
        #
        # post = {
        #     'name': u'以色列',
        #     'name_en': u'Israel',
        #     'name_py': u'yiselie',
        #     'aliases': [],
        #     'code': u'ISR',
        #     'type': u'country',
        #     'path': u'亚洲.以色列'
        # }
        # area.insert(post)
        # print(post)
        #
        # post = {
        #     'name': u'印度尼西亞',
        #     'name_en': u'Indonesia',
        #     'name_py': u'yindunixiya',
        #     'aliases': [],
        #     'code': u'IDN',
        #     'type': u'country',
        #     'path': u'亚洲.印度尼西亞'
        # }
        # area.insert(post)
        # print(post)

        # 亚洲城市
        order = 01
        for city in latest_city.find({"continents": "亚洲"}):
            post_city = {
                '_id': city['_id'],
                'name': city['cityname'],
                'name_en': city['cityname_en'],
                'name_py': city['cityname_py'],
                'aliases': [],
                'code': u'',
                'type': u'city',
                'path': u'亚洲.' + city['countryname'] + '.' + city['cityname'],
                'order': 100 + order
            }
            area.insert(post_city)
            print(post_city)
            order += 1

        # 欧洲城市
        order = 01
        for city in latest_city.find({"continents": "欧洲"}):
            post_city = {
                '_id': city['_id'],
                'name': city['cityname'],
                'name_en': city['cityname_en'],
                'name_py': city['cityname_py'],
                'aliases': [],
                'code': u'',
                'type': u'city',
                'path': u'欧洲.' + city['countryname'] + '.' + city['cityname'],
                'order': 300 + order
            }
            area.insert(post_city)
            print(post_city)
            order += 1

        # 北美洲城市
        order = 01
        for city in latest_city.find({"continents": "美洲"}):
            post_city = {
                '_id': city['_id'],
                'name': city['cityname'],
                'name_en': city['cityname_en'],
                'name_py': city['cityname_py'],
                'aliases': [],
                'code': u'',
                'type': u'city',
                'path': u'北美.' + city['countryname'] + '.' + city['cityname'],
                'order': 200 + order
            }
            area.insert(post_city)
            print(post_city)
            order += 1

        # 南美洲城市
        order = 01
        for city in latest_city.find({"continents": "南美"}):
            post_city = {
                '_id': city['_id'],
                'name': city['cityname'],
                'name_en': city['cityname_en'],
                'name_py': city['cityname_py'],
                'aliases': [],
                'code': u'',
                'type': u'city',
                'path': u'南美.' + city['countryname'] + '.' + city['cityname'],
                'order': 400 + order
            }
            area.insert(post_city)
            print(post_city)
            order += 1

        # 大洋洲城市
        order = 01
        for city in latest_city.find({"continents": "大洋洲"}):
            post_city = {
                '_id': city['_id'],
                'name': city['cityname'],
                'name_en': city['cityname_en'],
                'name_py': city['cityname_py'],
                'aliases': [],
                'code': u'',
                'type': u'city',
                'path': u'大洋洲.' + city['countryname'] + '.' + city['cityname'],
                'order': 500 + order
            }
            area.insert(post_city)
            print(post_city)
            order += 1

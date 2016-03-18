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

        post_as_countries = []
        exist_countries = []
        for city in latest_city.find({"continents": "亚洲"}):
            post_city = {
                'id': str(city['_id']),
                'name': city['cityname'],
                'name_en': city['cityname_en'],
                'name_py': city['cityname_py'],
                'type': 'city'
            }

            country_name = city['countryname']
            if country_name not in exist_countries:
                exist_countries.append(country_name)
                post_as_country = {
                    'type': 'country',
                    'name': city['countryname'],
                    'name_en': None,
                    'code': city['countrycode'],
                    'city_list': [post_city]
                }
                post_as_countries.append(post_as_country)

            else:
                post_as_country['city_list'].append(post_city)

        post_as = {
            'type': u'continent',  # 行政区类型
            'name': u"亚洲",  # 行政区中文名
            'name_en': u"Asia",  # 行政区英文名
            'code': u'AS',  # 行政区代码
            'country_list': post_as_countries
        }
        area.insert(post_as)
        print(post_as)

        post_eu_countries = []
        exist_countries = []
        for city in latest_city.find({"continents": "欧洲"}):
            post_city = {
                'id': str(city['_id']),
                'name': city['cityname'],
                'name_en': city['cityname_en'],
                'name_py': city['cityname_py'],
                'type': 'city'
            }

            country_name = city['countryname']
            if country_name not in exist_countries:
                exist_countries.append(country_name)
                post_eu_country = {
                    'type': 'country',
                    'name': city['countryname'],
                    'name_en': None,
                    'code': city['countrycode'],
                    'city_list': [post_city]
                }
                post_eu_countries.append(post_eu_country)

            else:
                post_eu_country['city_list'].append(post_city)

        post_eu = {
            'type': u'continent',
            'name': u'欧洲',
            'name_en': u"Europe",
            'code': u'EU',
            'country_list': post_eu_countries
        }
        area.insert(post_eu)
        print(post_eu)

        post_na_countries = []
        exist_countries = []
        for city in latest_city.find({"continents": "美洲"}):
            post_city = {
                'id': str(city['_id']),
                'name': city['cityname'],
                'name_en': city['cityname_en'],
                'name_py': city['cityname_py'],
                'type': 'city'
            }

            country_name = city['countryname']
            if country_name not in exist_countries:
                exist_countries.append(country_name)
                post_na_country = {
                    'type': 'country',
                    'name': city['countryname'],
                    'name_en': None,
                    'code': city['countrycode'],
                    'city_list': [post_city]
                }
                post_na_countries.append(post_na_country)

            else:
                post_na_country['city_list'].append(post_city)

        post_na = {
            'type': u'continent',
            'name': u'美洲',
            'name_en': u'North America',
            'code': u'NA',
            'country_list': post_na_countries
        }
        area.insert(post_na)
        print(post_na)

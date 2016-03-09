#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId
# from pymongo import ObjectId


class Pgc:
    def __init__(self):
        pass

    @staticmethod
    def convert_pgc(address_old, port_old, address_new, port_new):
        # old database connection
        client = MongoClient(address_old, port_old)
        travel1 = client.travel1

        # new database connection
        client = MongoClient(address_new, port_new)
        travel2 = client.travel2
        # old collection latest activities
        pgcs = travel1.pgcs
        pgcs_new = travel2.pgc

        # clean former data
        pgcs_new.remove()

        for pgc_old in pgcs.find():
            # print(pgc_old)
            _id = pgc_old['_id']
            if 'title' in pgc_old:
                title = pgc_old['title']
            else:
                title = None

            if 'cover_image' in pgc_old:
                cover_image = pgc_old['cover_image']
            else:
                cover_image = None

            if 'pgc_city' in pgc_old:
               city_id=pgc_old['pgc_city']['_id']
               # city_id1 = json.loads(city_id)
               # print(city_id1._id)
               city_id=ObjectId(city_id)
               print(unicode(city_id))


            else:
               city_id=None


            post = {
                '_id': _id,  # 活动ID
                'city_id': city_id,  # 城市ID
                'title': title,  # 活动主题
                'cover_image': cover_image  # 活动封面
            }
            pgcs_new.insert(post)

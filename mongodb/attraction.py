#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId


class Attraction:
    def __init__(self):
        pass

    @staticmethod
    def convert_attraction(address_old, port_old, address_new, port_new):
        # old database connection
        client = MongoClient(address_old, port_old)
        travel1 = client.travel1

        # new database connection
        client = MongoClient(address_new, port_new)
        travel2 = client.travel2

        # old collection latest attraction
        latest_attraction = travel1.latestattractions
        attraction_new = travel2.attraction

        # clean former data
        attraction_new.remove()

        for attraction_old in latest_attraction.find():
            _id = attraction_old['_id']
            # address = attraction_old['address']

            # 是否线上展示
            show_flag = attraction_old['show_flag']
            if show_flag == u'1':
                is_show = True
            else:
                is_show = False

            post = {
                '_id': _id,  # 景点ID
                # 'address': address,  # 景点地址
                'is_show': is_show  # 是否线上展示
            }
            attraction_new.insert(post)

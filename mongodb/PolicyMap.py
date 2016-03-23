#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import datetime

import pytz
from pymongo import MongoClient
from bson.objectid import ObjectId


class PolicyMap:
    def __init__(self):
        pass

    @staticmethod
    def insert_policy_map(address_new, port_new):
        # new database connection
        client = MongoClient(address_new, port_new)
        travel2 = client.travel2

        # old collection latest city
        policy_map = travel2.policy_map

        # clean former data
        policy_map.remove()

        post = {
            "policy_id": ObjectId("56f26273095963c0ac40ceb2"),
            "content_id": ObjectId("566b8391f5cf37195100018e"),
            "first_title": "城市活动",
            "second_title": "你附近有场音乐会即将举行",
            "type": 4,
            "last_modify_time": datetime.datetime(2016, 3, 14, 22, 0, 0, 0, tzinfo=pytz.utc),
            "last_modify_person": "weego"
        }
        policy_map.insert(post)
        print post

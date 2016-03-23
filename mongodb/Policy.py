#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import datetime

import pytz
from pymongo import MongoClient
from bson.objectid import ObjectId


class Policy:
    def __init__(self):
        pass

    @staticmethod
    def insert_policy(address_new, port_new):

        # new database connection
        client = MongoClient(address_new, port_new)
        travel2 = client.travel2

        # old collection latest city
        policy = travel2.policy

        # clean former data
        policy.remove()

        post = {
            "city_id": ObjectId("516a34f958e3511036000001"),
            "start_time": datetime.datetime(2016, 3, 14, 0, 0, 0, 0, tzinfo=pytz.utc),
            "end_time": datetime.datetime(2016, 3, 14, 23, 0, 0, 0, tzinfo=pytz.utc),
            "radius": 20000,
            "type": {
                "attraction": [],
                "restaurant": [],
                "shopping": [],
                "shopping_circle": [],
                "activity": [],
                "pgc": [],
                "news": []
            },
            "status": True,
            "last_modify_time": datetime.datetime(2016, 3, 14, 22, 0, 0, 0, tzinfo=pytz.utc),
            "last_modify_person": "weego"
        }
        policy.insert(post)
        print post


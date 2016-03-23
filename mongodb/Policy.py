#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient


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
            "city_id": "516a34f958e3511036000001",
            "start_time": "2016-03-14T00:00:00Z",
            "end_time": "2016-03-14T23:00:00Z",
            "radius": "20000",
            "type": {
                "attraction": [],
                "restaurant": [],
                "shopping": [],
                "shopping_circle": [],
                "activity": [],
                "pgc": [],
                "news": []
            },
            "status": "0",
            "last_modify_time": "2016-03-14T22:00:00Z",
            "last_modify_person": "weego"
        }
        policy.insert(post)


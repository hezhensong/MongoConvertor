#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import datetime

import pytz
from pymongo import MongoClient
from bson.objectid import ObjectId


class RecommendHistory:
    def __init__(self):
        pass

    @staticmethod
    def insert_recommend_history(address_new, port_new):
        # new database connection
        client = MongoClient(address_new, port_new)
        travel2 = client.travel2

        # old collection latest city
        recommend_history = travel2.recommend_history

        # clean former data
        recommend_history.remove()

        post = {
            "city_id": ObjectId("516a34f958e3511036000001"),
            "user_id": ObjectId("516a34f958e3511036000011"),
            "recommend_time": datetime.datetime(2016, 3, 14, 19, 15, 0, 0, tzinfo=pytz.utc),
            "recommend_content": [
                {
                    "type": 0,
                    "content_id": ObjectId("516cc44ce3c6a60f69000011"),
                    "content_first": "标题1.1",
                    "content_second": "标题2.1"
                },
                {
                    "type": 1,
                    "content_id": ObjectId("5322c08d2fab6f0c1d000002"),
                    "content_first": "标题1.2",
                    "content_second": "标题2.2"
                }
            ]
        }
        recommend_history.insert(post)

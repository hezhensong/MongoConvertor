#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient


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
            "city_id": "516a34f958e3511036000001",
            "user_id": "5361414496",
            "recommend_time": "2016-03-14T19:15:00Z",
            "recommend_content": [
                {
                    "type": 0,
                    "content_id": "516cc44ce3c6a60f69000011"
                },
                {
                    "type": 1,
                    "content_id": "5322c08d2fab6f0c1d000002"
                }
            ]
        }
        recommend_history.insert(post)

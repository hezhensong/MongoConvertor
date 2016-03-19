#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient


class Person:
    def __init__(self):
        pass

    @staticmethod
    def convert_person(address_old, port_old, address_new, port_new):
        client = MongoClient(address_old, port_old)
        travel1 = client.travel1

        # new database connection
        client = MongoClient(address_new, port_new)
        travel2 = client.travel2

        # old collection latest activities
        peoples = travel1.peoples
        peoples_new = travel2.person

        peoples_new.remove()

        for people in peoples.find():
            _id = people['_id']
            if 'head_image' in people:
                head_image = people['head_image']
            else:
                head_image = None

            if 'username' in people:
                username = people['username']
            else:
                username = None

            if 'job_desc' in people:
                job_desc = people['job_desc']
            else:
                job_desc = None

            if 'simple_introduce' in people:
                simple_introduce = people['simple_introduce']
            else:
                simple_introduce = None

            post = {
                '_id': _id,  # 活动ID
                'username': username,
                'job_desc': job_desc,
                'head_image': head_image,
                'simple_introduce': simple_introduce
            }
            peoples_new.insert(post)

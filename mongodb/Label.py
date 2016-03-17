#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient


class Label:
    def __init__(self):
        pass

    @staticmethod
    def convert_label(address_old, port_old, address_new, port_new):
        # old database connection
        client = MongoClient(address_old, port_old)
        travel1 = client.travel1

        # new database connection
        client = MongoClient(address_new, port_new)
        travel2 = client.travel2

        # old collection latest city
        labels_old = travel1.label
        label_new = travel2.label

        # clean former data
        label_new.remove()

        for label_old in labels_old.find():
            _id = label_old['_id']
            title = label_old['label']

            # 标签英文名
            if 'label_en' in label_old:
                title_en = label_old['label_en']
            else:
                title_en = None

            post = {
                '_id': _id,  # 标签ID
                'name': title,  # 标签中文名
                'name_en': title_en,  # 标签英文名
                'type': 0,  # 标签类型
            }
            label_new.insert(post)
            print(post)

        # old collection latest city
        latestcity = travel1.latestcity
        res_label_dict = {}

        for city in latestcity.find():
            if 'reslabels' not in city:
                continue

            for reslabel in city['reslabels']:
                _id = reslabel['_id']
                name = reslabel['title']
                if _id not in res_label_dict.keys():
                    res_label_dict[_id] = True

                    post = {
                        '_id': _id,  # 标签ID
                        'name': name,  # 标签中文名
                        'name_en': None,  # 标签英文名
                        'type': 1,  # 标签类型
                    }
                    label_new.insert(post)
                    print(post)

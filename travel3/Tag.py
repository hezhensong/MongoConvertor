#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient


class Tag:
    def __init__(self):
        pass

    @staticmethod
    def convert_tag(address_old, port_old, address_new, port_new):
        # old database connection
        client = MongoClient(address_old, port_old)
        travel1 = client.travel1

        # new database connection
        client = MongoClient(address_new, port_new)
        travel2 = client.travel2

        # old collection latest city
        categories = travel1.categories

        tag = travel2.tag
        tag.remove()

        for category in categories.find():
            _id = category['_id']
            title = category['name']
            title_en = category['en_name']
            label_type = int(category['type'])

            if label_type == 3:
                label_type = 2

            post = {
                '_id': _id,  # 标签ID
                'name': title,  # 标签中文名
                'name_en': title_en,  # 标签英文名
                'type': label_type,  # 标签类型
            }
            tag.insert(post)
            print(post)

        # type 0
        labels_old = travel1.label
        label_new = travel2.tag

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

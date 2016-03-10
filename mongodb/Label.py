#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId


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

        # 转换父级标签
        relation = {}
        for label_old in labels_old.find():
            _id = label_old['_id']

            if label_old['subLabel'] is not None and len(label_old['subLabel']) > 0:
                for label_child in label_old['subLabel']:
                    relation[ObjectId(label_child)] = _id

        for label_old in labels_old.find():
            _id = label_old['_id']
            title = label_old['label']

            # 标签英文名
            if 'label_en' in label_old:
                title_en = label_old['label_en']
            else:
                title_en = None

            level = int(label_old['level'])
            if _id in relation:
                parent = relation[_id]
            else:
                parent = None

            post = {
                '_id': _id,  # 标签ID
                'title': title,  # 标签中文名
                'title_en': title_en,  # 标签英文名
                'level': level,  # 标签层级
                'parent': parent,  # 父级标签
            }
            label_new.insert(post)

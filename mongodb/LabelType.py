#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient


class LabelType:
    def __init__(self):
        pass

    @staticmethod
    def insert_label_type(address_new, port_new):
        # new database connection
        client = MongoClient(address_new, port_new)
        travel2 = client.travel2
        label_type = travel2.label_type

        # clean former data
        label_type.remove()

        post = {'type_id': 0,  # 标签类型ID
                'name': u"景点",  # 标签类型中文名
                'name_en': u"attraction"  # 标签类型英文名
                }
        label_type.insert(post)
        print(post)

        post = {'type_id': 1,  # 标签类型ID
                'name': u"购物",  # 标签类型中文名
                'name_en': u"shopping"  # 标签类型英文名
                }
        label_type.insert(post)
        print(post)

        post = {'type_id': 2,  # 标签类型ID
                'name': u"餐厅",  # 标签类型中文名
                'name_en': u"restaurant"  # 标签类型英文名
                }
        label_type.insert(post)
        print(post)

        post = {'type_id': 3,  # 标签类型ID
                'name': u"购物圈",  # 标签类型中文名
                'name_en': u"shopping"  # 标签类型英文名
                }
        label_type.insert(post)
        print(post)

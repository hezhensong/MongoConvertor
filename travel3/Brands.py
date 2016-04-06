#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient


class Brands:
    def __init__(self):
        pass

    @staticmethod
    def convert_brands(address_old, port_old, address_new, port_new):
        # old database connection
        client = MongoClient(address_old, port_old)
        travel1 = client.travel1

        # new database connection
        client = MongoClient(address_new, port_new)
        travel3 = client.travel3

        # get old collection and create new collection
        old_brands = travel1.brands
        new_brands = travel3.brand

        # clean former data
        new_brands.remove()

        for old_Brands in old_brands.find():
            post = {'_id': old_Brands['_id']}

            # 品牌类型
            if 'advice' in old_Brands:
                post['advice'] = str(old_Brands['advice']).strip()
            else:
                post['advice'] = ''

            if 'title' in old_Brands:
                post['title'] = str(old_Brands['title']).strip()
            else:
                post['title'] = ''

            if 'desc' in old_Brands:
                post['desc'] = str(old_Brands['desc']).strip()
            else:
                post['desc'] = ''

            if 'cover_image' in old_Brands:
                post['cover_image'] = str(old_Brands['cover_image']).strip()
            else:
                post['cover_image'] = ''

            # 插入数据库
            new_brands.insert(post)
            print(post)

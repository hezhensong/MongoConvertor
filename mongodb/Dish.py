#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient


class Dish:
    collection_old = 'restaurants'

    collection_new = 'dish'

    params_map = {}

    def __init__(self):
        pass

    @staticmethod
    def create_dish(address_old, port_old, address_new, port_new, collection_old, collection_new,
                     params_map):

        # old database connection
        client = MongoClient(address_old, port_old)
        travel1 = client.travel1

        # new database connection
        client = MongoClient(address_new, port_new)
        travel2 = client.travel2

        # get old collection and create new collection
        db_old = travel1[collection_old]
        db_new = travel2[collection_new]

        # clean former data
        db_new.remove()

        # 临时数组
        temp = [''] * len(params_map.keys())

        # 判断当前文档是否含有某个字段,若有则取出后赋值给临时数组,否则为 None
        for document in db_old.find():
            for i in range(len(params_map.keys())):
                if params_map.keys()[i] in document:
                    temp[i] = document[params_map.keys()[i]]

            # 需要特殊处理的字段,处理后以字典的形式添加到 other 中
            image_url = 'http://weegotest.b0.upaiyun.com/restaurant/iosimgs/'
            other = {}

            if 'menu' in document:
                dish = document['menu']
                for i in range(len(dish)):
                    if 'cover_image' in dish[i]:
                        if dish[i]['cover_image'] != '':
                            cover_image = image_url + dish[i]['cover_image']
                    desc = dish[i]['desc']
                    advice = dish[i]['advice']
                    
                    num = db_new.find({'cover_image': cover_image, 'desc':desc,
                                      'advice': advice}).count() 
                    if num > 1:
                        print('重复项')
                        print(document['_id'])
                        
                    else :
                        temp_dish = {}
                        temp_dish.update({'cover_image': cover_image, 'desc':desc,
                                      'advice': advice, 'title': '', 'tag': ''})
                        db_new.insert(temp_dish)
                        print temp_dish

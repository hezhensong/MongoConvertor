#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient


class Spot:
    collection_old = 'latestattractions'

    collection_new = 'spot'

    params_map = {}

    def __init__(self):
        pass

    @staticmethod
    def create_spot(address_old, port_old, address_new, port_new, collection_old, collection_new,
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

            image_url = 'http://weegotest.b0.upaiyun.com/attractions/iosimgs/'
            post = {}

            if 'spot' in document:
                spot = document['spot']
                if spot is not None:
                    for i in range(len(spot)):
                        if 'cover_image' in spot[i]:
                            if spot[i]['cover_image'] != '':
                                cover_image = image_url + spot[i]['cover_image']
                        if 'title' in spot[i]:
                            title = spot[i]['title']
                        if 'desc' in spot[i]:
                            desc = spot[i]['desc']
                        if 'advice' in spot[i]:
                            advice = spot[i]['advice']
                            
                        num = db_new.find({'cover_image': cover_image, 'title': title,
                                          'desc': desc, 'advice': advice}).count() 
                        if num > 1:
                            print('重复项')
                            print(document['_id'])
                        else:
                            temp_spot = {}
                            temp_spot.update({'cover_image': cover_image, 'title': title,
                                              'desc': desc, 'advice': advice, 'tag': ''})
                            db_new.insert(temp_spot)
                            print(temp_spot)

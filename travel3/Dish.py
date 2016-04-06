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
    def create_dish(address_old, port_old, address_new, port_new):

        # old database connection
        client = MongoClient(address_old, port_old)
        travel1 = client.travel1

        # new database connection
        client = MongoClient(address_new, port_new)
        travel3 = client.travel3

        # get old collection and create new collection
        db_old = travel1.restaurants
        db_new = travel3.dish

        # clean former data
        db_new.remove()

        image_url = 'http://weegotest.b0.upaiyun.com/restaurant/iosimgs/'
        cover_image = ''
        desc = ''
        advice = ''
        for document in db_old.find():
            if 'menu' in document:
                dish = document['menu']
                for i in range(len(dish)):
                    if 'cover_image' in dish[i]:
                        if dish[i]['cover_image'] != '':
                            cover_image = image_url + dish[i]['cover_image']
                    if 'desc' in dish[i]:
                        desc = dish[i]['desc']
                    if 'advice' in dish[i]:
                        advice = dish[i]['advice']
                    
                    num = db_new.find({'cover_image': cover_image, 'desc':desc,
                                      'advice': advice}).count() 
                    if num > 1:
                        print('重复项')
                        print(document['_id'])
                    else :
                        new_dish = {}
                        new_dish.update({'cover_image': cover_image, 'desc':desc,
                                      'advice': advice, 'title': '', 'tag': ''})
                        db_new.insert(new_dish)
                        print new_dish

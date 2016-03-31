#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId


class Pgc:
    def __init__(self):
        pass

    collection_old = 'pgcs'

    collection_new = 'pgc'

    params_map = {'_id': '_id',
                  'cover_image': 'cover_image',
                  'title': 'title',
                  'introducation': 'introduction'
                  }

    @staticmethod
    def convert_pgc(address_old, port_old, address_new, port_new,
                    collection_old, collection_new, params_map):

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

            person = ''
            city_id = ''
            poi_list = []
            temp_poi_list = []
            _id = ''
            name = ''
            poi_desc = ''
            poi_image = ''
            poi_image_desc = ''
            type = -1
            temp_type = ''
            tag = ''
            other = {}
            
            if 'pgc_tags' in document:
                tag = document['pgc_tags']
            
            if 'type' in document:
                type = int(document['type'])

            if 'pgc_people' in document:
                person = document['pgc_people']
                if '_id' in person:
                    if person['_id'] != '':
                        person = ObjectId(person['_id'].strip())
                    else:
                        person = ''

            if 'pgc_city' in document:
                city_id = document['pgc_city']
                if '_id' in city_id:
                    city_id = ObjectId(city_id['_id'].strip())

            if 'pgc_poi' in document:
                temp_poi_list = document['pgc_poi']
                for i in range(len(temp_poi_list)):
                    if '_id' in temp_poi_list[i]:
                        _id = temp_poi_list[i]['_id']
                    if 'type' in temp_poi_list[i]:
                        if temp_poi_list[i]['type'] != '':
                            temp_type = temp_poi_list[i]['type']
                    if 'name' in temp_poi_list[i]:
                        name = temp_poi_list[i]['name']
                    if 'poi_desc' in temp_poi_list[i]:
                        poi_desc = temp_poi_list[i]['poi_desc']
                    if 'poi_image' in temp_poi_list[i]:
                        poi_image = "http://weegotest.b0.upaiyun.com/attractions/origin/" + temp_poi_list[i]['poi_image']
                    if 'poi_image_desc' in temp_poi_list[i]:
                        poi_image_desc = temp_poi_list[i]['poi_image_desc']
                    if _id.find('*') != -1:
                        _id = ''
                        temp_type =''
                    temp_poi = {}
                    temp_poi.update({'_id': _id, 'type':temp_type, 'paragraph_desc': poi_desc, 'name': name,
                                     'poi_image': poi_image, 'paragraph_title': poi_image_desc, 'image_url':'', 'image_source': ''})
                    poi_list.append(temp_poi)

            original = {}
            original.update({'image': '', 'desc':'','url': '', 'author': '', 'source': ''})
            other.update({'original' : original, 'tag': tag,
                          'person': person, 'city_id': city_id,
                          'poi_list': poi_list, 'type': type })

            post = {}
            post.update(other)
            for i in range(len(params_map.keys())):
                post.update({params_map.values()[i]: temp[i]})

            post['cover_image'] = "http://weegotest.b0.upaiyun.com/brands/iosimgs/" + post['cover_image']

            db_new.insert(post)
            print post

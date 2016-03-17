#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient


class Attraction:
    def __init__(self):
        pass

    collection_old = 'latestattractions'

    collection_new = 'attraction'

    params_map = {'_id': '_id', # 景点 ID
                  'activities': 'activities', # 景点活动
                  'address': 'address', # 景点地址
                  'attractions': 'name', # 景点名
                  'attractions_en': 'name_en', # 景点英文名
                  'city_id': 'city_id', # 城市 ID
                  'cityname': 'city_name', # 城市名
                  'comments': 'comments', # 评论
                  'comments_from': 'comments_from', # 评论来源
                  'comments_url': 'comments_url', # 评论 url
                  'coverImageName': 'cover_image', # 背景图片
                  'image': 'image', # 图片
                  'introduce': 'introduction', # 介绍
                  'masterLabelNew': 'master_label', # 景点主标签
                  'subLabelNew': 'sub_label', # 景点次标签  
                  'price': 'price_desc', # 价格描述
                  'short_introduce': 'brief_introduction', # 简介
                  'telno': 'tel', # 电话
                  'tips': 'tips', # 提示
                  'website': 'website', # 网站
                  'yelp_rating': 'rating', # 评分
                  'spot': 'spot' 
                  }

    @staticmethod
    def convert_attraction(address_old, port_old, address_new, port_new, collection_old, collection_new,
                           params_map):

        # old database connection
        client = MongoClient(address_old, port_old)
        travel1 = client.travel1

        # new database connection
        client = MongoClient(address_new, port_new)
        travel2 = client.travel2

        # get old collection and coeate new collection
        db_old = travel1[collection_old]
        db_new = travel2[collection_new]

        # clean former data
        db_new.remove()

        # 临时数组
        temp = [None] * len(params_map.keys())

        # 判断当前文档是否含有某个字段,若有则取出后赋值给临时数组,否则为 None
        for document in db_old.find():
            print(document['_id'])
            for i in range(len(params_map.keys())):
                if params_map.keys()[i] in document:
                    temp[i] = document[params_map.keys()[i]]

            # 需要特殊处理的字段,处理后以字典的形式添加到 other 中
            coordination = None
            latitude = None
            longitude = None
            open_time = []
            other = {}

            if 'latitude' in document:

                latitude = str(document['latitude'])
            if 'longitude' in document:
                longitude = str(document['longitude'])

                coordination = latitude + ',' + longitude

            if 'open_time' in document:
                temp_open_time = document['open_time']
                if type(temp_open_time) == dict:
                    for i in range(len(temp_open_time)):
                        open_time.append(temp_open_time[i]['desc'])
                else:
                    open_time.append(temp_open_time)

            # 是否线上展示
            if 'show_flag' in document:
                show_flag = document['show_flag']
                if show_flag == u'1':
                    is_show = True
                else:
                    is_show = False
            else:
                is_show = False

            # 是否推荐
            if 'recommand_flag' in document:
                is_recommend = document['recommand_flag']
                if is_recommend == u'1':
                    is_recommend = True
                else:
                    is_recommend = False
            else:
                is_recommend = False

            other.update({'is_show': is_show, 'is_recommend': is_recommend,
                          'coordination': coordination , 'open_time': open_time,
                          'open_table_url': None,
                          'last_modified_person': None, 'last_modified_time': None})

            post = {}
            post.update(other)
            for i in range(len(params_map.keys())):
                post.update({params_map.values()[i]: temp[i]})
            db_new.insert(post)
            print post

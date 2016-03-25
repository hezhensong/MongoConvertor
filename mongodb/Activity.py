#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import datetime
import pytz

from pymongo import MongoClient
from TimeZoneUtil import TimeZoneUtil


class Activity:
    # 定义旧集合的名字
    collection_old = 'activities'

    # 定义新集合的名字
    collection_new = 'activity'

    # 定义参数字典,其中键为旧集合的字段名,值为新集合的字段名
    # 注意:这里只定义不需要做特殊处理的字段
    params_map = {
        '_id': '_id',  # 活动 ID
        'acturl': 'act_url',  # 活动 url
        'atype': 'type',  # 活动类型
        'cover_image': 'cover_image',  # 背景图片
        'deaddress': 'detail_address',  # 详细地址
        'desc': 'description',  # 描述
        'order_url': 'order_url',  # 订票地址
        'title': 'title',  # 标题
        'address': 'address'
    }

    def __init__(self):
        pass

    @staticmethod
    def convert_activity(address_old,
                         port_old,
                         address_new,
                         port_new,
                         collection_old,
                         collection_new,
                         params_map):

        # old database connection
        client = MongoClient(address_old, port_old)
        travel1 = client.travel1

        latestcity = travel1.latestcity

        # new database connection
        client = MongoClient(address_new, port_new)
        travel2 = client.travel2

        # get old collection and coeate new collection
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
            other = {}
            paragraphs = []

            start_time = ''
            end_time = ''
            act_time = ''
            coordination = ''
            latitude = ''
            longitude = ''
            if 'start_time' in document:
                start_time = document['start_time']
            if 'end_time' in document:
                end_time = document['end_time']
            if 'acttime' in document:
                    act_time = document['acttime']
            if 'latitude' in document:
                latitude = document['latitude']
            if 'longitude' in document:
                longitude = document['longitude']
                coordination = longitude + ',' + latitude

            paragraphs.append({'image_title': '', 'image_url': '',
                               'detail': '', 'image_brief': ''})

            other.update({'start_time': start_time, 'end_time': end_time, 
                          'act_time': act_time, 'coordination': coordination,
                          'last_modified_person': '', 'last_modified_time': datetime.datetime(1970,1,1),
                          'paragraphs': paragraphs})
            post = {}

            post.update(other)
            for i in range(len(params_map.keys())):
                post.update({params_map.values()[i]: temp[i]})

            if post['title'] == u'猴年特展（Monkey Business）':
                pass

            # 添加关联的城市ID
            post['city_id'] = ''
            for city in latestcity.find():
                found = False

                if 'activity_labels' in city:
                    for activity_label in city['activity_labels']:
                        if activity_label['title'] == post['title']:
                            post['city_id'] = city['_id']
                            found = True
                            break

                if found is True:
                    break

            # 修改图片地址为全路径
            post['cover_image'] = "http://weegotest.b0.upaiyun.com/activities/iosimgs/" + post['cover_image']
            db_new.insert(post)
            print post
            
        new_start_time = datetime.datetime(1970,1,1,0,0,0,tzinfo=pytz.utc)
        new_end_time = datetime.datetime(1970,1,1,0,0,0,tzinfo=pytz.utc)
        for document in db_new.find():
            temp_start_time = document['start_time']
            new_start_year = int(temp_start_time[0:4])
            new_start_month = int(temp_start_time[4:6])
            new_start_day = int(temp_start_time[6:8])
            
            if document['city_id'] != '':
                new_start_time = TimeZoneUtil.gettimezone(document['city_id'], new_start_year, new_start_month, new_start_day,
                                                       0, 0, 0)
            
            temp_end_time = document['end_time']
            new_end_year = int(temp_end_time[0:4])
            new_end_month = int(temp_end_time[4:6])
            new_end_day = int(temp_end_time[6:8])
            
            if document['city_id'] != '':
                new_end_time = TimeZoneUtil.gettimezone(document['city_id'], new_end_year, new_end_month, new_end_day,
                                                       0, 0, 0)
            
            db_new.update({'_id':document['_id']},{"$set": {'start_time': new_start_time, 'end_time': new_end_time}}) 
        
            

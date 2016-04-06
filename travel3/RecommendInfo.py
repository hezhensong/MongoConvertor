#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient
import datetime
import pytz
from bson.objectid import ObjectId

class RecommendInfo:

    # 定义参数字典,其中键为旧集合的字段名,值为新集合的字段名
    # 注意:这里只定义不需要做特殊处理的字段
    params_map = {
        '_id': '_id',
        'city_name': 'city_name',
        'recommend_poi_position': 'coordination'
    }

    def __init__(self):
        pass

    @staticmethod
    def convert_recommend_info(address_old, port_old, address_new, port_new):

        # old database connection
        client = MongoClient(address_old, port_old)
        travel1 = client.travel1

        # new database connection
        client = MongoClient(address_new, port_new)
        travel3 = client.travel3

        # get old collection and coeate new collection
        db_old = travel1.recommendinfo
        db_new = travel3.recommend_info

        # clean former data
        db_new.remove()

        for document in db_old.find():
            post = {'_id': document['_id']}

            # city id, 需要转换为 ObjectId 类型
            if 'city_id' in document:
                city_id = document['city_id']
                if city_id != '':
                    if type(city_id) == unicode:
                        city_id = ObjectId(city_id.encode('utf-8'))
                post['city_id'] = city_id
            else:
                post['city_id'] = ''
            
            # city name
            if 'city_name' in document:
                post['city_name'] = document['city_name']
            else:
                post['city_name'] = ''
                
            # type
            if 'type' in document:
                post['type'] = document['type']
            else:
                post['type'] = int(-1)
            
            recommend_content = ''
            cover_image = ''
            content_title = ''
            content_first = ''
            content_second = ''
            content_desc = ''
            content_url = ''

            if 'recommend_start_time' in document:
                start_time = document['recommend_start_time']
            if 'recommend_start_date' in document:
                start_date = document['recommend_start_date']
            if 'recommend_start_time' in document:
                end_time = document['recommend_end_time']
            if 'recommend_end_time' in document:
                end_date = document['recommend_end_date']
                
            year = int(start_date[0:4])
            month = int(start_date[4:6])
            day = int(start_date[6:8])
            new_start_time = datetime.datetime(year,month,day,int(start_time), 0, 0, tzinfo=pytz.utc)
            post['start_time'] = new_start_time
            
            year = int(end_date[0:4])
            month = int(end_date[4:6])
            day = int(end_date[6:8])
            new_end_time = datetime.datetime(year,month,day,int(end_time), 0, 0, tzinfo=pytz.utc)
            post['end_time'] = new_end_time
                    
            if 'recommend_content' in document:
                recommend_content = document['recommend_content']
                if 'recommend_content_id' in recommend_content:
                    content_id = recommend_content['recommend_content_id']
                if 'recommend_content_title' in recommend_content:
                    content_title = recommend_content['recommend_content_title']
                if 'recommend_content_first' in recommend_content:
                    content_first = recommend_content['recommend_content_first']
                if 'recommend_content_second' in recommend_content:
                    content_second = recommend_content['recommend_content_second']
                if 'recommend_content_desc' in recommend_content:
                    content_desc = recommend_content['recommend_content_desc']
                if 'recommend_content_url' in recommend_content:
                    content_url = recommend_content['recommend_content_url']
                if 'cover_image' in recommend_content:
                    cover_image = recommend_content['cover_image']
                temp_content = {}        
                temp_content.update({'content_id': content_id,
                                     'content_title': content_title,
                                     'content_first': content_first,
                                     'content_second': content_second,
                                     'content_desc': content_desc,
                                     'content_url': content_url,
                                     'cover_image': cover_image})
                post['content'] = temp_content

            
            db_new.insert(post)
            
            if 'city_id' in document:
                city_id = document['city_id']
                if city_id == '':
                    db_new.remove(document['_id'])
            print post

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import HTMLParser
import datetime

import pytz
from bson import ObjectId
from pymongo import MongoClient


class Attraction:
    def __init__(self):
        pass

    @staticmethod
    def convert_attraction(address_old, port_old, address_new, port_new):

        # old database connection
        client = MongoClient(address_old, port_old)
        travel1 = client.travel1

        # new database connection
        client = MongoClient(address_new, port_new)
        travel3 = client.travel3

        # get old collection and create new collection
        latestattractions = travel1.latestattractions
        attraction = travel3.attraction

        # clean former data
        attraction.remove()

        for latest_attraction in latestattractions.find():
            post = {'_id': latest_attraction['_id']}

            # 中文名、英文名都没有，当做脏数据删除
            if 'attractions' not in latest_attraction and 'attractions_en' not in latest_attraction:
                print "脏数据: ", post['_id']
                continue

            # 中文名
            if 'attractions' in latest_attraction:
                post['name'] = latest_attraction['attractions']
            else:
                post['name'] = ''

            # 英文名
            if 'attractions_en' in latest_attraction:
                post['name_en'] = latest_attraction['attractions_en']
            else:
                post['name_en'] = ''

            # 是否线上展示
            if 'show_flag' in latest_attraction:
                show_flag = latest_attraction['show_flag']
                if show_flag == u'1':
                    post['is_show'] = True
                else:
                    post['is_show'] = False
            else:
                post['is_show'] = False

            # 是否已经删除
            post['is_delete'] = False

            # city id
            if 'city_id' in latest_attraction:
                post['city_id'] = latest_attraction['city_id']
            else:
                post['city_id'] = ''

            # city name
            if 'cityname' in latest_attraction:
                post['city_name'] = latest_attraction['cityname']
            else:
                post['city_name'] = ''

            # Google Place ID
            if 'googleId' in latest_attraction:
                post['google_place_id'] = latest_attraction['googleId']
            else:
                post['google_place_id'] = ''

            # 新增字段：排序
            post['order'] = 0.0

            # 景点详情页轮播图
            post['image'] = []
            image_url = 'http://weegotest.b0.upaiyun.com/attractions/iosimgs/'

            if 'image' in latest_attraction:
                image_list = latest_attraction['image']

                for image_item in image_list:
                    image_element = {
                        'url': image_url + image_item,
                        'use': ''
                    }
                    post['image'].append(image_element)

            # 地址
            post['address'] = {
                'continent': '',
                'country': '',
                'city': ''
            }

            # 详细地址
            if 'address' in latest_attraction:
                post['address_detail'] = latest_attraction['address']
            else:
                post['address_detail'] = ''

            # 经纬度

            # 特例，经纬度写的不规范
            if latest_attraction['_id'] == ObjectId('536a09f91713475210000002'):
                latest_attraction['longitude'] = latest_attraction['longitude'].replace(u'，', u'.')
                latest_attraction['latitude'] = latest_attraction['latitude'].replace(u'，', u'.')

            if 'longitude' in latest_attraction and 'latitude' in latest_attraction:
                longitude = str(latest_attraction['longitude'])
                latitude = str(latest_attraction['latitude'])
                post['coordinate'] = longitude.strip() + ',' + latitude.strip()
            else:
                post['coordinate'] = ''

            # 价格描述
            if 'price' in latest_attraction:
                post['price_desc'] = str(latest_attraction['price'])
            else:
                post['price_desc'] = ''

            # 价格等级
            if 'price_level' in latest_attraction:
                post['price_level'] = int(latest_attraction['price_level'])
            else:
                post['price_level'] = 0

            # 营业时间
            if 'open_time' in latest_attraction:
                post['open_time'] = latest_attraction['open_time']
            else:
                post['open_time'] = []

            # 营业时间描述
            if 'opentime' in latest_attraction and type(latest_attraction['opentime']) == 'str':
                post['open_time_desc'] = str(latest_attraction['opentime'])
            else:
                post['open_time_desc'] = ''

            # 交通信息
            if 'traffic_info' in latest_attraction:
                post['traffic_info'] = HTMLParser.HTMLParser().unescape(latest_attraction['traffic_info'])
            else:
                post['traffic_info'] = ''

            # 网址
            if 'website' in latest_attraction:
                post['website'] = str(latest_attraction['website'])
            else:
                post['website'] = ''

            # 电话
            if 'telno' in latest_attraction:
                post['telephone'] = str(latest_attraction['telno'])
            else:
                post['telephone'] = ''

            # 建议游览时长
            if 'recommand_duration' in latest_attraction and len(latest_attraction['recommand_duration']) > 0:
                if latest_attraction['recommand_duration'] == '两天':
                    post['recommend_duration'] = int(1440 * 2)

                elif latest_attraction['recommand_duration'] == '全天' \
                        or latest_attraction['recommand_duration'] == '一天' \
                        or latest_attraction['recommand_duration'] == '1天':
                    post['recommend_duration'] = int(1440)

                elif latest_attraction['recommand_duration'] == '半天' \
                        or latest_attraction['recommand_duration'] == '半日':
                    post['recommend_duration'] = int(60 * 6)

                elif latest_attraction['recommand_duration'] == '2个小时':
                    post['recommend_duration'] = int(120)

                elif latest_attraction['recommand_duration'] == '一小时':
                    post['recommend_duration'] = int(60)

                else:
                    post['recommend_duration'] = int(latest_attraction['recommand_duration'])

            else:
                post['recommend_duration'] = int(0)

            # 一句话简介
            if 'short_introduce' in latest_attraction:
                post['brief_introduction'] = HTMLParser.HTMLParser().unescape(latest_attraction['short_introduce'])
            else:
                post['brief_introduction'] = ''

            # 简介
            if 'short_introduce' in latest_attraction:
                post['introduction'] = HTMLParser.HTMLParser().unescape(latest_attraction['introduce'])
            else:
                post['introduction'] = ''

            # 小贴士
            if 'tips' in latest_attraction:
                post['tips'] = HTMLParser.HTMLParser().unescape(latest_attraction['tips'])
            else:
                post['tips'] = ''

            # 预定来源
            post['book_source'] = ''

            # 预订URL
            post['book_url'] = ''

            # 总评分
            post['rating'] = 0.0

            # 类别标签
            if 'masterLabelNew' in latest_attraction and isinstance(latest_attraction['masterLabelNew'], dict):
                post['label'] = {
                    'id': latest_attraction['masterLabelNew']['_id'],
                    'name': latest_attraction['masterLabelNew']['label']
                }
            else:
                post['label'] = {
                    'id': ObjectId('000000000000'),
                    'name': '未归类'
                }

            # 属性标签
            post['tag'] = []
            if 'subLabelNew' in latest_attraction and latest_attraction['subLabelNew'] is not None:
                for tags in latest_attraction['subLabelNew']:
                    if '_id' in tags and 'label' in tags and \
                                    len(str(tags['_id']).strip()) > 0 and len(str(tags['label']).strip()) > 0:
                        tag = {
                            'id': ObjectId(tags['_id']),
                            'name': tags['label']
                        }
                        post['tag'].append(tag)

            # 评论来源
            if 'comments_from' in latest_attraction:
                post['comments_from'] = latest_attraction['comments_from']
            else:
                post['comments_from'] = ''

            # 评论URL
            if 'comments_url' in latest_attraction:
                post['comments_url'] = latest_attraction['comments_url']
            else:
                post['comments_url'] = ''

            # 评论内容
            post['comments'] = []
            if 'comments' in latest_attraction:
                post_comment = {}

                for comment in latest_attraction['comments']:
                    if 'title' in comment:
                        post_comment['title'] = comment['title']
                    else:
                        post_comment['title'] = ''

                    post_comment['rating'] = int(comment['rating'])
                    post_comment['text'] = comment['text']
                    post_comment['date'] = comment['date']
                    post_comment['nickname'] = comment['nickname']

                    if 'language' in comment:
                        post_comment['language'] = comment['language']
                    else:
                        post_comment['language'] = ''

                    post['comments'].append(post_comment)

            # 亮点
            post['spot'] = []
            if 'spot' in latest_attraction:
                post_spot = {}

                for spot in latest_attraction['spot']:
                    if 'cover_image' in spot and spot['cover_image'] is not None:
                        post_spot['cover_image'] = spot['cover_image']
                    else:
                        post_spot['cover_image'] = ''

                    if 'title' in spot and spot['title'] is not None:
                        post_spot['title'] = spot['title']
                    else:
                        post_spot['title'] = ''

                    if 'desc' in spot and spot['desc'] is not None:
                        post_spot['desc'] = spot['desc']
                    else:
                        post_spot['desc'] = ''

                    if 'advice' in spot and spot['advice'] is not None:
                        post_spot['advice'] = spot['advice']
                    else:
                        post_spot['advice'] = ''

                    post['spot'].append(post_spot)

            # 最后修改记录
            post['last_modified_person'] = ''
            post['last_modified_time'] = datetime.datetime(2016, 3, 29, 0, 0, 0, tzinfo=pytz.utc)

            # 插入数据库
            attraction.insert(post)
            print(post)

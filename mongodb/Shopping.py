#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient
import datetime

class Shopping:
    collection_old = 'shoppings'

    collection_new = 'shopping'
    
    params_map = {'_id':'_id', # 购物 ID
                  'activities': 'activities', # 购物活动
                  'address': 'address', # 购物地址
                  'name': 'name', # 购物名
                  'name_en': 'name_en', # 购物英文名
                  'city_id': 'city_id', # 城市 ID
                  'city_name': 'city_name', # 城市名
                  'comments_from': 'comments_from', # 评论来源
                  'comments_url': 'comments_url', # 评论 url
                  'cover_image': 'cover_image', # 背景图片
                  'image': 'image', # 图片
                  'introduce': 'introduction', # 介绍
                  'price_desc': 'price_desc', # 价格描述
                  'brief_introduce': 'brief_introduction', # 简介
                  'tel': 'tel', # 电话
                  'tips': 'tips', # 提示
                  'url': 'website', # 网站
                  'rating': 'rating' # 评分
                }

    def __init__(self):
        pass

    @staticmethod
    def convert_shopping(address_old, port_old, address_new, port_new, collection_old, collection_new,
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
            for i in range(len(params_map.keys())):
                if params_map.keys()[i] in document:
                    temp[i] = document[params_map.keys()[i]]

            # 需要特殊处理的字段,以字典的形式添加到 other 中
            coordination = None
            latitude = None
            longitude = None
            open_time = []
            master_tag = {}
            comments = []
            new_comments = []
            new_date = None
            rating = None
            nickname = None
            text = None
            title = None
            language = 'zh'
            sub_tag = []
            temp_sub_tag = {}
            _id = None
            tag = None
            brand = []
            temp_brand = {}
            new_brand = []
            cover_image =  None
            title = None
            desc = None
            advice = None
            other = {}
            
            if 'category' in document:
                category = document['category']
                if len(category) > 0:
                    master_tag.update({'_id':category[0]['_id'],'tag':category[0]['name']})
                
                for i in range(len(category)):
                    if category != None:
                        if '_id' in category[i]:
                            _id = category[i]['_id']
                        if 'name' in category[i]:
                            tag = category[i]['name']
                        temp_sub_tag.update({'_id': _id, 'tag': tag})
                        sub_tag.append(temp_sub_tag)
                
            if 'latitude' in document:
                latitude = str(document['latitude'])
            if 'longitude' in document:
                longitude = str(document['longitude'])
                coordination = longitude + ',' + latitude
                
            if 'open_time' in document:
                temp_open_time = document['open_time']
                if type(temp_open_time) == list:
                    for i in range(len(temp_open_time)):
                        open_time.append(temp_open_time[i]['desc'])
                else:
                    open_time.append(temp_open_time)
            
            if 'brand' in document:
                brand = document['brand']
                if brand != None:
                    for i in range(len(brand)):
                        if 'cover_image' in brand[i]:
                            cover_image = brand[i]['cover_image']
                        if 'title' in brand[i]:
                            title = brand[i]['title']
                        if 'desc' in brand[i]:
                            desc = brand[i]['desc']
                        if 'advice' in brand[i]:
                            advice = brand[i]['advice']
                        temp_brand.update({'cover_image': cover_image, 'title': title,
                                          'desc': desc, 'advice': advice, 'tag': None})
                        new_brand.append(temp_brand)
            
            
            if 'comments' in document:
                comments = document['comments']
                for i in range(len(comments)):
                    if type(comments[i]) == unicode:
                        temp_comments = {}
                        temp_comments.update({'date': None,'rating': rating,'nickname': nickname,
                                              'language': language,'text': comments[i], 'title': title})
                        new_comments.append(temp_comments)
                    else:
                        if comments != [None]:
                            if 'date' in comments[i]:
                                temp_date = comments[i]['date'].encode('utf-8').strip()
                                index1 = temp_date.find('年')
                                index2 = temp_date.find('月')
                                index3 = temp_date.find('日')
                                if index1 != -1:
                                    year = int(temp_date[0:index1])
                                    month = int(temp_date[index1+3:index2])
                                    if month == 0:
                                        month = 1
                                    day = int(temp_date[index2+3:index3])
                                    if day == 0:
                                        day = 1
                                    new_date = datetime.datetime(year, month ,day)
                                else:
                                    new_date = None
                            if 'rating' in comments[i]:
                                rating = comments[i]['rating']
                            if 'nickname' in comments[i]:
                                nickname = comments[i]['nickname']
                            if 'text' in comments[i]:
                                text = comments[i]['text']
                            if 'title' in comments[i]:
                                title = comments[i]['title']
                            temp_comments = {}
                            temp_comments.update({'date': new_date,'rating': rating,'nickname': nickname,
                                                  'language': language,'text': text, 'title': title})
                            new_comments.append(temp_comments)
            
            # 是否线上展示
            if 'show_flag' in document:
                show_flag = document['show_flag']
                if show_flag == u'1':
                    is_show = True
                else:
                    is_show = False
            else:
                is_show = False
            
            other.update({'coordination': coordination , 'open_time': open_time,'sub_tag': sub_tag,
                          'master_tag': master_tag, 'is_show': is_show, 'comments': new_comments,
                          'brand': new_brand, 'last_modified_person': None, 'last_modified_time': None})

            post = {}
            post.update(other)
            for i in range(len(params_map.keys())):
                post.update({params_map.values()[i]: temp[i]})
            db_new.insert(post)
            print post

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient
import datetime
import time
import HTMLParser
from bson.objectid import ObjectId

class Attraction:
    def __init__(self):
        pass

    collection_old = 'latestattractions'

    collection_new = 'attraction'

    params_map = {'_id': '_id', # 景点 ID
                  'address': 'address', # 景点地址
                  'attractions': 'name', # 景点名
                  'attractions_en': 'name_en', # 景点英文名
                  'city_id': 'city_id', # 城市 ID
                  'cityname': 'city_name', # 城市名
                  'comments_from': 'comments_from', # 评论来源
                  'comments_url': 'comments_url', # 评论 url
                  'price': 'price_desc', # 价格描述
                  'telno': 'tel', # 电话
                  'website': 'website', # 网站
                  'yelp_rating': 'rating' # 评分
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
        temp = [''] * len(params_map.keys())

        # 判断当前文档是否含有某个字段,若有则取出后赋值给临时数组,否则为 ''
        for document in db_old.find():
            for i in range(len(params_map.keys())):
                if params_map.keys()[i] in document:
                    temp[i] = document[params_map.keys()[i]]

            # 需要特殊处理的字段,处理后以字典的形式添加到 other 中
            coordination = ''
            latitude = ''
            longitude = ''
            open_time = []
            comments = []
            activities = []
            new_comments = []
            new_date = datetime.datetime(1970, 1 ,1)
            rating = ''
            nickname = ''
            text = ''
            title = ''
            language = 'zh'
            master_tag = {}
            new_master_tag = {}
            sub_tag = []
            new_sub_tag = []
            _id = ''
            tag = ''
            spot = []
            spot_id = ''
            new_spot = []
            cover_image =  ''
            spot_cover_image = ''
            image = []
            title = ''
            desc = ''
            advice = ''
            image_url = 'http://weegotest.b0.upaiyun.com/attractions/iosimgs/'
            introduction = ''
            brief_introduction = ''
            tips = ''
            price_level = 1
            last_modified_time = datetime.datetime(1970, 1, 1)
            other = {}
            
            if 'activities' in document:
                activities = document['activities']
            
            if 'price_level' in document:
                price_level = document['price_level']
            
            if 'introduce' in document:
                introduction = document['introduce']
                if (introduction.find('&') != -1):
                    introduction = HTMLParser.HTMLParser().unescape(introduction)
                    
            if 'short_introduce' in document:
                brief_introduction = document['short_introduce']
                if (brief_introduction.find('&') != -1):
                    brief_introduction = HTMLParser.HTMLParser().unescape(brief_introduction)
            
            if 'tips' in document:
                tips = document['tips']
                if (tips.find('&') != -1):
                    tips = HTMLParser.HTMLParser().unescape(tips)
            
            if 'coverImageName' in document:
                cover_image = document['coverImageName']
                if cover_image != '':
                    cover_image = image_url + cover_image
                    
            if 'image' in document:
                image = document['image']
                if image is not None and len(image) > 0:
                    for i in range(len(image)):
                        image[i] = image_url + image[i]
                        
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
            
            if 'comments' in document:
                comments = document['comments']
                for i in range(len(comments)):
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
                            new_date = datetime.datetime(1970, 1 ,1)
                            
                    if 'rating' in comments[i]:
                        rating = comments[i]['rating']
                    if 'nickname' in comments[i]:
                        nickname = comments[i]['nickname']
                    if 'text' in comments[i]:
                        text = comments[i]['text']
                    if 'title' in comments[i]:
                        title = comments[i]['title']
                    if 'language' in comments[i]:
                        language = comments[i]['language']
                    temp_comments = {}
                    temp_comments.update({'date': new_date,'rating': rating,'nickname': 
                                          nickname,'text': text, 'title': title, 'language': language})
                    new_comments.append(temp_comments)

            if 'masterLabelNew' in document:
                master_tag = document['masterLabelNew']
                if '_id' in master_tag:
                    _id = master_tag['_id']
                if 'label' in master_tag:
                    tag = master_tag['label']
                new_master_tag.update({'_id': _id,'label': tag})
                
            if 'subLabelNew' in document:
                sub_tag = document['subLabelNew']
                if sub_tag is not None and sub_tag != '':
                    for i in range(len(sub_tag)):
                        if '_id' in sub_tag[i]:
                            _id = sub_tag[i]['_id']
                        if 'label' in sub_tag[i]:
                            tag = sub_tag[i]['label']
                        temp_sub_tag = {}    
                        temp_sub_tag.update({'_id': _id, 'tag': tag})
                        new_sub_tag.append(temp_sub_tag)
            
            if 'spot' in document:
                spot = document['spot']
                if spot != '':
                    for i in range(len(spot)):
                        if 'cover_image' in spot[i]:
                            if spot[i]['cover_image'] != '':
                                spot_cover_image = image_url + spot[i]['cover_image']
                        if 'title' in spot[i]:
                            title = spot[i]['title']
                        if 'desc' in spot[i]:
                            desc = spot[i]['desc']
                        if 'advice' in spot[i]:
                            advice = spot[i]['advice']
                        
                        spot_id = travel2['spot'].find_one({'cover_image': spot_cover_image, 'title': title,
                                          'desc': desc, 'advice': advice})['_id']
                        
                        temp_spot = {}
                        temp_spot.update({'_id': spot_id, 'cover_image': spot_cover_image, 'title': title,
                                          'desc': desc, 'advice': advice, 'tag': ''})
                        new_spot.append(temp_spot)
            # 是否线上展示
            if 'show_flag' in document:
                show_flag = document['show_flag']
                if show_flag == u'1':
                    is_show = True
                else:
                    is_show = False
            else:
                is_show = False


            other.update({'is_show': is_show,'coordination': coordination , 'open_time': open_time,
                          'open_table_url': '', 'comments': new_comments,'spot': new_spot,
                          'cover_image': cover_image, 'image': image, 'price_level': price_level,
                          'activities': activities, 'master_label': new_master_tag,'sub_tag': new_sub_tag,
                          'last_modified_person': '', 'last_modified_time':  last_modified_time,
                          'introduction': introduction, 'brief_introduction': brief_introduction, 'tips': tips })

            post = {}
            post.update(other)
            for i in range(len(params_map.keys())):
                post.update({params_map.values()[i]: temp[i]})
            db_new.insert(post)
            print post

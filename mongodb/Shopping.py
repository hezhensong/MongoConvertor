#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime
import HTMLParser
import datetime

class Shopping:
    collection_old = 'shoppings'

    collection_new = 'shopping'
    
    params_map = {'_id':'_id', # 购物 ID
                  'address': 'address', # 购物地址
                  'name': 'name', # 购物名
                  'name_en': 'name_en', # 购物英文名
                  'city_id': 'city_id', # 城市 ID
                  'city_name': 'city_name', # 城市名
                  'comments_from': 'comments_from', # 评论来源
                  'comments_url': 'comments_url', # 评论 url
                  'price_desc': 'price_desc', # 价格描述
                  'tel': 'tel', # 电话
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
        temp = [''] * len(params_map.keys())

        # 判断当前文档是否含有某个字段,若有则取出后赋值给临时数组,否则为 None
        for document in db_old.find():
            for i in range(len(params_map.keys())):
                if params_map.keys()[i] in document:
                    temp[i] = document[params_map.keys()[i]]

            # 需要特殊处理的字段,以字典的形式添加到 other 中
            coordination = ''
            latitude = ''
            longitude = ''
            open_time = []
            master_tag = {}
            comments = []
            new_comments = []
            new_date = datetime.datetime(1970,1,1)
            rating = ''
            nickname = ''
            text = ''
            title = ''
            language = 'zh'
            sub_tag = []
            _id = ''
            tag = ''
            brand = []
            new_brand = []
            brand_id = ''
            cover_image = ''
            brand_cover_image =  ''
            image = []
            title = ''
            desc = ''
            advice = ''
            image_url = 'http://weegotest.b0.upaiyun.com/shoparea/iosimgs/'
            introduction = ''
            brief_introduction = ''
            tips = ''
            price_level = 1
            activities = []
            master_label = []
            other = {}
            
            if 'activities' in document:
                activities = document['activities']
            
            if 'price_level' in document:
                price_level = document['price_level']
                if type(price_level) == str or type(price_level) == unicode:
                    price_level = 1
                if price_level == 5:
                    price_level = 4
            
            if 'introduce' in document:
                introduction = document['introduce']
                if (introduction.find('#') != -1):
                    introduction = HTMLParser.HTMLParser().unescape(introduction)
                    
            if 'short_introduce' in document:
                brief_introduction = document['short_introduce']
                if (brief_introduction.find('#') != -1):
                    brief_introduction = HTMLParser.HTMLParser().unescape(brief_introduction)
            
            if 'tips' in document:
                tips = document['tips']
                if (tips.find('#') != -1):
                    tips = HTMLParser.HTMLParser().unescape(tips)
            
            if 'cover_image' in document:
                cover_image = document['cover_image']
                if cover_image != '':
                    cover_image = image_url + cover_image
                    
            if 'image' in document:
                image = document['image']
                if image != None and len(image) > 0:
                    for i in range(len(image)):
                        image[i] = image_url + image[i]
            
            if 'city_id' in document:
                temp_city = travel1['latestcity'].find_one({'_id':document['city_id']})
                if temp_city is not None:
                    if 'shoplabels' in temp_city:
                        shoplabels = temp_city['shoplabels']
                        if shoplabels is not None and len(shoplabels) > 0:
                            for i in range(len(shoplabels)):
                                temp_label = {}
                                temp_label.update({'id': ObjectId(shoplabels[i]['_id'])})
                                temp_label.update({'label': shoplabels[i]['title'] })
                                master_label.append(temp_label)
            
            if 'category' in document:
                category = document['category']
                for i in range(len(category)):
                    if category != None:
                        if '_id' in category[i]:
                            _id = category[i]['_id']
                        if 'name' in category[i]:
                            tag = category[i]['name']
                        temp_sub_tag = {}
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
                        if '_id' in brand[i]:
                            brand_id = brand[i]['_id']
                            db_brand = travel2['brand'].find_one({'_id': ObjectId(brand_id)})
                            if db_brand != None:
                                if db_brand['cover_image'] != '' and db_brand['cover_image'] != None:
                                    brand_cover_image = image_url + db_brand['cover_image']
                                title = db_brand['title']
                                desc = db_brand['desc']
                                advice = db_brand['advice']
                        
                        temp_brand = {}
                        temp_brand.update({'_id': brand_id, 'cover_image': brand_cover_image, 'title': title,
                                          'desc': desc, 'advice': advice, 'tag': ''})
                        new_brand.append(temp_brand)
            
            
            if 'comments' in document:
                comments = document['comments']
                for i in range(len(comments)):
                    if type(comments[i]) == unicode:
                        temp_comments = {}
                        temp_comments.update({'date': datetime.datetime(1970,1,1),'rating': rating,'nickname': nickname,
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
                                    new_date = datetime.datetime(1970,1,1)
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
                          'master_label': master_label, 'is_show': is_show, 'comments': new_comments,
                          'cover_image': cover_image, 'image': image, 'price_level': price_level,
                          'activities': activities, 'introduction':introduction, 'brief_introduction': brief_introduction, 'tips': tips,
                          'brand': new_brand, 'last_modified_person': '', 'last_modified_time': datetime.datetime(1970,1,1)})

            post = {}
            post.update(other)
            for i in range(len(params_map.keys())):
                post.update({params_map.values()[i]: temp[i]})
            db_new.insert(post)
            print post

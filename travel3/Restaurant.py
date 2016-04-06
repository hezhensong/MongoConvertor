#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import HTMLParser
import datetime

import pytz
from bson import ObjectId
from pymongo import MongoClient
from idlelib.ReplaceDialog import replace


class Restaurant:
    def __init__(self):
        pass

    @staticmethod
    def convert_restaurant(address_old, port_old, address_new, port_new):

        # old database connection
        client = MongoClient(address_old, port_old)
        travel1 = client.travel1

        # new database connection
        client = MongoClient(address_new, port_new)
        travel3 = client.travel3

        # get old collection and create new collection
        restaurant_old = travel1.restaurants
        restaurant_new = travel3.restaurant

        # clean former data
        restaurant_new.remove()

        for restuarant_temp in restaurant_old.find():
            # 字段数少于10的直接跳过
            if(len(restuarant_temp) <= 10):
                continue
            
            print restuarant_temp['_id']
            post = {'_id': restuarant_temp['_id']}
            
            # 中文名、英文名都没有，当做脏数据删除
            if 'name' not in restuarant_temp and 'name_en' not in restuarant_temp:
                print "脏数据: ", post['_id']
                continue
        
            # 中文名
            if 'name' in restuarant_temp:
                post['name'] = restuarant_temp['name']
            else:
                post['name'] = ''

            # 英文名
            if 'name_en' in restuarant_temp:
                post['name_en'] = restuarant_temp['name_en']
            else:
                post['name_en'] = ''
            
             # 是否线上展示
            if 'show_flag' in restuarant_temp:
                show_flag = restuarant_temp['show_flag']
                if show_flag == u'1':
                    post['is_show'] = True
                else:
                    post['is_show'] = False
            else:
                post['is_show'] = False

            # 是否已经删除
            post['is_delete'] = False
            
            # city id
            if 'city_id' in restuarant_temp:
                post['city_id'] = restuarant_temp['city_id']
            else:
                post['city_id'] = None

            # city name
            if 'city_name' in restuarant_temp:
                post['city_name'] = restuarant_temp['city_name']
            else:
                post['city_name'] = ''
                
            # Google Place ID
            if 'googleId' in restuarant_temp:
                post['google_place_id'] = restuarant_temp['googleId']
            else:
                post['google_place_id'] = ''
                
            # 新增字段：排序, 与 ranking 的关系, 待定
#            post['order'] = 0.0

            # 景点详情页轮播图
            post['image'] = []
            image_url = 'http://weegotest.b0.upaiyun.com/restaurant/iosimgs/'

            
            if 'image' in restuarant_temp:
                image_list = restuarant_temp['image']

                # 遍历找背景图,use 标记为 cover
                if 'cover_image' in restuarant_temp:
                    cover_image = restuarant_temp['cover_image']

                for image_item in image_list:
                    if image_item == cover_image:
                        image_element = {
                            'url': image_url + image_item,
                            'use': 'cover'
                        }
                    else:
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
            if 'address' in restuarant_temp:
                post['address_detail'] = restuarant_temp['address']
            else:
                post['address_detail'] = ''

            # 经纬度
            if 'longitude' in restuarant_temp and 'latitude' in restuarant_temp:
                longitude = str(restuarant_temp['longitude'])
                latitude = str(restuarant_temp['latitude'])
                post['coordinate'] = longitude.strip() + ',' + latitude.strip()
            else:
                post['coordinate'] = ''
            
             # 价格描述
            if 'price_desc' in restuarant_temp:
                if restuarant_temp['price_desc'] != 'null':
                    post['price_desc'] = str(restuarant_temp['price_desc'])
                else:
                    post['price_desc'] = ''
            else:
                post['price_desc'] = ''
            
            # 价格等级,有字符串类型的脏数据
            if 'price_level' in restuarant_temp:
                price_level = restuarant_temp['price_level']
                if type(price_level) == str or type(price_level) == unicode:
                    price_level = 1
                if price_level == 5:
                    price_level = 4
                post['price_level'] = price_level
            else:
                post['price_level'] = int(-1)
                
            # 营业时间
            if 'open_time' in restuarant_temp:
                post['open_time'] = restuarant_temp['open_time']
            else:
                post['open_time'] = []
            
            # 营业时间描述
            post['open_time_desc'] = ''
            # 交通信息
            post['traffic_info'] = ''
            
            # 网址
            if 'website' in restuarant_temp:
                post['website'] = restuarant_temp['website']
            else:
                post['website'] = ''

            # 电话
            if 'tel' in restuarant_temp:
                post['telephone'] = restuarant_temp['tel']
            else:
                post['telephone'] = ''
            
            # 建议游览时长,可能为空串、int类型 或 字符串类型
            if 'recommand_duration' in restuarant_temp:
                if type(restuarant_temp['recommand_duration']) == int:
                    post['recommend_duration'] = restuarant_temp['recommand_duration']
                elif len(restuarant_temp['recommand_duration']) > 0:
                    post['recommend_duration'] = int(restuarant_temp['recommand_duration'])
                else:
                    post['recommend_duration'] = int(0)
            else:
                post['recommend_duration'] = int(0)
                
            # 一句话简介
            if 'brief_introduce' in restuarant_temp:
                brief_introduction_temp = HTMLParser.HTMLParser().unescape(restuarant_temp['brief_introduce'])
                post['brief_introduction'] = brief_introduction_temp\
                    .replace('<p>','').replace('</p>','').replace('<br/>','')\
                    .replace('<span>','').replace('</span>','')
            else:
                post['brief_introduction'] = ''
                
            # 简介
            if 'introduce' in restuarant_temp:
                introduction_temp = HTMLParser.HTMLParser().unescape(restuarant_temp['introduce'])
                post['introduction'] = introduction_temp\
                    .replace('<p>','').replace('</p>','').replace('<br/>','')\
                    .replace('<span>','').replace('</span>','')
            else:
                post['introduction'] = ''
                
            # 小贴士
            if 'tips' in restuarant_temp:
                tips_temp = HTMLParser.HTMLParser().unescape(restuarant_temp['tips'])
                post['tips'] = tips_temp\
                    .replace('<p>','').replace('</p>','').replace('<br/>','')\
                    .replace('<span>','').replace('</span>','')
            else:
                post['tips'] = ''
                
            # 预定来源
            post['book_source'] = ''

            # 预订URL
            if 'openTable_url' in restuarant_temp:
                post['book_url'] = restuarant_temp['openTable_url']
            else:
                post['book_url'] = ''
                
            # 总评分
            if 'rating' in restuarant_temp:
                if restuarant_temp['rating'] != None:
                    post['rating'] = float(restuarant_temp['rating'])
                else:
                    post['rating'] = 0.0
            else:
                post['rating'] = 0.0
            
            label = []
            # 类别标签 label 的第一部分
            if 'city_id' in restuarant_temp:
                temp_city = travel1['latestcity'].find_one({'_id':restuarant_temp['city_id']})
                if temp_city is not None:
                    if 'reslabels' in temp_city:
                        reslabels = temp_city['reslabels']
                        if reslabels is not None and len(reslabels) > 0:
                            for i in range(len(reslabels)):
                                temp_label = {}
                                temp_label.update({'_id': ObjectId(reslabels[i]['_id'])})
                                temp_label.update({'name': reslabels[i]['title'] })
                                label.append(temp_label)
                                
            # 类别标签 label 的第二部分
            if 'tags_zh' in restuarant_temp:
                tags_zh = restuarant_temp['tags_zh']
                if tags_zh is not None and len(tags_zh) > 0:
                    for i in range(len(tags_zh)):
                        temp_label = {}
                        temp_label.update({'_id': ''})
                        temp_label.update({'name': tags_zh[i] })
                        label.append(temp_label)
            post['label'] = label
            
            tag = []
            # 属性标签
            if 'category' in restuarant_temp:
                category = restuarant_temp['category']                
                for i in range(len(category)):
                    if category is not None:
                        if '_id' in category[i]:
                            _id = category[i]['_id']
                        if 'name' in category[i]:
                            tag_name = category[i]['name']
                        temp_sub_tag = {}
                        temp_sub_tag.update({'_id': _id, 'tag': tag_name})
                        tag.append(temp_sub_tag)
            post['tag'] = tag
            
            # 评论来源
            if 'comments_from' in restuarant_temp:
                post['comments_from'] = restuarant_temp['comments_from']
            else:
                post['comments_from'] = ''

            # 评论URL
            if 'comments_url' in restuarant_temp:
                post['comments_url'] = restuarant_temp['comments_url']
            else:
                post['comments_url'] = ''
                
            # yelp网址
            if 'url' in restuarant_temp:
                post['yelp_url'] = restuarant_temp['url']
            else:
                post['yelp_url'] = ''
            
            # 评论,有些评论是只有 text 的脏数据
            new_comments = []
            date = ''
            rating = 0.0
            nickname = ''
            text = ''
            title = ''
            language = 'zh'
            if 'comments' in restuarant_temp:
                comments = restuarant_temp['comments']
                for i in range(len(comments)):
                    if type(comments[i]) == unicode or type(comments[i]) == str:
                        break
                        
                    else:
                        if comments != [None]:
                            if 'date' in comments[i]:
                                date = comments[i]['date']
                            if 'rating' in comments[i]:
                                rating = float(comments[i]['rating'])
                            if 'nickname' in comments[i]:
                                nickname = comments[i]['nickname']
                            if 'text' in comments[i]:
                                text = comments[i]['text']
                            if 'title' in comments[i]:
                                title = comments[i]['title']
                            if 'language' in comments[i]:
                                language = comments[i]['language']
                            temp_comments = {}
                            temp_comments.update({'date': date,'rating': rating,'nickname': 
                                                  nickname,'text': text, 'title': title, 'language': language})
                            new_comments.append(temp_comments)         
            post['comments'] = new_comments
            
            # 菜品
            new_dish = []
            dish_cover_image = ''
            desc = ''
            if 'menu' in restuarant_temp:
                dish = restuarant_temp['menu']
                for i in range(len(dish)):
                    if 'cover_image' in dish[i]:
                        if dish[i]['cover_image'] != '':
                            dish_cover_image = image_url + dish[i]['cover_image']
                    if 'desc' in dish[i]:
                        desc = dish[i]['desc']
                    if 'advice' in dish[i]:
                        advice = dish[i]['advice']
                    
                    dish_id = travel3['dish'].find_one({'cover_image': dish_cover_image,'desc': desc})['_id']
                    temp_dish = {}
                    temp_dish.update({'_id': dish_id, 'cover_image': dish_cover_image, 'desc':desc,
                                      'advice': advice, 'title': '', 'tag': ''})
                    new_dish.append(temp_dish)
            post['dish'] = new_dish
            
            # 设施 
            alcohol = ''
            noise = ''
            waiter = False
            tv = False
            outseat = False 
            group = False
            kid = False
            card = False
            takeout = False
            delivery = False
            reserve = False
            wifi = False
            facilities = {}
            if 'info' in restuarant_temp:
                temp_facilities = restuarant_temp['info']
                if 'alcohol' in temp_facilities:
                    alcohol = temp_facilities['alcohol']
                if 'noise' in temp_facilities:
                    noise = temp_facilities['noise']
                if 'waiter' in temp_facilities:
                    waiter = temp_facilities['waiter']
                if 'tv' in temp_facilities:
                    tv = temp_facilities['tv']
                if 'out_seat' in temp_facilities:
                    outseat = temp_facilities['out_seat'] 
                if 'g_f_group' in temp_facilities:
                    group = temp_facilities['g_f_group']
                if 'g_f_kid' in temp_facilities:
                    kid = temp_facilities['g_f_kid']
                if 'card' in temp_facilities:
                    card = temp_facilities['card']
                if 'take_out' in temp_facilities:
                    takeout = temp_facilities['take_out']
                if 'delivery' in temp_facilities:
                    delivery = temp_facilities['delivery']
                if 'yu_ding' in temp_facilities:
                    reserve = temp_facilities['yu_ding']
                if 'wifi' in temp_facilities:
                    wifi = temp_facilities['wifi']
                
            facilities.update({'alcohol': alcohol, 'noise': noise, 'waiter': waiter,
                               'tv': tv, 'outseat': outseat, 'group': group, 'kid': kid,
                               'card': card, 'takeout': takeout, 'delivery': delivery,
                               'reserve': reserve, 'wifi': wifi})
            post['facilities'] = facilities
                
            # 最后修改记录
            post['last_modified_person'] = ''
            post['last_modified_time'] = datetime.datetime(2016, 4, 6, 0, 0, 0, tzinfo=pytz.utc)

            # 插入数据库
            restaurant_new.insert(post)
            print(post)
           

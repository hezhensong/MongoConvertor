#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import HTMLParser
import datetime

import pytz
from bson import ObjectId
from pymongo import MongoClient
from idlelib.ReplaceDialog import replace


class Shopping:
    def __init__(self):
        pass

    @staticmethod
    def convert_shopping(address_old, port_old, address_new, port_new):

        # old database connection
        client = MongoClient(address_old, port_old)
        travel1 = client.travel1

        # new database connection
        client = MongoClient(address_new, port_new)
        travel3 = client.travel3

        # get old collection and create new collection
        shopping_old = travel1.shoppings
        shopping_new = travel3.shopping

        # clean former data
        shopping_new.remove()

        for shopping_temp in shopping_old.find():
            print shopping_temp['_id']
            post = {'_id': shopping_temp['_id']}
            
            # 中文名、英文名都没有,当做脏数据删除
            if 'name' not in shopping_temp and 'name_en' not in shopping_temp:
                print "脏数据: ", post['_id']
                continue
        
            # 中文名
            if 'name' in shopping_temp:
                post['name'] = shopping_temp['name']
            else:
                post['name'] = ''
                
            # 英文名
            if 'name_en' in shopping_temp:
                post['name_en'] = shopping_temp['name_en']
            else:
                post['name_en'] = ''
            
            # 是否线上展示
            if 'show_flag' in shopping_temp:
                show_flag = shopping_temp['show_flag']
                if show_flag == u'1':
                    post['is_show'] = True
                else:
                    post['is_show'] = False
            else:
                post['is_show'] = False

            # 是否已经删除
            post['is_delete'] = False
            
            # city id
            if 'city_id' in shopping_temp:
                post['city_id'] = shopping_temp['city_id']
            else:
                post['city_id'] = None

            # city name
            if 'city_name' in shopping_temp:
                post['city_name'] = shopping_temp['city_name']
            else:
                post['city_name'] = ''
                
            # Google Place ID
            if 'googleId' in shopping_temp:
                post['google_place_id'] = shopping_temp['googleId']
            else:
                post['google_place_id'] = ''
                
             # 景点详情页轮播图
            post['image'] = []
            image_url = 'http://weegotest.b0.upaiyun.com/shopping/iosimgs/'

            
            if 'image' in shopping_temp:
                image_list = shopping_temp['image']

                # 遍历找背景图,use 标记为 cover
                if 'cover_image' in shopping_temp:
                    cover_image = shopping_temp['cover_image']

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
            if 'address' in shopping_temp:
                post['address_detail'] = shopping_temp['address']
            else:
                post['address_detail'] = ''
                
                
            # 经纬度
            if 'longitude' in shopping_temp and 'latitude' in shopping_temp:
                longitude = str(shopping_temp['longitude'])
                latitude = str(shopping_temp['latitude'])
                post['coordinate'] = longitude.strip() + ',' + latitude.strip()
            else:
                post['coordinate'] = ''
            
             # 价格描述
            if 'price_desc' in shopping_temp:
                if shopping_temp['price_desc'] != 'null':
                    post['price_desc'] = str(shopping_temp['price_desc'])
                else:
                    post['price_desc'] = ''
            else:
                post['price_desc'] = ''
            
            # 价格等级,有字符串类型的脏数据
            if 'price_level' in shopping_temp:
                price_level = shopping_temp['price_level']
                if type(price_level) == str or type(price_level) == unicode:
                    price_level = 1
                if price_level == 5:
                    price_level = 4
                post['price_level'] = price_level
            else:
                post['price_level'] = int(-1)
                
            # 营业时间
            if 'open_time' in shopping_temp:
                post['open_time'] = shopping_temp['open_time']
            else:
                post['open_time'] = []
            
            # 营业时间描述
            post['open_time_desc'] = ''
            # 交通信息
            post['traffic_info'] = ''
            
            # 网址
            if 'website' in shopping_temp:
                post['website'] = shopping_temp['website']
            else:
                post['website'] = ''

            # 电话
            if 'tel' in shopping_temp:
                post['telephone'] = shopping_temp['tel']
            else:
                post['telephone'] = ''
                
            # 建议游览时长,可能为空串、int类型 或 字符串类型
            if 'recommand_duration' in shopping_temp:
                if type(shopping_temp['recommand_duration']) == int:
                    post['recommend_duration'] = shopping_temp['recommand_duration']
                elif len(shopping_temp['recommand_duration']) > 0:
                    post['recommend_duration'] = int(shopping_temp['recommand_duration'])
                else:
                    post['recommend_duration'] = int(0)
            else:
                post['recommend_duration'] = int(0)
                
             # 一句话简介
            if 'brief_introduce' in shopping_temp:
                brief_introduction_temp = HTMLParser.HTMLParser().unescape(shopping_temp['brief_introduce'])
                post['brief_introduction'] = brief_introduction_temp\
                    .replace('<p>','').replace('</p>','').replace('<br/>','')\
                    .replace('<span>','').replace('</span>','')
            else:
                post['brief_introduction'] = ''
                
            # 简介
            if 'introduce' in shopping_temp:
                introduction_temp = HTMLParser.HTMLParser().unescape(shopping_temp['introduce'])
                post['introduction'] = introduction_temp\
                    .replace('<p>','').replace('</p>','').replace('<br/>','')\
                    .replace('<span>','').replace('</span>','')
            else:
                post['introduction'] = ''
                
            # 小贴士
            if 'tips' in shopping_temp:
                tips_temp = HTMLParser.HTMLParser().unescape(shopping_temp['tips'])
                post['tips'] = tips_temp\
                    .replace('<p>','').replace('</p>','').replace('<br/>','')\
                    .replace('<span>','').replace('</span>','')
            else:
                post['tips'] = ''
                
            # 预定来源
            post['book_source'] = ''

            # 预订URL
            post['book_url'] = ''
                
            # 总评分
            if 'rating' in shopping_temp:
                if shopping_temp['rating'] != None:
                    post['rating'] = float(shopping_temp['rating'])
                else:
                    post['rating'] = 0.0
            else:
                post['rating'] = 0.0
            
            # 类别 标签 label
            label = []
            if 'city_id' in shopping_temp:
                temp_city = travel1['latestcity'].find_one({'_id':shopping_temp['city_id']})
                if temp_city is not None:
                    if 'shoplabels' in temp_city:
                        shoplabels = temp_city['shoplabels']
                        if shoplabels is not None and len(shoplabels) > 0:
                            for i in range(len(shoplabels)):
                                temp_label = {}
                                temp_label.update({'_id': ObjectId(shoplabels[i]['_id'])})
                                temp_label.update({'name': shoplabels[i]['title'] })
                                label.append(temp_label)
            post['label'] = label
            
            # 属性标签 tag
            new_tag = []
            if 'category' in shopping_temp:
                category = shopping_temp['category']
                for i in range(len(category)):
                    if category != None:
                        if '_id' in category[i]:
                            _id = category[i]['_id']
                        if 'name' in category[i]:
                            tag = category[i]['name']
                        temp_sub_tag = {}
                        temp_sub_tag.update({'_id': _id, 'tag': tag})
                        new_tag.append(temp_sub_tag)
            post['tag'] = tag
            
            # 评论来源
            if 'comments_from' in shopping_temp:
                post['comments_from'] = shopping_temp['comments_from']
            else:
                post['comments_from'] = ''

            # 评论URL
            if 'comments_url' in shopping_temp:
                post['comments_url'] = shopping_temp['comments_url']
            else:
                post['comments_url'] = ''
                
            # yelp网址
            if 'url' in shopping_temp:
                post['yelp_url'] = shopping_temp['url']
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
            if 'comments' in shopping_temp:
                comments = shopping_temp['comments']
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
            
            # 品牌,图片的全路径待定
            new_brand = []
            if 'brand' in shopping_temp:
                brand = shopping_temp['brand']
                if brand != None:
                    for i in range(len(brand)):
                        if '_id' in brand[i]:
                            brand_id = brand[i]['_id']
                            db_brand = travel3['brands'].find_one({'_id': ObjectId(brand_id)})
                            if db_brand != None:
                                if db_brand['cover_image'] != '' and db_brand['cover_image'] != None:
                                    brand_cover_image = db_brand['cover_image']
                                title = db_brand['title']
                                desc = db_brand['desc']
                                advice = db_brand['advice']
                        temp_brand = {}
                        temp_brand.update({'_id': brand_id, 'cover_image': brand_cover_image, 'title': title,
                                          'desc': desc, 'advice': advice, 'tag': ''})
                        new_brand.append(temp_brand)
            post['brand'] = new_brand
            
            # 最后修改记录
            post['last_modified_person'] = ''
            post['last_modified_time'] = datetime.datetime(2016, 4, 6, 0, 0, 0, tzinfo=pytz.utc)

            # 插入数据库
            shopping_new.insert(post)
            print post
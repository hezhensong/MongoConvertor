#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient
import datetime
import HTMLParser

class Restaurant:
    def __init__(self):
        pass

    collection_old = 'restaurants'

    collection_new = 'restaurant'
    
    params_map = {'_id':'_id', # 餐厅ID
                  'address': 'address', # 餐厅地址地址
                  'name': 'name', # 餐厅名
                  'name_en': 'name_en', # 餐厅英文名
                  'city_id': 'city_id', # 城市 ID
                  'city_name': 'city_name', # 城市名
                  'comments_from': 'comments_from', # 评论来源
                  'comments_url': 'comments_url', # 评论 url
                  'price_desc': 'price_desc', # 价格描述
                  'tel': 'tel', # 电话
                  'website': 'website', # 网站
                  'rating': 'rating', # 评分
                  'openTable_url':'open_table_url'  # 服务预订 url
    }

    @staticmethod
    def convert_restaurant(address_old, port_old, address_new, port_new, collection_old, collection_new,
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

            # 需要特殊处理的字段,处理后以字典的形式添加到 other 中
            coordination = ''
            latitude = ''
            longitude = ''
            open_time = []
            cover_image = ''
            dish_cover_image = ''
            image = []
            image_url = 'http://weegotest.b0.upaiyun.com/restaurant/iosimgs/'
            title = ''
            desc = ''
            advice = ''
            newdish = []
            dish_id = ''
            facilities = {}
            activities = []
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
            introduction = ''
            brief_introduction = ''
            tips = ''
            price_level = 1
            
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
                if (introduction.find('&') != -1):
                    introduction = HTMLParser.HTMLParser().unescape(introduction)
                    
            if 'brief_introduce' in document:
                brief_introduction = document['brief_introduce']
                if (brief_introduction.find('&') != -1):
                    brief_introduction = HTMLParser.HTMLParser().unescape(brief_introduction)
            
            if 'tips' in document:
                tips = document['tips']
                if (tips.find('&') != -1):
                    tips = HTMLParser.HTMLParser().unescape(tips)
            
            if 'cover_image' in document:
                cover_image = document['cover_image']
                if cover_image != '':
                    cover_image = image_url + cover_image
                    
            if 'image' in document:
                image = document['image']
                if image is not None and len(image) > 0:
                    for i in range(len(image)):
                        image[i] = image_url + image[i]
            
            if 'category' in document:
                category = document['category']
                if len(category) > 0:
                    master_tag.update({'_id': '','label': ''})
                
                for i in range(len(category)):
                    if category is not None:
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

            if 'comments' in document:
                comments = document['comments']
                for i in range(len(comments)):
                    if type(comments[i]) == unicode:
                        temp_comments = {}
                        temp_comments.update({'date': datetime.datetime(1970,1,1),'rating': rating,'nickname': nickname,
                                              'language': language, 'text': comments[i], 'title': title})
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
                            if 'language' in comments[i]:
                                language = comments[i]['language']
                            temp_comments = {}
                            temp_comments.update({'date': new_date,'rating': rating,'nickname': 
                                                  nickname,'text': text, 'title': title, 'language': language})
                            new_comments.append(temp_comments)
            
            if 'menu' in document:
                dish = document['menu']
                for i in range(len(dish)):
                    if 'cover_image' in dish[i]:
                        if dish[i]['cover_image'] != '':
                            dish_cover_image = image_url + dish[i]['cover_image']
                    desc = dish[i]['desc']
                    advice = dish[i]['advice']
                    
                    dish_id = travel2['dish'].find_one({'cover_image': dish_cover_image,
                                              'desc': desc, 'advice': advice})['_id']
                    
                    print(dish_id)
                    temp_dish = {}
                    temp_dish.update({'_id': dish_id, 'cover_image':dish_cover_image, 'desc':desc,
                                      'advice': advice, 'title': title, 'tag': ''})
                    newdish.append(temp_dish)
            
            if 'info' in document:
                temp_facilities = document['info']
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
                
            # 是否线上展示
            if 'show_flag' in document:
                show_flag = document['show_flag']
                if show_flag == u'1':
                    is_show = True
                else:
                    is_show = False
            else:
                is_show = False
            
            other.update({'coordination': coordination , 'open_time': open_time,
                          'dish': newdish, 'facilities': facilities,'comments': new_comments,
                          'cover_image': cover_image, 'image': image, 'price_level': price_level,
                          'introduction':introduction, 'brief_introduction': brief_introduction, 'tips': tips,
                          'master_label': master_tag, 'sub_tag': sub_tag, 'is_show': is_show,
                          'activities': activities, 'last_modified_person': '', 'last_modified_time': ''})
            
            post = {}      
            post.update(other)
            for i in range(len(params_map.keys())):
                post.update({params_map.values()[i]:temp[i]})
            db_new.insert(post)
            print post

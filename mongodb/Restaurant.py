#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId
from ConvertUtil import ConvertUtil

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
        travel2 = client.travel2

        # old collection latest city
        restaurant = travel1.restaurants
        restaurant_new = travel2.restaurant

        # clean former data
        restaurant_new.remove()

        address  = None
        brief_introduce = None
        city_id = None
        city_name = None
        comments = None
        comments_from = None
        cover_image = None
        create_at = None
        image = None
        image_url = None
        info = None
        introduce = None
        latitude = None
        longitude = None
        menu = None
        name = None 
        openTable_url = None
        open_time = None
        price_desc = None
        ranking = None
        rating = None
        tags = None
        tags_zh = None
        tel = None
        tips = None
        website = None
        
        for restaurant_old in restaurant.find():
            _id = restaurant_old['_id']
            print(_id)
            if 'address' in restaurant_old:
                address = restaurant_old['address']
            if 'brief_introduce' in restaurant_old:
                brief_introduce = restaurant_old['brief_introduce']
            if 'city_id' in restaurant_old:
                city_id = restaurant_old['city_id']
            if 'city_name' in restaurant_old:
                city_name = restaurant_old['city_name']
            if 'comments' in restaurant_old:
                comments = restaurant_old['comments']
            if 'comments_from' in restaurant_old:
                comments_from = restaurant_old['comments_from']
            if 'cover_image' in restaurant_old:
                cover_image = restaurant_old['cover_image']
            if 'create_at' in restaurant_old:
                create_at = restaurant_old['create_at']
            if 'image' in restaurant_old:
                image = restaurant_old['image']
            if 'image_url' in restaurant_old:
                image_url = restaurant_old['image_url']
            if 'info' in restaurant_old:
                info = restaurant_old['info']
            if 'introduce' in restaurant_old:
                introduce = restaurant_old['introduce']
            if 'latitude' in restaurant_old:
                latitude = restaurant_old['latitude']
            if 'longitude' in restaurant_old:
                longitude = restaurant_old['longitude']
            if 'menu' in restaurant_old:
                menu = restaurant_old['menu']
            if 'name' in restaurant_old:
                name = restaurant_old['name']
            if 'openTable_url' in restaurant_old:
                openTable_url = restaurant_old['openTable_url']
            if 'open_time' in restaurant_old:
                open_time = restaurant_old['open_time']
            if 'price_desc' in restaurant_old:
                price_desc = restaurant_old['price_desc']
            if 'ranking' in restaurant_old:
                ranking = restaurant_old['ranking']
            if 'rating' in restaurant_old:
                rating = restaurant_old['rating']
            if 'tags' in restaurant_old:
                tags = restaurant_old['tags']
            if 'tags_zh' in restaurant_old:
                tags_zh = restaurant_old['tags_zh']
            if 'tel' in restaurant_old:
                tel = restaurant_old['tel']
            if 'tips' in restaurant_old:
                tips = restaurant_old['tips']
            if 'website' in restaurant_old:
                website = restaurant_old['website']

            post = {
                '_id': _id, # 餐厅ID
                'address': address, # 餐厅地址
                'brief_introduce': brief_introduce, # 餐厅简介
                'city_id': city_id, # 城市ID
                'city_name': city_name, # 城市名字
                'comments': comments, # 评论
                'comments_from': comments_from, # 评论来源
                'cover_image': cover_image, # 封面图片
                'create_at': create_at, # 创建时间
                'image': image, # 图片
                'image_url': image_url, # 图片 url
                'info': info, # 餐厅的相关信息
                'introduce': introduce, # 餐厅详细介绍
                'latitude': latitude, # 纬度
                'longitude': longitude, # 经度
                'menu': menu, # 菜品推荐
                'name': name, # 餐厅名字
                'openTable_url': openTable_url, # 服务预订 url
                'open_time': open_time, # 开放时间
                'price_desc': price_desc, # 价格描述
                'ranking': ranking, # 排行
                'rating': rating, # 评分 
                'tags': tags, # 标签
                'tags_zh': tags_zh, # 中文标签
                'tel': tel, # 电话
                'tips': tips, # 提示
                'website': website # 网址
            }
            result = restaurant_new.insert(post)
            print post
            print result

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from pymongo import MongoClient


class ChangeId:
    def __init__(self):
        pass

    @staticmethod
    def update_city_id(address, port):
        
        client = MongoClient(address, port)
        travel1 = client.travel1
        
        city = travel1.latestcity
        attraction = travel1.latestattractions
        restaurant = travel1.restaurants 
        shopping = travel1.shoppings
        area = travel1.areas
        
        cityNames = ['大阪','京都','澳门','首尔','台北','香港','东京']
        # 景点表 
        for temp_attraction in attraction.find():
            if 'cityname' in temp_attraction:
                city_name = temp_attraction['cityname']
                if city_name in cityNames:
                    print(temp_attraction['_id'])
                    temp_city = city.find_one({'cityname': city_name})
                    attraction.update({'_id': temp_attraction['_id'] }, {'$set':{'city_id': temp_city['_id'],
                                                                                 'cityid': temp_city['_id']}}) 
            else:
                continue
        print("attraction is ok")
                
        # 餐厅表 
        for temp_restaurant in restaurant.find():
            if 'city_name' in temp_restaurant:
                city_name = temp_restaurant['city_name']
                if city_name in cityNames:
                    print(temp_restaurant['_id'])
                    temp_city = city.find_one({'cityname': city_name})
                    restaurant.update({'_id': temp_restaurant['_id'] }, {'$set':{'city_id': temp_city['_id']}}) 
            else:
                continue
        print("restaurant is ok")
        
        # 购物表
        for temp_shopping in shopping.find():
            if 'city_name' in temp_shopping:
                city_name = temp_shopping['city_name']
                if city_name in cityNames:
                    print(temp_shopping['_id'])
                    temp_city = city.find_one({'cityname': city_name})
                    shopping.update({'_id': temp_shopping['_id'] }, {'$set':{'city_id': temp_city['_id']}}) 
            else:
                continue
        print("shopping is ok")
        
         # 购物圈表
        for temp_area in area.find():
            if 'city_name' in temp_area:
                city_name = temp_area['city_name']
                if city_name in cityNames:
                    print(temp_area['_id'])
                    temp_city = city.find_one({'cityname': city_name})
                    area.update({'_id': temp_area['_id'] }, {'$set':{'city_id': temp_city['_id']}}) 
            else:
                continue
        print("area is ok")
        
        print("chang id is over")
        
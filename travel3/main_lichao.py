#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
from Restaurant import Restaurant
from Dish import Dish
from Shopping import Shopping
from Brands import Brands
from RecommendInfo import RecommendInfo

reload(sys)
sys.setdefaultencoding('utf8')

def main():
#    address_old = 'localhost'
    address_old = '192.168.199.254'
    port_old = 27017

#    address_new = 'localhost'
    address_new = '192.168.199.254'
    port_new = 27017
    
    # dish 表需要在 restaurant 表之前创建
    print('create dish')
#    Dish.create_dish(address_old, port_old, address_new, port_new)

    # restaurant 表的 dish 字段需要重新关联  dish 表的id
    print('convert restaurants to restaurant.')
#    Restaurant.convert_restaurant(address_old, port_old, address_new, port_new)
    
    # brands 表需要在 shopping 表之前创建
    print('convert travel1Brands to travel3Brands.')
#    Brands.convert_Brands(address_old, port_old, address_new, port_new)
    
    # restaurant 表的 brand 字段需要重新关联  brands 表的id
    print('convert shoppings to shopping')
#    Shopping.convert_shopping(address_old, port_old, address_new, port_new)
    
    print('convert recommend_info')
    RecommendInfo.convert_recommend_info(address_old, port_old, address_new, port_new)

    print("OK")

if __name__ == "__main__":
    main()

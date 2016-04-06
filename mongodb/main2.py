#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from Activity import Activity
from City import City
from Label import Label
from Pgc import Pgc
from Weather import Weather
from WeatherHistory import WeatherHistory
from Attraction import Attraction
from Restaurant import Restaurant
from Shopping import Shopping
from RecommendInfo import RecommendInfo
from Plan import Plan
from RecommendHistory import RecommendHistory
from LabelType import LabelType
from Brand import Brand
from Spot import Spot
from Dish import Dish
from Person import Person
from POILabelId import POILabelId

def main():
    address_old = 'localhost'
    port_old = 27017

    address_new = '123.56.65.17'
#    address_new = 'localhost'
    port_new = 27017


    print("convert label type data")
    LabelType.insert_label_type(address_new, port_new)

    print("convert weather data")
    Weather.convert_weather(address_old, port_old, address_new, port_new,
                            Weather.collection_old, Weather.collection_new, Weather.params_map)
    
    # 特别注意  weather_history 表依赖于当前的 weather 表
    print("create weather_history data")
    WeatherHistory.create_weather_history(address_new, port_new, address_new, port_new,
                            WeatherHistory.collection_old, WeatherHistory.collection_new, WeatherHistory.params_map)

    print("convert pgc data")
    Pgc.convert_pgc(address_old, port_old, address_new, port_new,
                              Pgc.collection_old, Pgc.collection_new, Pgc.params_map)
    
    print("convert person data")
    Person.convert_person(address_old, port_old, address_new, port_new)

    # 必须在  attraction 之前创建
    print("create spot data")
    Spot.create_spot(address_old, port_old, address_new, port_new,
                              Spot.collection_old, Spot.collection_new, Spot.params_map)

    # 必须在 restaurant 之前创建
    print("create dish data")
    Dish.create_dish(address_old, port_old, address_new, port_new,
                              Dish.collection_old, Dish.collection_new, Dish.params_map)
    # 必须在 shopping 之前创建
    print("convert brand data")
    Brand.convert_brand(address_old, port_old, address_new, port_new,
                              Brand.collection_old, Brand.collection_new, Brand.params_map)

    # label的  id 依赖于 label 表
    print("convert attraction data")
    Attraction.convert_attraction(address_old, port_old, address_new, port_new,
                                  Attraction.collection_old, Attraction.collection_new, Attraction.params_map)
    # label的  id 依赖于 label 表
    print("convert restaurant data")
    Restaurant.convert_restaurant(address_old, port_old, address_new, port_new,
                                  Restaurant.collection_old, Restaurant.collection_new, Restaurant.params_map)
    # label的  id 依赖于 label 表
    print("convert shopping data")
    Shopping.convert_shopping(address_old, port_old, address_new, port_new,
                              Shopping.collection_old, Shopping.collection_new, Shopping.params_map)
    
    # label 表依赖于 attraction、restaurant、shopping 表      
    print("convert label data")
    Label.convert_label(address_new, port_new)
    
    # 需 在 poi 表之后处理
    print("change poi label id")
    POILabelId.attraction_label(address_new, port_new)

    # 城市表 依赖新导入的Label表，需保证City前导入Label
    print("convert city data")
    City.convert_city(address_old, port_old, address_new, port_new)
    
    print("convert activity data")
    Activity.convert_activity(address_old, port_old, address_new, port_new,
                              Activity.collection_old, Activity.collection_new, Activity.params_map)

    print("convert recommendInfo data")
    RecommendInfo.convert_recommend_info(address_old, port_old, address_new, port_new,
                                           RecommendInfo.collection_old, RecommendInfo.collection_new, RecommendInfo.params_map)
    print("convert recommendHistory data")
    RecommendHistory.insert_recommend_history(address_new, port_new)
#
    print("convert plan data")
    Plan.convert_plan(address_old, port_old, address_new, port_new,
                      Plan.collection_old, Plan.collection_new, Plan.params_map)
    print("OK")


if __name__ == "__main__":
    main()

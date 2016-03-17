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
from RecommendDynamic import RecommendDynamic
from Plan import Plan
from LabelType import LabelType


def main():
    address_old = 'localhost'
    port_old = 27017

    address_new = '192.168.6.254'
#    address_new = 'localhost'
    port_new = 37017


    print("convert label type data")
#    LabelType.insert_label_type(address_new, port_new)

    print("convert label data")
#    Label.convert_label(address_old, port_old, address_new, port_new)

    # 城市表 依赖新导入的Label表，需保证City前导入Label
    print("convert city data")
#    City.convert_city(address_old, port_old, address_new, port_new)

    print("convert weather data")
    Weather.convert_weather(address_old, port_old, address_new, port_new,
                            Weather.collection_old, Weather.collection_new, Weather.params_map)
    
    # 特别注意  weather_history 表依赖于当前的 weather 表
    print("create weather_history data")
#    WeatherHistory.create_weather_history(address_new, port_new, address_new, port_new,
#                            WeatherHistory.collection_old, WeatherHistory.collection_new, WeatherHistory.params_map)

    print("convert pgc data")
#    Pgc.convert_pgc(address_old, port_old, address_new, port_new)

    print("convert label data")
#    Label.convert_label(address_old, port_old, address_new, port_new)

    print("convert attraction data")
#    Attraction.convert_attraction(address_old, port_old, address_new, port_new,
#                                  Attraction.collection_old, Attraction.collection_new, Attraction.params_map)

    print("convert restaurant data")
#    Restaurant.convert_restaurant(address_old, port_old, address_new, port_new,
#                                  Restaurant.collection_old, Restaurant.collection_new, Restaurant.params_map)

    print("convert shopping data")
#    Shopping.convert_shopping(address_old, port_old, address_new, port_new,
#                              Shopping.collection_old, Shopping.collection_new, Shopping.params_map)

    print("convert activity data")
#    Activity.convert_activity(address_old, port_old, address_new, port_new,
#                              Activity.collection_old, Activity.collection_new, Activity.params_map)

    print("convert recommendBynamic data")
#    RecommendDynamic.convert_recommendDynamic(address_old, port_old, address_new, port_new,RecommendDynamic.collection_old, 
#                               RecommendDynamic.collection_new, RecommendDynamic.params_map)

    print("convert plan data")
#    Plan.convert_plan(address_old, port_old, address_new, port_new,
#                      Plan.collection_old, Plan.collection_new, Plan.params_map)
    print("OK")


if __name__ == "__main__":
    main()

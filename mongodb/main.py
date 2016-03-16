#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from Activity import Activity
from City import City
from Label import Label
from Pgc import Pgc
from Weather import Weather
from Attraction import Attraction
from Restaurant import Restaurant
from Shopping import Shopping
from RecommendDynamic import RecommendDynamic
from Plan import Plan
from LabelType import LabelType


def main():
    address_old = '192.168.37.128'
    port_old = 27017
    address_new = '192.168.37.128'
    port_new = 27017

    print("convert label type data")
    LabelType.insert_label_type(address_new, port_new)

    print("convert label data")
    Label.convert_label(address_old, port_old, address_new, port_new)

    # 城市表 依赖新导入的Label表，需保证City前导入Label
    print("convert city data")
    City.convert_city(address_old, port_old, address_new, port_new)

    print("convert weather data")
    Weather.convert_weather(address_old, port_old, address_new, port_new,
                            Weather.database_old, Weather.database_new, Weather.params_map)

    print("convert pgc data")
    Pgc.convert_pgc(address_old, port_old, address_new, port_new)

    print("convert label data")
    Label.convert_label(address_old, port_old, address_new, port_new)

    print("convert attraction data")
    Attraction.convert_attraction(address_old, port_old, address_new, port_new,
                                  Attraction.database_old, Attraction.database_new, Attraction.params_map)

    print("convert restaurant data")
    Restaurant.convert_restaurant(address_old, port_old, address_new, port_new,
                                  Restaurant.database_old, Restaurant.database_new, Restaurant.params_map)

    print("convert shopping data")
    Shopping.convert_shopping(address_old, port_old, address_new, port_new,
                              Shopping.database_old, Shopping.database_new, Shopping.params_map)

    print("convert activity data")
    Activity.convert_activity(address_old, port_old, address_new, port_new,
                              Activity.database_old, Activity.database_new, Activity.params_map)

    print("convert recommendBynamic data")
    RecommendDynamic.convert_recommendDynamic(address_old, port_old, address_new, port_new,
                                              RecommendDynamic.database_old, RecommendDynamic.database_new,
                                              RecommendDynamic.params_map)

    print("convert plan data")
    Plan.convert_plan(address_old, port_old, address_new, port_new,
                      Plan.database_old, Plan.database_new, Plan.params_map)
    print("OK")


if __name__ == "__main__":
    main()

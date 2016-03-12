#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from Activity import Activity
from Attraction import Attraction
from City import City
from Label import Label
from Pgc import Pgc
from Weather import Weather
from Attraction import Attraction
from Restaurant import Restaurant
from Shopping import Shopping

def main():
    address_old = '123.56.65.17'
    port_old = 27017
    address_new = '192.168.6.254'
    port_new = 27017

    print("convert city data")
#    City.convert_city(address_old, port_old, address_new, port_new)

    print("convert weather data")
#    Weather.convert_weather(address_old, port_old, address_new, port_new)

    print("convert activity data")
#    Activity.convert_activity(address_old, port_old, address_new, port_new)

    print("convert pgc data")
#    Pgc.convert_pgc(address_old, port_old, address_new, port_new)

    print("convert label data")
#    Label.convert_label(address_old, port_old, address_new, port_new)

    print("convert attraction data")
#    Attraction.convert_attraction(address_old, port_old, address_new, port_new, 
#                                    Attraction.database_old, Attraction.database_new, Attraction.params_map)

    print("convert restaurant data")
#    Restaurant.convert_restaurant(address_old, port_old, address_new, port_new,
#                                  Restaurant.database_old,Restaurant.database_new, Restaurant.params_map)
    
    print("convert shopping data")
#    Shopping.convert_shopping(address_old, port_old, address_new, port_new,
#                              Shopping.database_old,Shopping.database_new,Shopping.params_map)

    print("convert activity data")
    Activity.convert_activity(address_old, port_old, address_new, port_new,
                              Activity.database_old,Activity.database_new,Activity.params_map)
   
    print("OK")

if __name__ == "__main__":
    main()

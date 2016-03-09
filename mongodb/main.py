#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from City import City
from Weather import Weather
from Activity import Activity
from Pgc import Pgc


def main():
    address_old = '123.56.65.17'
    port_old = 27017
 #   address_new = '114.215.102.190'
    address_new = '192.168.230.128'
    port_new = 27017

    # print("convert city data")
    # City.convert_city(address_old, port_old, address_new, port_new)
    #
    # print("convert weather data")
    # Weather.convert_weather(address_old, port_old, address_new, port_new)

    # print("convert activity data")
    # Activity.convert_activity(address_old, port_old, address_new, port_new)

    print("convert pgc data")
    Pgc.convert_pgc(address_old,port_old,address_new,port_new)


if __name__ == "__main__":
    main()

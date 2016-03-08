#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from City import City
from Weather import Weather
from Activity import Activity


def main():
    address_old = 'localhost'
    port_old = 27017
    address_new = '192.168.1.53'
    port_new = 27017

    print("convert city data")
    City.convert_city(address_old, port_old, address_new, port_new)

    print("convert weather data")
    Weather.convert_weather(address_old, port_old, address_new, port_new)

    print("convert activity data")
    Activity.convert_activity(address_old, port_old, address_new, port_new)


if __name__ == "__main__":
    main()

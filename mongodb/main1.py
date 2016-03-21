#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from WeatherTranslation import WeatherTranslation
from City import City


def main():
    address_old = '192.168.37.128'
    port_old = 27017

    address_new = '192.168.6.254'
    port_new = 37017

    # WeatherTranslation.insert_weather_translation(address_new, port_new)

    # 城市表 依赖新导入的Label表，需保证City前导入Label
    print("convert city data")
    City.convert_city(address_old, port_old, address_new, port_new)

    print("OK")


if __name__ == "__main__":
    main()

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from Area import Area
from Policy import Policy
from RecommendHistory import RecommendHistory
from WeatherTranslation import WeatherTranslation


# 插入新增数据，这部分数据不需要从老库导入
def main():
    address_old = '192.168.37.128'
    port_old = 27017

    address_new = '192.168.6.254'
    port_new = 37017

    # Area.insert_area(address_old, port_old, address_new, port_new)
    #
    # WeatherTranslation.insert_weather_translation(address_new, port_new)

    Policy.insert_policy(address_new, port_new)

    RecommendHistory.insert_recommend_history(address_new, port_new)

    print("OK")


if __name__ == "__main__":
    main()

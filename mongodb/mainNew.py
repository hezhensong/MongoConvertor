#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from Area import Area
from News import News
from Policy import Policy
from PolicyMap import PolicyMap
from WeatherTranslation import WeatherTranslation
from RecommendHistory import RecommendHistory


# 插入新增数据，这部分数据不需要从老库导入
def main():
    address_old = 'localhost'
    port_old = 27017

    address_new = '123.56.65.17'
    port_new = 27017

    Area.insert_area(address_old, port_old, address_new, port_new)
    
    WeatherTranslation.insert_weather_translation(address_new, port_new)

    Policy.insert_policy(address_new, port_new)

#    RecommendHistory.insert_recommend_history(address_new, port_new)

    PolicyMap.insert_policy_map(address_new, port_new)

    News.insert_news(address_new, port_new)

    print("OK")


if __name__ == "__main__":
    main()

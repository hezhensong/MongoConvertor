#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import pytz
import datetime
from bson.objectid import ObjectId


class TimeZoneUtil:
    timezoneMap = {
        ObjectId('516a34f958e3511036000001'): 'America/New_York',  # 纽约
        ObjectId('516a34f958e3511036000002'): 'Etc/GMT+8',  # 旧金山
        ObjectId('516a34f958e3511036000003'): 'America/Los_Angeles',  # 洛杉矶
        ObjectId('516a34fa58e3511036000004'): 'America/Chicago',  # 芝加哥
        ObjectId('516a34fa58e3511036000005'): 'Etc/GMT+5',  # 波士顿
        ObjectId('516a350ec221c21236000001'): 'America/Vancouver',  # 温哥华
        ObjectId('516a350ec221c21236000002'): 'America/Toronto',  # 多伦多
        ObjectId('516a350ec221c21236000003'): 'Europe/Paris',  # 巴黎
        ObjectId('516a350ec221c21236000004'): 'Etc/GMT-1',  # 里昂
        ObjectId('516a350fc221c21236000005'): 'Etc/GMT-1',  # 尼斯
        ObjectId('516a3519f8a6461636000001'): 'Etc/GMT-1',  # 威尼斯
        ObjectId('516a3519f8a6461636000002'): 'Europe/Madrid',  # 马德里
        ObjectId('516a3519f8a6461636000003'): 'Etc/GMT-1',  # 巴萨罗那
        ObjectId('516a3519f8a6461636000004'): 'Europe/Berlin',  # 柏林
        ObjectId('516a3519f8a6461636000005'): 'Etc/GMT-1',  # 法兰克福
        ObjectId('516a35208902ca1936000001'): 'Etc/GMT-1',  # 慕尼黑
        ObjectId('516a35218902ca1936000002'): 'Europe/Zurich',  # 苏黎世
        ObjectId('516a35218902ca1936000003'): 'Etc/GMT-1',  # 日内瓦
        ObjectId('516a35218902ca1936000004'): 'Europe/Amsterdam',  # 阿姆斯特丹
        ObjectId('516a35218902ca1936000005'): 'Europe/London',  # 伦敦
        ObjectId('516a352b625d8b1e36000001'): 'Etc/GMT+0',  # 曼彻斯特
        ObjectId('516a352b625d8b1e36000003'): 'Etc/GMT-9',  # 大阪
        ObjectId('516a352b625d8b1e36000005'): 'Asia/Seoul',  # 首尔（测试）
        ObjectId('516a3534dac6182136000001'): 'Etc/GMT-9',  # 釜山
        ObjectId('516a3535dac6182136000002'): 'Asia/Bangkok',  # 曼谷
        ObjectId('516a3535dac6182136000003'): 'Etc/GMT-7',  # 普吉岛
        ObjectId('516a3535dac6182136000004'): 'Asia/Singapore',  # 新加坡
        ObjectId('516a3535dac6182136000005'): 'Asia/Kuala_Lumpur',  # 吉隆坡
        ObjectId('516a35427dbbf72336000002'): 'Etc/GMT-8',  # 马尼拉
        ObjectId('516a35427dbbf72336000003'): 'Etc/GMT-8',  # 长滩岛
        ObjectId('51d3d238e98bbb566a000001'): 'Europe/Rome',  # 罗马
        ObjectId('52e0f1efb64f047135000003'): 'Australia/Sydney',  # 悉尼
        ObjectId('52e62f8e4e59f08771000009'): 'Etc/GMT+10',  # 欧胡岛
        ObjectId('530735c6d05b06507f000056'): 'Etc/GMT-9',  # 济州特别自治道
        ObjectId('53074df8d05b06507f00005e'): 'Asia/Dubai',  # 迪拜
        ObjectId('53077a0ed05b06507f000077'): 'America/Argentina/Buenos_Aires',  # 布宜诺斯艾利斯
        ObjectId('5307cf87d05b06507f000090'): 'Asia/Tel_Aviv',  # 特拉维夫
        ObjectId('5308cb32d05b06507f00009b'): 'America/Santiago',  # 圣地亚哥
        ObjectId('5308d35dd05b06507f0000a5'): 'Etc/GMT-2',  # 圣托里尼岛
        ObjectId('53845d836b36839c04000007'): 'Etc/GMT-8',  # 巴厘岛
        ObjectId('565fa92d18a1bf1a2b000046'): 'Hongkong',  # 香港
        ObjectId('565fa9cd18a1bf1a2b000048'): 'Asia/Macau',  # 澳门（测试）
        ObjectId('5698ae4730e3611971000024'): 'Asia/Seoul',  # 首尔
        ObjectId('5698bec74fb72baf67000001'): 'Asia/Macau',  # 澳门
        ObjectId('569c86a02fedc1e719000194'): 'Asia/Taipei',  # 台北
        ObjectId('569c8d062fedc1e7190001ad'): 'Asia/Tokyo',  # 东京
        ObjectId('569c95852fedc1e7190001ea'): 'Etc/GMT-9',  # 京都
    }

    def __init__(self):
        pass

    @staticmethod
    def gettimezone(cityId, year, month, day, hour, minute, second):
        zone = pytz.timezone(TimeZoneUtil.timezoneMap[cityId])
        return datetime.datetime(year, month, day, hour, minute, tzinfo=zone).astimezone(pytz.utc)

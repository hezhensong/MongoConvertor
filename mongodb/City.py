#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId
from TimeZoneUtil import TimeZoneUtil

class City:
    
    timezoneMap = {
                   ObjectId('516a34f958e3511036000001'):'GMT-5:00',     # 纽约
                   ObjectId('516a34f958e3511036000002'):'GMT-8:00',     # 旧金山  
                   ObjectId('516a34f958e3511036000003'):'GMT-8:00',     # 洛杉矶
                   ObjectId('516a34fa58e3511036000004'):'GMT-6:00',     # 芝加哥
                   ObjectId('516a34fa58e3511036000005'):'GMT-5:00',     # 波士顿   
                   ObjectId('516a350ec221c21236000001'):'GMT-8:00',     # 温哥华
                   ObjectId('516a350ec221c21236000002'):'GMT-5:00',     # 多伦多
                   ObjectId('516a350ec221c21236000003'):'GMT+1:00',     # 巴黎
                   ObjectId('516a350ec221c21236000004'):'GMT+1:00',     # 里昂
                   ObjectId('516a350fc221c21236000005'):'GMT+1:00',     # 尼斯 
                   ObjectId('516a3519f8a6461636000001'):'GMT+1:00',     # 威尼斯
                   ObjectId('516a3519f8a6461636000002'):'GMT+1:00',     # 马德里
                   ObjectId('516a3519f8a6461636000003'):'GMT+1:00',     # 巴萨罗那
                   ObjectId('516a3519f8a6461636000004'):'GMT+1:00',     # 柏林
                   ObjectId('516a3519f8a6461636000005'):'GMT+1:00',     # 法兰克福
                   ObjectId('516a35208902ca1936000001'):'GMT+1:00',     # 慕尼黑
                   ObjectId('516a35218902ca1936000002'):'GMT+1:00',     # 苏黎世
                   ObjectId('516a35218902ca1936000003'):'GMT+1:00',     # 日内瓦
                   ObjectId('516a35218902ca1936000004'):'GMT+1:00',     # 阿姆斯特丹
                   ObjectId('516a35218902ca1936000005'):'GMT-5:00',     # 伦敦
                   ObjectId('516a352b625d8b1e36000001'):'GMT+0:00',     # 曼彻斯特
                   ObjectId('516a352b625d8b1e36000003'):'GMT+9:00',     # 大阪
                   ObjectId('516a352b625d8b1e36000005'):'GMT+9:00',     # 首尔（测试）
                   ObjectId('516a3534dac6182136000001'):'GMT+9:00',     # 釜山
                   ObjectId('516a3535dac6182136000002'):'GMT+7:00',     # 曼谷
                   ObjectId('516a3535dac6182136000003'):'GMT+7:00',     # 普吉岛
                   ObjectId('516a3535dac6182136000004'):'GMT+8:00',     # 新加坡  
                   ObjectId('516a3535dac6182136000005'):'GMT+8:00',     # 吉隆坡
                   ObjectId('516a35427dbbf72336000002'):'GMT+8:00',     # 马尼拉
                   ObjectId('516a35427dbbf72336000003'):'GMT+8:00',     # 长滩岛
                   ObjectId('51d3d238e98bbb566a000001'):'GMT+1:00',     # 罗马 
                   ObjectId('52e0f1efb64f047135000003'):'GMT+10:00',    # 悉尼
                   ObjectId('52e62f8e4e59f08771000009'):'GMT-10:00',    # 欧胡岛
                   ObjectId('530735c6d05b06507f000056'):'GMT+9:00',     # 济州特别自治道
                   ObjectId('53074df8d05b06507f00005e'):'GMT+4:00',     # 迪拜
                   ObjectId('53077a0ed05b06507f000077'):'GMT-3:00',     # 布宜诺斯艾利斯
                   ObjectId('5307cf87d05b06507f000090'):'GMT+2:00',     # 特拉维夫
                   ObjectId('5308cb32d05b06507f00009b'):'GMT-8:00',     # 圣地亚哥 
                   ObjectId('5308d35dd05b06507f0000a5'):'GMT+2:00',     # 圣托里尼岛
                   ObjectId('53845d836b36839c04000007'):'GMT+8:00',     # 巴厘岛
                   ObjectId('565fa92d18a1bf1a2b000046'):'GMT+8:00',     # 香港
                   ObjectId('565fa9cd18a1bf1a2b000048'):'GMT+8:00',     # 澳门（测试）
                   ObjectId('5698ae4730e3611971000024'):'GMT+9:00',     # 首尔
                   ObjectId('5698bec74fb72baf67000001'):'GMT+8:00',     # 澳门
                   ObjectId('569c86a02fedc1e719000194'):'GMT+8:00',     # 台北
                   ObjectId('569c8d062fedc1e7190001ad'):'GMT+9:00',     # 东京
                   ObjectId('569c95852fedc1e7190001ea'):'GMT+9:00',     # 京都
        }
    
    def __init__(self):
        pass

    @staticmethod
    def convert_city(address_old, port_old, address_new, port_new):
        # old database connection
        client = MongoClient(address_old, port_old)
        travel1 = client.travel1

        # new database connection
        client = MongoClient(address_new, port_new)
        travel2 = client.travel2

        # old collection latest city
        latest_city = travel1.latestcity
        old_label = travel1.label
        city_new = travel2.city
        new_label = travel2.label

        # clean former data
        city_new.remove()

        for city_old in latest_city.find():
            _id = city_old['_id']
            city_name = city_old['cityname']
            city_name_en = city_old['cityname_en']
            city_name_py = city_old['cityname_py']

            if 'imgforapp' in city_old:
                city_cover_image = "http://weegotest.b0.upaiyun.com/city/citypathforApp/" + city_old['imgforapp']
            else:
                city_cover_image = None


            label_dict = {}
            label_list = []
            # 景点 list
            if 'attrlabels' in city_old:
                label_list_old = city_old['attrlabels']
                if len(label_list_old) > 0:
                    for label_old in label_list_old:
                        label_id = label_old['_id']
                        if label_id != '':
                            label_temp = old_label.find_one({'_id': ObjectId(label_id)}) 
                            temp_new_label = new_label.find_one({'name': label_temp['label'], 'type': 0})
                            label_list.append({'_id': temp_new_label['_id'], 'name': temp_new_label['name'] })
                    label_dict['0'] = label_list       

            # 餐厅 list
            label_list = []
            
            if 'reslabels' in city_old and len(city_old['reslabels']) > 0:
                for label_old in city_old['reslabels']:
                    if 'title' in label_old:
                        temp_new_label = new_label.find_one({'name': label_old['title'], 'type': 1})
                        label_list.append({'_id': temp_new_label['_id'], 'name': temp_new_label['name'] })
                label_dict['1'] = label_list
            else:
                temp_new_label = new_label.find_one({'name': u'米其林推荐' , 'type': 1})
                label_list.append({'_id': temp_new_label['_id'], 'name': temp_new_label['name'] })
                    
                temp_new_label = new_label.find_one({'name': u'本地特色' , 'type': 1})
                label_list.append({'_id': temp_new_label['_id'], 'name': temp_new_label['name'] })
                
                temp_new_label = new_label.find_one({'name': u'人气热门' , 'type': 1})
                label_list.append({'_id': temp_new_label['_id'], 'name': temp_new_label['name'] })
                
                temp_new_label = new_label.find_one({'name': u'城市精选' , 'type': 1})
                label_list.append({'_id': temp_new_label['_id'], 'name': temp_new_label['name'] })   
                
                label_dict['1'] = label_list

           # 购物 list
            label_list = []
            if 'shoplabels' in city_old and len(city_old['shoplabels']) > 0:
                for label_old in city_old['shoplabels']:
                    if 'title' in label_old:
                        temp_new_label = new_label.find_one({'name': label_old['title'], 'type': 2})
                        label_list.append({'_id': temp_new_label['_id'], 'name': temp_new_label['name'] })
                label_dict['2'] = label_list 
            else:
                temp_new_label = new_label.find_one({'name': u'商圈' , 'type': 2})
                label_list.append({'_id': temp_new_label['_id'], 'name': temp_new_label['name'] })
                label_dict['2'] = label_list 
                
            if city_old['continents'] == u'美洲':
                city_old['continents'] = u'北美'

            area = {
                'continent': city_old['continents'],
                'country': city_old['countryname']
            }

            # 是否线上展示
            show_flag = city_old['show_flag']
            if show_flag == u'1':
                is_show = True
            else:
                is_show = False

            time_zone = ''
            if _id is not None:
                if City.timezoneMap.has_key(_id):
                    timezone = City.timezoneMap[_id]

            post = {
                '_id': _id,  # 城市ID
                'name': city_name,  # 城市中文名
                'name_en': city_name_en,  # 城市英文名
                'name_py': city_name_py,  # 城市中文名拼音
                'cover_image': city_cover_image,  # 城市首页背景图片
                'label_list': label_dict,  # label列表
                'area': area,
                'is_show': is_show,  # 是否线上展示
                'timezone': timezone
            }
            city_new.insert(post)
            print(post)

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId


class Plan:
    
    # 定义旧集合的名字
    database_old = 'plans'
    
    # 定义新集合的名字
    database_new = 'plan'
    
    # 定义参数字典,其中键为旧集合的字段名,值为新集合的字段名
    # 注意:这里只定义不需要做特殊处理的字段
    params_map = {'_id':'_id',
                  'plan':'plan'
                  }
    
    def __init__(self):
        pass

    @staticmethod
    def convert_plan(address_old, port_old, address_new, port_new, database_old, database_new,
                     params_map):
      
        # old database connection
        client = MongoClient(address_old, port_old)
        travel1 = client.travel1

        # new database connection
        client = MongoClient(address_new, port_new)
        travel2 = client.travel2
      
        # get old collection and coeate new collection
        db_old = travel1[database_old]
        db_new = travel2[database_new]

        # clean former data
        db_new.remove()

        # 临时数组
        temp = [None] * len(params_map.keys())
        
        # 判断当前文档是否含有某个字段,若有则取出后赋值给临时数组,否则为 None
        data = db_old.find()
        for document in data:
            for i in range(len(params_map.keys())):
                if params_map.keys()[i] in document: 
                   temp[i] = document[ params_map.keys()[i] ]
            
            # 需要特殊处理的字段,处理后以字典的形式添加到 other 中
            other = {}
            plan = None
            plans = None
            is_show = None
            is_check = None
            is_image = None
#            if 'plan' in document:
#                plan = document['plan']
#                for i in range(len(plan)):
#                    if plan[i].has_key('plans'):
#                        plans = plan[i]['plans']
#                    for j in range(len(plans)):
#                        if plans[j].has_key('show_flag'):
#                            is_show = plans[j]['show_flag']
#                            if is_show == u'1':
#                                is_show = True
#                            else:
#                                is_show = False
#                        plans[j].update({'show_flag':is_show})
#                                
#                        if plans[j].has_key('checkFlag'):
#                            is_check = plans[j]['checkFlag']
#                            if is_check == u'1':
#                                is_check = True
#                            else:
#                                is_check = False
#                        plans[j].update({'checkFlag':is_check})
#                        
#                        if plans[j].has_key('imgFlag'):
#                            is_image = plans[j]['imgFlag']
#                            if is_image == 'true':
#                                is_image = True
#                            else:
#                                is_image = False
#                        plans[j].update({'imgFlag':is_image})
                     
#                other.update(plan)    
            post = {}      
            post.update(other)
            for i in range(len(params_map.keys())):
                post.update({params_map.values()[i]:temp[i]})
            db_new.insert(post)
            print post
        
            
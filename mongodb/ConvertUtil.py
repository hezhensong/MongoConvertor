#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId


class ConvertUtil:
    
    # 定义旧集合的名字
    database_old = ''
    
    # 定义新集合的名字
    database_new = ''
    
    # 定义参数字典,其中键为旧集合的字段名,值为新集合的字段名
    # 注意:这里只定义不需要做特殊处理的字段
    params_map = {}
    
    def __init__(self):
        pass

    @staticmethod
    def convert_util(address_old, port_old, address_new, port_new, database_old, database_new,
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
        for document in db_old.find():
            for i in range(len(params_map.keys())):
                if params_map.keys()[i] in document: 
                   temp[i] = document[ params_map.keys()[i] ]
            
            # 需要特殊处理的字段,处理后以字典的形式添加到 other 中
            other = {}       
            
#             例如,需要将 show_flag 的 0/1 转换为 false/true
#            if 'show_flag' in document:
#                show_flag = document['show_flag']
#                if show_flag == u'1':
#                    is_show = True
#                else:
#                    is_show = False
#            else:
#                is_show = False
#            
#            other.update({'is_show':is_show})
            
            post = {}      
            post.update(other)
            for i in range(len(params_map.keys())):
                post.update({params_map.values()[i]:temp[i]})
            db_new.insert(post)
            print post
        
            
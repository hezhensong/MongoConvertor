#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient


class Label:
    def __init__(self):
        pass

    @staticmethod
    def convert_label(address_new, port_new):
       
        client = MongoClient(address_new, port_new)
        travel2 = client.travel2

        label_new = travel2.label
        attraction_new = travel2.attraction
        restaurant_new = travel2.restaurant
        shopping_new =  travel2.shopping
        
        # clean former data
        label_new.remove()
        
        name = ''
        name_array = []
        
        for document in attraction_new.find():
            if 'master_label' in document:
                if document['master_label'] is not None and document['master_label'] != {}:
                    label_array = document['master_label']
                    if label_array is not None and len(label_array) > 0:
                        for i in range(len(label_array)):
                            if label_array[i]['label'] != '':
                                post = {'name': label_array[i]['label'], 'type': 0}
                                if name_array.count({'name': label_array[i]['label'], 'type': 1}) == 0:
                                    name_array.append({'name': label_array[i]['label'], 'type': 1})
                                    label_new.insert(post)
                                    print post
            
                    
        for document in restaurant_new.find():
            if 'master_label' in document:
                if document['master_label'] is not None and document['master_label'] != {}:
                    label_array = document['master_label']
                    if label_array is not None and len(label_array) > 0:
                        for i in range(len(label_array)):
                            if label_array[i]['label'] != '':
                                post = {'name': label_array[i]['label'], 'type': 1}
                                if name_array.count({'name': label_array[i]['label'], 'type': 1}) == 0:
                                    name_array.append({'name': label_array[i]['label'], 'type': 1})
                                    label_new.insert(post)
                                    print post
        
        for document in shopping_new.find():
            if 'master_label' in document:
                if document['master_label'] is not None and document['master_label'] != {}:
                    label_array = document['master_label']
                    if label_array is not None and len(label_array) > 0:
                        for i in range(len(label_array)):
                            if label_array[i]['label'] != '':
                               post = {'name': label_array[i]['label'], 'type': 2}
                               if name_array.count({'name': label_array[i]['label'], 'type': 2}) == 0:
                                    name_array.append({'name': label_array[i]['label'], 'type': 2})
                                    label_new.insert(post)
                                    print post
                                    
        post = {'name': '商圈', 'type': 2}
        label_new.insert(post)
        print post
    
        #             print(post)
        # for label_old in labels_old.find():
        #     _id = label_old['_id']
        #     title = label_old['label']
        #
        #     # 标签英文名
        #     if 'label_en' in label_old:
        #         title_en = label_old['label_en']
        #     else:
        #         title_en = None
        #
        #     post = {
        #         '_id': _id,  # 标签ID
        #         'name': title,  # 标签中文名
        #         'name_en': title_en,  # 标签英文名
        #         'type': 0,  # 标签类型
        #     }
        #     label_new.insert(post)
        #     print(post)
        #
        # # old collection latest city
        # latestcity = travel1.latestcity
        # res_label_dict = {}
        #
        # for city in latestcity.find():
        #     if 'reslabels' not in city:
        #         continue
        #
        #     for reslabel in city['reslabels']:
        #         _id = reslabel['_id']
        #         name = reslabel['title']
        #         if _id not in res_label_dict.keys():
        #             res_label_dict[_id] = True
        #
        #             post = {
        #                 '_id': _id,  # 标签ID
        #                 'name': name,  # 标签中文名
        #                 'name_en': None,  # 标签英文名
        #                 'type': 1,  # 标签类型
        #             }
        #             label_new.insert(post)
        #             print(post)

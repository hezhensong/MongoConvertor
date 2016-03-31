#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import datetime

import pytz
from pymongo import MongoClient


class Activity:
    def __init__(self):
        pass

    @staticmethod
    def update_activity(address, port):
        client = MongoClient(address, port)
        travel2 = client.travel2
        activity = travel2.activity

        post = {
            'order_url': u'http://weegotest.b0.upaiyun.com/activities',
            'description': u'2015年11月4日—2016年1月18日  10:00—23:30\n\n提示：\n滑冰整点入场，一场90分钟。',
            'title': u'联合广场2015/2016滑冰季',
            'act_time': datetime.datetime(2016, 6, 3, 0, 0, 0, tzinfo=pytz.utc),
            'start_time': datetime.datetime(2016, 5, 1, 0, 0, 0, tzinfo=pytz.utc),
            'end_time': datetime.datetime(2016, 6, 1, 0, 0, 0, tzinfo=pytz.utc),
            'address': u'布鲁克林博物馆五楼',
            'detail_address': u'圣杰曼德佩区Espace Fondation',
            'cover_image': u'http://weegotest.b0.upaiyun.com/activities/iosimgs/56625acd6079f4ac6f0000c2.jpeg',
            'last_modified_person': u'liuyu',
            'last_modified_time': u'',
            'city_id': u'516a34f958e3511036000003',
            'act_url': u'http://weegotest.b0.upaiyun.com/activities/iosimgs',
            'type': u'体验活动',
            'coordination': u'-118.264654,34.044656',
            'paragraphs': [
                {
                    'detail_up': u'2015年2月2日－2016年6月10日\n周一到周五：10:30-18:30\n周六到周日：10:00-18:30\n   \n简介：\nTupac Shakur是《ALL EYEZ ON ME》的作者，他的写作完全表现了其对生活的热情和对过去的反思，并且他的写作不断激励和鼓舞新一代。',
                    'detail_down': u'在世贸遗址的南缘一角，有一座醒目的建筑，这就是在“9·11”恐怖袭击事件十周年当天对外开放的“9·11”国家纪念馆。之所以醒目，是由于纪念馆入口处有两根顶端呈三叉戟形状的钢柱，高约21米，每根重约45吨，是原先世贸双子楼建筑结构中的一部分，在清理世贸废墟时被找到。纽约市长布隆伯格曾表示，七层楼高的世贸“三叉戟”被放置在世贸遗址，象征着人们克服“9·11”灾难的勇气，也昭示着人们面对未来的希望。此外，国家纪念馆最独特的设计就是位于世贸双子楼原址上的两个陷入地下的方形瀑布池，很好地体现出设计师“倒映虚空”的理念，意在提醒人们反思这里曾经失去的存在。',
                    'image_title': u'"9·11"国家纪念博物馆',
                    'image_url': u'http://weegotest.b0.upaiyun.com/attractions/iosimgs/542a8295a990b99a0500005d.jpeg',
                    'image_brief': u'博物馆9月11日闭馆，9月22日-12月31日的开放时间为9:00-21:00.'
                },
                {
                    'detail_up': u'',
                    'detail_down': u'',
                    'image_title': u'圣巴特里爵主教座堂',
                    'image_url': u'http://weegotest.b0.upaiyun.com/attractions/iosimgs/540eafb3008840e66800002c.jpeg',
                    'image_brief': u'纽约市最大、最华丽的教堂'
                },
                {
                    'detail_up': u'',
                    'detail_down': u'    每日新闻大楼建立于1929-1930年，是纽约最有名的摩天大楼之一，1981年被指定为纽约市的地标。\n    该大楼在1995年以前都是《纽约每日新闻》的总部。《纽约每日新闻》是纽约市场上最大、读者最多的报纸，算是纽约八卦报纸的始祖，在1995年迁出本栋大楼。\n    这幢建筑极具特色，以垂直的棕色砖和水平的白砖，砌成巨大的长形窗户，也形成线条感极强的外观，是30年代装饰艺术(Art Deco)的代表。\n    最让人赞赏的是进门大厅内的地球仪，这是全世界最大的室内地球仪，可以发光而且会逐日运转。看过电影《超人》的朋友对此地一定不会陌生，因为这里正是主角克拉克·肯特(Clark Kent)上班的地方。\n\n       \n      \n    ',
                    'image_title': u'',
                    'image_url': u'http://weegotest.b0.upaiyun.com/attractions/iosimgs/540ebbe1008840e668000037.jpeg',
                    'image_brief': u''
                },
                {
                    'detail_up': u'',
                    'detail_down': u'',
                    'image_title': u'布鲁克林博物馆',
                    'image_url': u'',
                    'image_brief': u'    布鲁克林博物馆位于波士派克公园(Prospect Park)的东北角，占地56万平方英尺，是美国最大、历史最悠久的博物馆之一，也是一座综合性的艺术、历史博物馆。\n    馆内有闻名世界的典藏，展览内容涵盖各国文化渊源，分别在五个楼层展出。其中一楼主要以雕塑展览为主，二楼是亚洲与东南亚艺术展等，三楼为欧洲绘画展以及最重要的埃及古物学展，四楼有十八世纪的欧洲与布鲁克林房间的装饰展，五楼则有美国艺术品展出。此外，内设的埃及古物学图书馆，里面收藏这方面的藏品已超过了大都会艺术博物馆。馆内最重要的是埃及古代艺术的收藏，包括公元前四千年至公元七世纪的文物，另外还有一个埃及古物学图书馆，它的这方面收藏超过了大都会艺术博物馆。\n    有人称布鲁克林艺术博物馆是小“大都会”，但大都会的展陈方式比较传统，参观路线比较复杂，如同卢浮宫那样令人如堕五里云雾；相比之下，布鲁克林的展陈方式却很现代，展线设计得也非常清晰，不仅方便观众观看，也方便进行博物馆教育。\n    这里的展品足够的精彩。且不说朱迪·芝加哥最著名的装置作品“The Dinner Party”，在Luce基金会赞助的整整一层的美国艺术展厅中，其作品的代表性和精彩程度，绝对值得你在看过MoMA和大都会后还要到这里来看一次。此外，博物馆收藏的欧洲现代绘画也不乏精品，绝对值得探访。'
                }
            ]
        }

        activity.insert(post)


address_new = '192.168.6.254'
port_new = 37017
Activity.update_activity(address_new, port_new)

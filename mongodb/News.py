#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import datetime
import pytz
from pymongo import MongoClient


class News:
    def __init__(self):
        pass

    @staticmethod
    def insert_news(address_new, port_new):
        # new database connection
        client = MongoClient(address_new, port_new)
        travel2 = client.travel2
        news = travel2.news

        # clean former data
        news.remove()

        post = {
            'lead': u"一周热点新闻汇总",
            "lead_text": u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean euismod bibendum laoreet. Proin gravida dolor sit amet lacus accumsan et viverra justo commodo. Aenean euismod bibendum laoreet. Proin gravida dolor sit amet lacus accumsan et viverra justo commodo.",
            "news_content": [
                {
                    "title": u"中国买家吸引中国开发商与投资者涌入旧金山湾区",
                    "date": datetime.datetime(2015, 12, 8, 0, 0, 0, 0, tzinfo=pytz.utc),
                    "source": u"环球网",
                    "image": u"http://weegotest.b0.upaiyun.com/activities/iosimgs/5666716bfa93abfc1d00012e.jpeg",
                    "image_desc": u"图片拍摄于xxxxxxx",
                    "text": u"【环球网综合报道】“旧金山门户网站”3月13日报道表示，中国开发商正进入旧金山湾区房地产市场，其中，吸引他们的一大因素就是想要在此购房的中国买家们。报道称，涌入旧金山湾区房产市场的中国资金不仅仅都来自中国的购房者。中国的开发商与投资者们也正在这里建设和发展大型的住宅项目。他们主要是想从中国过剩的房产市场中抽离出来，同时也可以服务于想在旧金山湾区买房的中国买家们...",
                    "url": u"http://news.163.com/16/0323/21/BISDNFNN00014PRF.html"
                },
                {
                    "title": u"中国买家吸引中国开发商与投资者涌入旧金山湾区",
                    "date": datetime.datetime(2015, 12, 8, 0, 0, 0, 0, tzinfo=pytz.utc),
                    "source": u"环球网",
                    "image": u"http://weegotest.b0.upaiyun.com/activities/iosimgs/5666716bfa93abfc1d00012e.jpeg",
                    "image_desc": u"图片拍摄于xxxxxxx",
                    "text": u"【环球网综合报道】“旧金山门户网站”3月13日报道表示，中国开发商正进入旧金山湾区房地产市场，其中，吸引他们的一大因素就是想要在此购房的中国买家们。报道称，涌入旧金山湾区房产市场的中国资金不仅仅都来自中国的购房者。中国的开发商与投资者们也正在这里建设和发展大型的住宅项目。他们主要是想从中国过剩的房产市场中抽离出来，同时也可以服务于想在旧金山湾区买房的中国买家们...",
                    "url": u"http://news.163.com/16/0323/21/BISDNFNN00014PRF.html"
                }
            ]
        }
        news.insert(post)
        print(post)

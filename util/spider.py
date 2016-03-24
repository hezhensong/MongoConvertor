#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import urllib

from bs4 import BeautifulSoup

import html5lib


class Question:
    def __init__(self):
        self.question = u''
        self.time = u''
        self.useful = u''
        self.same = u''
        self.qa = u''
        self.browse = u''


class Mafengwo:
    def __init__(self):
        pass

    @staticmethod
    def crawl(mafengwo_url):
        BeautifulSoup(markup, "html5lib")
        content = urllib.urlopen(mafengwo_url).read()

        soup = BeautifulSoup(content)
        li_list = soup.find_all('ul', class_='_j_pager_box')

        for li in li_list:
            print li.class_


if __name__ == "__main__":
    url = 'http://www.mafengwo.cn/wenda/14383-0/useful.html'
    Mafengwo.crawl(url)

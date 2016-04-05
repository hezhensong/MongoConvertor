#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import urllib

from bs4 import BeautifulSoup


class Question:
    question = u''
    time = u''
    useful = u''
    same = u''
    answer = u''
    browse = u''

    def __init__(self):
        pass

    def format(self):
        print self.question, self.time, self.useful, self.same, self.answer, self.browse


class Mafengwo:
    def __init__(self):
        pass

    @staticmethod
    def crawl(mafengwo_url):
        content = urllib.urlopen(mafengwo_url).read()

        soup = BeautifulSoup(content, "html5lib")
        li_list = soup.body.find_all('li', class_='item clearfix _j_question_item')

        for li in li_list:
            question = Question()

            div_wen = li.find_all('div', class_='wen')
            wen = div_wen[0]
            a = wen.find_all('a', class_='_j_filter_click')
            question.question = a[1].text

            div_info = li.find_all('div', class_='info clearfix')
            info = div_info[0]
            li_list = info.find_all('li')

            question.time = li_list[0].span.text.strip()
            question.useful = li_list[1].a.text.strip()
            question.same = li_list[2].a.text.strip()
            question.answer = li_list[3].text.strip()
            question.browse = li_list[4].a.text.strip()

            question.format()


if __name__ == "__main__":
    url = 'http://www.mafengwo.cn/wenda/14383-0/useful.html'
    Mafengwo.crawl(url)

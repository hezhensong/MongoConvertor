# -*- coding: UTF-8 -*-
import urllib2  
from bs4 import BeautifulSoup  
  
url = "http://www.tripadvisor.cn/Hotel_Review-g60763-d122020-Reviews-Chelsea_Pines_Inn-New_York_City_New_York.html"  
header = {'User-Agent':'Mozilla/5.0'}
req = urllib2.Request(url=url,headers=header)
page = urllib2.urlopen(req)
soup_packtpage = BeautifulSoup(page,"html.parser",from_encoding="utf-8")  
page.close()

names = []
name_list = soup_packtpage.find_all('span',class_ = 'expand_inline scrname mbrName_')
for name in name_list:
    names.append(name.get_text().strip())

titles = []
title_list = soup_packtpage.find_all('span',class_ = 'noQuotes')
for title in title_list:
    titles.append(title.get_text().strip())

ratings = []
ratingDates = []
other_list = soup_packtpage.find_all('div',class_ = 'rating reviewItemInline')
for other in other_list:
    rating = other.find('span', class_='rate sprite-rating_s rating_s')
    ratings.append(rating.img.attrs['alt'].strip())
    ratingDate = other.find('span', class_='ratingDate')
    ratingDates.append(ratingDate.get_text().strip())

comments = []
comments_list = soup_packtpage.find_all('p',class_='partial_entry')
for comment in comments_list:
    comments.append(comment.get_text().strip())
    
comment_data = []
for i in range(len(names)):
    temp = {}
    temp.update({'name':names[i]})
    temp.update({'title':titles[i]})
    temp.update({'rating':ratings[i]})
    temp.update({'date':ratingDates[i]})
    temp.update({'content':comments[i]})
    comment_data.append(temp)
    
for i in range(len(comment_data)):
    print comment_data[i]['name'] + ':' + comment_data[i]['title'] + ':' + comment_data[i]['rating'] + ':' + comment_data[i]['date'] + ':' + comment_data[i]['content']



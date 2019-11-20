import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

#client = MongoClient('localhost', 27017)
#db = client.keyword_project

#플래텀에서 크롤링하기

#keyword 받아서 url 만들기
url1= 'https://platum.kr//?s='
keyword = '스푼'
url2 = url1 + keyword

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url2,headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')


#print(data.status_code == 200)
#title = soup.select_one('#post-131732 > div > div > div > div.post_header_title.two_third.last > h5 > a').text
#title2 = soup.select('#post-129194 > div > div > div > div.post_header_title.two_third.last > h5 > a')
#news = soup.select('#page_content_wrapper > div > div > div.sidebar_content > div > div > div > div > div')

Page = 1
while data.status_code == 200 :
    url3 = 'https://platum.kr/page/'
    keyword1 = '?s=' + keyword
    url4 = url3 + str(Page) + keyword1
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url4, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    news = soup.select('#page_content_wrapper > div > div > div.sidebar_content > div > div > div > div > div')
    for a in news:
        title = a.select_one('h5')
        if title != None :
            #date = a.select_one('div > div > div.cf.listing-meta.meta.below > time').text.strip()
            # image = a.select_one('div > a > img')
            # desc = a.select_one('div > div > div.excerpt > p').text.strip()
            news_data = {
                'title': title.text,
            }
            print(news_data)
    Page += 1

'''
# 벤처 스퀘어에서 크롤링하기

#keyword 받아서 url 만들기
url1= 'https://www.venturesquare.net/?s='
keyword = '패스트파이브'
url2 = url1 + keyword

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url2,headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

page_list = soup.select('body > div.main-wrap > div.main.wrap.cf > div > div > div.main-pagination > a')
page_length = len(page_list)

if page_length == 0 :
    news = soup.select('body > div.main-wrap > div.main.wrap.cf > div > div > div.posts-list.listing-alt > article.post')
    for a in news:
        title = a.select_one('div > div > a').text.strip()
        date = a.select_one('div > div > div.cf.listing-meta.meta.below > time').text.strip()
        # image = a.select_one('div > a > img')
        # desc = a.select_one('div > div > div.excerpt > p').text.strip()
        data = {
            'title': title,
            'date': date
        }
        print(data)
else :
    for i in range(int(page_list[page_length-2].text)):
        url3 = 'https://www.venturesquare.net/page/'
        keyword1 = '?s=' + keyword
        url4 = url3 + str(i+1) + keyword1
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(url4, headers=headers)
        soup = BeautifulSoup(data.text, 'html.parser')
        news = soup.select(
            'body > div.main-wrap > div.main.wrap.cf > div > div > div.posts-list.listing-alt > article.post')
        for a in news:
            title = a.select_one('div > div > a').text.strip()
            date = a.select_one('div > div > div.cf.listing-meta.meta.below > time').text.strip()
            # image = a.select_one('div > a > img')
            # desc = a.select_one('div > div > div.excerpt > p').text.strip()
            news_data = {
                'title': title,
                'date': date
            }
            print(news_data)
'''


from flask import Flask, render_template ,jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.Sparta_test

@app.route('/')
def home():
   return render_template('index.html')

#플래텀에서 크롤링하기

@app.route('/platum', methods=['GET'])
def article_get():
    keyword = request.args.get('keyword')
    url1 = 'https://platum.kr//?s='
    url2 = url1 + keyword
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url2, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    Page = 1
    while data.status_code == 200 :
        url3 = 'https://platum.kr/page/'
        keyword1 = '?s=' + keyword
        url4 = url3 + str(Page) + keyword1
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(url4, headers=headers)
        soup = BeautifulSoup(data.text, 'html.parser')
        news = soup.select('#page_content_wrapper > div > div > div.sidebar_content > div > div > div > div')
        for a in news:
            title = a.select_one('div > h5')
            if title != None :
                news_image = a.select_one('div > div.post_img.static.one_third > a > img')
                news_date = a.select_one('div > span.post_info_date > a').text.strip()
                news_url = a.select_one('div > div.post_img.static.one_third > a')
                news_source = '플래텀'
                news_data = {
                    'title': title.text, 'date' : news_date, 'image' : news_image['src'] ,
                    'url' : news_url['href'], 'source' : news_source
                }
                print(news_data)
                db.platumnews.insert_one(news_data)
        Page += 1
    return jsonify({'result': 'success'})
#print(data.status_code == 200)
#title = soup.select_one('#post-131732 > div > div > div > div.post_header_title.two_third.last > h5 > a').text
#title2 = soup.select('#post-129194 > div > div > div > div.post_header_title.two_third.last > h5 > a')
#news = soup.select('#page_content_wrapper > div > div > div.sidebar_content > div > div > div > div > div')

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

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
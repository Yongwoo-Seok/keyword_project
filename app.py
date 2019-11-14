import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

#client = MongoClient('localhost', 27017)
#db = client.keyword_project

# URL 받기
url = 'https://www.venturesquare.net/?s=오쉐어'

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
            data = {
                'title': title,
                'date': date
            }
            print(data)


'''
for i in range(3):
    print(type(i+1))

news =  soup.select('body > div.main-wrap > div.main.wrap.cf > div > div > div.posts-list.listing-alt > article.post')
for a in news:
    title = a.select_one('div > div > a').text.strip()
    date = a.select_one('div > div > div.cf.listing-meta.meta.below > time').text.strip()
    #image = a.select_one('div > a > img')
    #desc = a.select_one('div > div > div.excerpt > p').text.strip()
    data = {
        'title' : title,
        'date' :date
    }
    print(data)
'''
'''
해야할 일 
1. 검색했을 때 끝 페이지 찾아서 크롤링하기
- 페이지 리스트 길이에서 뒤에서 2번째로 확인
- 
- 페이지 길이 4일때 케이스 찾지못함
2. 날짜 순으로 소팅하기 : 보여줄때 소팅해서 보여주면 되겠지..?
'''

'''
검색했을 때 
https://www.venturesquare.net/?s=키워드

페이지 수 
https://www.venturesquare.net/page/1?s=키워드
제목
body > div.main-wrap > div.main.wrap.cf > div > div > div.posts-list.listing-alt > article.post-794015.post.type-post.status-publish.format-standard.has-post-thumbnail.category-news > div > div > a
body > div.main-wrap > div.main.wrap.cf > div > div > div.posts-list.listing-alt > article.post-786467.post.type-post.status-publish.format-standard.has-post-thumbnail.category-news.tag-30717 > div > div > a
body > div.main-wrap > div.main.wrap.cf > div > div > div.posts-list.listing-alt > article.post-786032.post.type-post.status-publish.format-standard.has-post-thumbnail.category-news.tag-33827 > div > div > a

날짜
body > div.main-wrap > div.main.wrap.cf > div > div > div.posts-list.listing-alt > article.post-794015.post.type-post.status-publish.format-standard.has-post-thumbnail.category-news > div > div > div.cf.listing-meta.meta.below > time
body > div.main-wrap > div.main.wrap.cf > div > div > div.posts-list.listing-alt > article.post-786467.post.type-post.status-publish.format-standard.has-post-thumbnail.category-news.tag-30717 > div > div > div.cf.listing-meta.meta.below > time

내용
body > div.main-wrap > div.main.wrap.cf > div > div > div.posts-list.listing-alt > article.post-794015.post.type-post.status-publish.format-standard.has-post-thumbnail.category-news > div > div > div.excerpt > p

이미지
body > div.main-wrap > div.main.wrap.cf > div > div > div.posts-list.listing-alt > article.post-794015.post.type-post.status-publish.format-standard.has-post-thumbnail.category-news > div > a > img

마지막 페이지
투자유치
body > div.main-wrap > div.main.wrap.cf > div > div > div.main-pagination > a:nth-child(5)

전동킥보드
body > div.main-wrap > div.main.wrap.cf > div > div > div.main-pagination > a:nth-child(3)

맥시멈 페이지 찾기
page_list = soup.select('body > div.main-wrap > div.main.wrap.cf > div > div > div.main-pagination > a')
page_length = len(page_list)
print(page_list)
print(page_length)
print(page_list[2].text)

검색결과의 페이지 수
url3 ='https://www.venturesquare.net/page/'
page = '2'
keyword1 = '?s=' +keyword
url4 = url3 + page + keyword1
'''
#!/usr/bin/env python
# coding: utf-8

# In[11]:


# 표준 모듈 삽입
import math
import math as m
from math import cos, ceil, floor
from math import ceil as c


# In[8]:


print(math.cos(10))
print(math.ceil(5.6))  # 숫자보다 큰 정수 중에 가장 작은 정수(올림)
print(math.floor(5.6)) # 숫자보다 작은 정수 중에 가장 큰 정수(버림)


# In[9]:


# from 모듈명 import 필요한 변수 또는 함수 
from math import cos, ceil, floor

print(cos(10))
print(ceil(5.6))
print(floor(5.6))


# In[10]:


# as를 사용하여 별명(alias) 사용
import math as m
m.cos(10)


# In[97]:


# random 모듈 
import random as rnd

print("random 모듈 : ")
#random() : 0.0 < x < 1.0 사이의 float 리턴
print(rnd.random())

#uniform(min, max) : min < x < max 사이의 float 리턴 
print(rnd.uniform(10,20))

#randrange([min,] max) : min < x < max 사이의 int 리턴 0부터 max
print(rnd.randrange(10,20))

#chioce(list) : 리스트 내부의 임의의 요소를 리턴
print(rnd.choice(list(range(10))))
      
#shuffle(list) : 리스트 요소를 랜덤하게 섞음
a = list(range(10))
print(rnd.shuffle(a), a)

#sample(list, k=숫자) : 리스트에서 숫자의 갯수 요소를 랜덤하게 리턴
print(rnd.sample(a,k=3))


# In[98]:


# sys 모듈 : 시스템 관련 정보를 가져 옴
import sys

print("coptright : ",sys.copyright)
print("version : ",sys.version)


# In[99]:


# os 모듈 : 운영체제와 관련된 명령어
import os

print("현재 운영체제 : ",os.name)
print("현재 작업 경로 : ",os.getcwd())
print("현재 폴더 리스트 : ",os.listdir())


# In[100]:


# 디렉토리 생성
os.mkdir('test_dir')
os.listdir()


# In[101]:


# 디렉토리 삭제
os.rmdir('test_dir')
os.listdir()


# In[102]:


#file 이름 변경 : rename(old_name, new_name)
os.rename('day_1.py', 'day_1_1.py')
os.listdir()


# In[ ]:


#file 삭제 : remove(파일명)
#os.remove('new.py')
os.listdir()


# In[103]:


get_ipython().system('dir')


# In[112]:


# datetime 모듈 : 날짜를 형식에 맞게 편집 가능
import datetime as dt
print(dt.datetime.now())
print(dt.datetime.today())


# In[114]:


# time 모듈 : 시간 멈춤
import time
print("time start")
time.sleep(3)
print("time end")


# In[116]:


# urllib 모듈 : url라이브러라
from urllib import request

target = request.urlopen('http://www.google.com')
output = target.read()
print(output)
# <html> ~ </html> tag 형식으로 변환해 주는 모듈 : BeatifulSoup


# In[117]:


get_ipython().system('pip install beautifulSoup4')


# In[118]:


from bs4 import BeautifulSoup

target = request.urlopen('http://www.google.com')
soup = BeautifulSoup(target)
soup


# In[121]:


soup.title.string
soup.find_all('a')


# In[140]:


# url에 연결 -> urllib.request.urlopen(url 명)
# url 자료를 가져옴 -> <html> ~ </html> 태그 형식으로
# BeautifulSoup(url open 정보)
from urllib import request
from bs4 import BeautifulSoup

url = 'https://www.weather.go.kr/w/weather/forecast/mid-term.do?stnId1=108'
target = request.urlopen(url)

soup = BeautifulSoup(target)
soup.title.string


# In[163]:


#for location in soup.select("table.table-col"):
for location in soup.find_all('tr'): #('td.midterm-city'):
    if location.find('td',class_= 'midterm-city'):
        print("도시명 : {}, 최저기온 : {}, 최고기온 {}".             format(location.find('td',class_= 'midterm-city').text,
                   location.find('span',class_= 'tmn').text,
                   location.find('span',class_= 'tmx').text))
        
    # print(tr.select_one('td.midterm-city'))
 #   print("도시 : ", location.select_one('td').text)

#for body in location.select("tbody"):
#   print(body)
        
# print("도시 : ",location.select("tbody").string)
';'


# In[165]:


#!pip install flask


# In[ ]:


# flask 모듈
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1> Hello </h1>"


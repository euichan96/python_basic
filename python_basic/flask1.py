#!/usr/bin/env python
# coding: utf-8

# In[6]:


# flask 모듈
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return url_report()

def url_report():
    from urllib import request
    from bs4 import BeautifulSoup
    
    url = 'https://www.weather.go.kr/w/weather/forecast/mid-term.do?stnId1=108'
    target =request.urlopen(url)
    soup = BeautifulSoup(target)
    output = '<table>'
    for location in soup.find_all('tr'):
        output += '<tr>'
        if location.find('td', class_='midterm-city'):
            output += "<td>{}</td>".format(location.find('td',class_='midterm-city').text)
            output += "<td>{}</td>".format(location.find('span',class_='tmn').text)
            output += "<td>{}</td>".format(location.find('span',class_='tmx').text)
    return(output)


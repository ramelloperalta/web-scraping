# -*- coding: utf-8 -*-

#hasn't worked since Amazon's bot detection doesn't like web scraping :(
#may find some success if you change user agent, but a better solution is probably to work with the amazon API, or even scrapy

import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.ca/Apple-MacBook-Retina-MPTV2LL-Refurbished/dp/B07JMNNNWH/ref=sr_1_10?dchild=1&keywords=macbook+pro&qid=1622258203&sr=8-10'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    title = soup.find(id='productTitle').get_text() 
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = price[:-3]
    
    if(converted_price < 1.500):
        send_mail()

    print(converted_price)
    print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('ramelloperalta@gmail.com', 'aflsyairkyigfcgj')
    subject = 'Price fell on the Macbook'
    body = 'Check it out! ' + URL
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'ramelloperalta@gmail.com',
        'ramelloperalta@gmail.com',
        msg
        )
    
    print('Email sent')
    
    server.quit()

check_price()


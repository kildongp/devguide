# -*- coding: utf-8 -*- 
# goodauction.py
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

driver = webdriver.Chrome( BASE_DIR + '/chromedriver')
driver.implicitly_wait(3)
# url에 접근한다.
driver.get('http://www.goodauction.com/')

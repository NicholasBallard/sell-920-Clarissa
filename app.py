"""
app.py - write the automation script for scraping Allegheny County's property site
"""
# use selenium

import time
from selenium import webdriver

# start chrome webdriver
dr = webdriver.Chrome(r'C:\web drivers\chromedriver.exe')
home_url = 'http://www2.county.allegheny.pa.us/RealEstate/Search.aspx'

# go to the home page
dr.get('http://www2.county.allegheny.pa.us/RealEstate/Search.aspx')

time.sleep(1)

dr.find_element_by_id('txtStreetName').send_keys('Clarissa')

dr.find_element_by_id('btnSearch').click()

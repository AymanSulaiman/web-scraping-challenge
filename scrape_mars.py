import requests
from bs4 import BeautifulSoup as bs
from datatime import datatime as dt
import pandas as pd
from splinter import Browser

class browser:
    exe_path = {'chrome': 'chromedriver.exe'}
    browser = Browser("chrome", **exe_path, headless=False)
    

def scrape_mars_news():
    # URL for Mars News
    url = 'https://mars.nasa.gov/news/'
    response = url.get(url)
    b  = browser.browser.visit(url)
    
    soup_title = bs(response.text, 'html.parser')
    soup_para = bs(b.html, 'html.parser')

    title = soup_title.find('div', class_='content_title').find('a').text
    para = soup_para.find('div', class_'article_teaser_body').text



def scrape_mars_image():
    # URL for space images
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    b = browser.browser.visit(url)
    html = b.html
    soup = bs(html, 'html.parser')


def scrape_mars_weather():
    # URL for the space weather on mars
    url = 'https://twitter.com/marswxreport'


def scrape_mars_facts():
    # URL for mars stats and facts
    url = 'https://space-facts.com/mars/'


def scrape_hemisphere():
    # URL for the mars hemisphere 
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt
import pandas as pd
from splinter import Browser


def scrape_mars_news():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://mars.nasa.gov/news/'
    response = requests.get(url)
    browser.visit(url)
    html = browser.html
    
    soup_title = bs(response.text, 'html.parser')
    soup_para = bs(html, 'html.parser')

    title = soup_title.find('div', class_='content_title').find('a').text
    paragraph = soup_para.find('div', class_='article_teaser_body').text

    title_clean = title.replace("\n","")

    return title_clean, paragraph



def scrape_mars_image():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    article = soup.find('article', class_='carousel_item')
    image_extension  = article['style'].split("('", 1)[1].split("')")[0]
    image_url = f'jpl.nasa.gov{image_extension}'
    return image_url



def scrape_mars_weather():
    url = 'https://twitter.com/marswxreport'
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    weather = soup.find('p', class_='tweet-text').text
    weather_latest = weather.replace("pic.twitter.com/DlcFke5nLl","")
    return weather_latest


def scrape_mars_facts():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://space-facts.com/mars/'
    browser.visit(url)
    html = browser.html
    mars_facts = pd.read_html(html)[2]
    mars_facts.columns = ['','Mars Values']
    mars_facts.set_index('', inplace = True)
    return mars_facts


def scrape_hemisphere():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    results_item_list = soup.find('div', class_='collapsible results').find_all('div', class_='item')
    
    hemisphere_image_urls = []
    
    for h in results_item_list:
        title = h.find('h3', class_=None).text
        title = title.replace(" Enhanced","")
        url = h.find('a')['href']
        url_1 = f'https://astrogeology.usgs.gov{url}'
        browser.visit(url_1)
        html = browser.html
        soup_image = bs(html,'html5lib')
        img_url = soup_image.find("div", class_="downloads").a['href']
        hemisphere_image_urls.append({"title": title, "img_url": img_url})
    
    return hemisphere_image_urls


def scrape_all():
    mars_data = {
        "title": scrape_mars_news()[0],
        "paragraph": scrape_mars_news()[1],
        "featured_img_url": scrape_mars_image(),
        "weather_update": scrape_mars_weather(),
        "mars_facts": scrape_mars_facts(),
        "hemisphere_links": scrape_hemisphere()

    }

    return mars_data


## Debuging area

# for i in range(10):
#     print(scrape_mars_news())

# for i in range(10):
#     print(scrape_mars_image())

# for i in range(1):
#     print(scrape_mars_weather())

# for i in range(10):
#     print(scrape_mars_facts())

# for i in range(10):
#     pprint(scrape_hemisphere())

# print(scrape_all())

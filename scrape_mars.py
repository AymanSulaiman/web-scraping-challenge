import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt
import pandas as pd
from splinter import Browser
import re


# def scrape_mars_news():
#     executable_path = {'executable_path': 'chromedriver.exe'}
#     browser = Browser('chrome', **executable_path, headless=False)

#     url = 'https://mars.nasa.gov/news/'
#     response = requests.get(url)
#     browser.visit(url)
#     html = browser.html
    
#     soup_title = bs(response.text, 'html.parser')
#     soup_para = bs(html, 'html.parser')

#     title = soup_title.find('div', class_='content_title').find('a').text
#     paragraph = soup_para.find('div', class_='article_teaser_body').text

#     title_clean = title.replace("\n","")

#     return title_clean, paragraph



# def scrape_mars_image():
#     executable_path = {'executable_path': 'chromedriver.exe'}
#     browser = Browser('chrome', **executable_path, headless=False)
#     url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
#     browser.visit(url)
#     html = browser.html
#     soup = bs(html, 'html.parser')
#     article = soup.find('article', class_='carousel_item')
#     image_extension  = article['style'].split("('", 1)[1].split("')")[0]
#     image_url = f'jpl.nasa.gov{image_extension}'
#     return image_url



# def scrape_mars_weather():
#     url = 'https://twitter.com/marswxreport'
#     response = requests.get(url)
#     soup = bs(response.text, 'html.parser')
#     weather = soup.find('p', class_='tweet-text').text
#     weather_latest = weather.replace("pic.twitter.com/DlcFke5nLl","")
#     return weather_latest


# def scrape_mars_facts():
#     executable_path = {'executable_path': 'chromedriver.exe'}
#     browser = Browser('chrome', **executable_path, headless=False)
#     url = 'https://space-facts.com/mars/'
#     browser.visit(url)
#     html = browser.html
#     mars_facts = pd.read_html(html)[2]
#     mars_facts.columns = ['','Mars Values']
#     mars_facts.set_index('', inplace = True)
#     return mars_facts


# def scrape_hemisphere():
#     executable_path = {'executable_path': 'chromedriver.exe'}
#     browser = Browser('chrome', **executable_path, headless=False)
#     url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
#     browser.visit(url)
#     html = browser.html
#     soup = bs(html, 'html.parser')
#     results_item_list = soup.find('div', class_='collapsible results').find_all('div', class_='item')
    
#     hemisphere_image_urls = []
    
#     for h in results_item_list:
#         title = h.find('h3', class_=None).text
#         title = title.replace(" Enhanced","")
#         url = h.find('a')['href']
#         url_1 = f'https://astrogeology.usgs.gov{url}'
#         browser.visit(url_1)
#         html = browser.html
#         soup_image = bs(html,'html5lib')
#         img_url = soup_image.find("div", class_="downloads").a['href']
#         hemisphere_image_urls.append({"title": title, "img_url": img_url})
    
#     return hemisphere_image_urls


def scrape():
    ####################
    ## NASA Mars News ##
    ####################
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://mars.nasa.gov/news/'
    response = requests.get(url)
    browser.visit(url)
    html = browser.html
    
    soup_title = bs(response.text, 'html.parser')
    soup_para = bs(html, 'html.parser')

    title_not_clean = soup_title.find('div', class_='content_title').a.text
    paragraph = soup_para.find('div', class_='article_teaser_body').text

    # named title_1 as not to conflict with the title variable 
    title_1 = title_not_clean.replace("\n","")
    browser.quit()
    # return title_1, paragraph
    ####################
    ## NASA Mars News ##
    ####################


    ###########################
    ## JPL Mars Space Images ##
    ###########################
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    article = soup.find('article', class_='carousel_item')
    image_extension  = article['style'].split("('", 1)[1].split("')")[0]
    featured_img_url = f'jpl.nasa.gov{image_extension}'
    browser.quit()
    ###########################
    ## JPL Mars Space Images ##
    ###########################


    ##################
    ## Mars Weather ##
    ##################
    url = 'https://twitter.com/marswxreport'
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    weather = soup.find('p', class_='tweet-text').text
    weather_update = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', weather)
    # return weather_update
    ###################
    ## Mars Weather  ##
    ###################


    #################
    ## Mars Facts  ##
    #################
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://space-facts.com/mars/'
    browser.visit(url)
    html = browser.html
    mars_facts = pd.read_html(html)[2]
    mars_facts.columns = ['','Mars Values']
    mars_facts.set_index('', inplace = True)
    browser.quit()
    mars_facts.to_html(os.path.join('templates','mars_facts.html'))
    # return mars_facts
    #################
    ## Mars Facts  ##
    #################


    #######################
    ## Mars Hemispheres  ##
    #######################
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
    
    browser.quit()
    # return hemisphere_image_urls
    #######################
    ## Mars Hemispheres  ##
    #######################

    #############################
    ## Compiling the Mars Data ##
    #############################

    mars_data = {
        "title_1": title_1,
        "paragraph": paragraph,
        "featured_img_url": featured_img_url,
        "weather_update": weather_update,
        # "mars_facts": mars_facts,
        "hemisphere_image_urls": hemisphere_image_urls
    }

    #############################
    ## Compiling the Mars Data ##
    #############################

    return mars_data

print(scrape())
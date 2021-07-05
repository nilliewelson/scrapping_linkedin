import requests, time, random
from bs4 import BeautifulSoup
from selenium import webdriver


browser = webdriver.Chrome("/home/nilliewelson/Desktop/USER/Web Scraping/scrapping_linkedin/chromedriver")
browser.get("https://www.linkedin.com/login/")
with open("config.txt", "r") as  file :
  lines = file.readlines()
username = lines[0]
password = lines[1]



elementID = browser.find_element_by_id("username")
elementID.send_keys(username)

elementID = browser.find_element_by_id("password")
elementID.send_keys(password)

elementID.submit()


remember_button = browser.find_element_by_name(".btn__secondary--large-muted")
remember_button.click()


link_00 = "https://www.linkedin.com/feed/"
browser.get(link_00)
link_01 = "https://www.linkedin.com/jobs/search/?keywords=Python&start=0"
browser.get(link_01)
#link_02 = "profile link 3"
#link_03 = "profile link 4"


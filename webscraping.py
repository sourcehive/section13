import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver 6.exe')
driver.get('https://oxylabs.io/blog')
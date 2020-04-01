import requests
from bs4 import BeautifulSoup
import pandas as pd
import selenium
from selenium import webdriver
import time




def scrape(url):
    print("loading data...")
    driver = webdriver.Chrome(r'C:\Users\cris_\Downloads\chromedriver_win32\chromedriver.exe')  # Optional argument, if not specified will search path.
    driver.get(url)
    time.sleep(20)
    html = driver.page_source
    soup = BeautifulSoup(html)
    table_legend = soup.find_all("table", class_="table_legend")
    print(table_legend)

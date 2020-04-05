from bs4 import BeautifulSoup
from selenium import webdriver
import time
import wave_checker.scrape_titles as sc
import wave_checker.scrape_content as sr


def scrape_all (url):
    print("loading data...")
    driver = webdriver.Chrome(r'C:\Users\cris_\Downloads\chromedriver_win32\chromedriver.exe')  # Optional argument, if not specified will search path.
    driver.get(url)
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html)
    mix_models_titles, swell_table_titles = sc.scrape_titles(soup)
    sr.contents(soup)
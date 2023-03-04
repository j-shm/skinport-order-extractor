from __future__ import unicode_literals
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pathlib import Path

from bs4 import BeautifulSoup
import time

if __name__ == "__main__":
    profile = webdriver.FirefoxProfile(r'firefoxprofile')
    executable_path = r'C:\Program Files (x86)\geckodriver'
    options = webdriver.FirefoxOptions(),
    driver = webdriver.Firefox(
        firefox_profile=profile
    )
    
    
    driver.implicitly_wait(5) 

    numberofpages = 2

    f = open("export.txt", "w", encoding="utf-8")
    f.writelines("item,price")
    for i in range(1,(numberofpages+1)):
        driver.get(f"https://skinport.com/account/orders?status=paid&page={i}")  

        time.sleep(2) 
        html = driver.page_source
        soup = BeautifulSoup(html)
        for item in soup.find_all("div", {"class": "ItemListView Orders-item ItemListView--simple"}):
            name = str(item.find("div", {"class": "ItemListView-name"}))
            if name != None:
                name = name.split("<")[1].split(">")[1]
            price = item.find("div", {"class": "ItemListView-priceRight"}).getText()
            f.writelines(f"\n{name},{price}")
            print(name,price)
f.close()
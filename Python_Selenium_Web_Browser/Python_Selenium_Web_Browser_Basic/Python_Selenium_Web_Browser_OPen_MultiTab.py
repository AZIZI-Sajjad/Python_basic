# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 03:06:20 2022

@author: SDA

https://www.youtube.com/watch?v=wmw6YyMie30
https://stackoverflow.com/questions/65075832/open-multiple-urls-in-same-browser-with-selenium-python
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path=r"D:\CODE\Python\Selenium_ChromeDrive\chromedriver.exe")


#driver.maximize_window()
driver.delete_all_cookies()
firstCard = 'https://www.linkedin.com'
secondeCard = 'https://www.google.com' 
thirthCard = 'https://www.yahoo.com'
forthCard = 'https://www.bing.com'
urls = [firstCard, secondeCard, thirthCard, forthCard]

#login = driver.find_element_by_xpath("//span[text()='Connexion']")
#login.click()

for posts in range(len(urls)):
    print(posts)
    driver.get(urls[posts])    
    if(posts!=len(urls)-1):
       driver.execute_script("window.open('');")
       chwd = driver.window_handles
       driver.switch_to.window(chwd[-1])


while (2 < 3):
    for posts in range(len(urls)):
        driver.switch_to.window(chwd[-1])
        #print(posts)
        #driver.get(urls[posts])    
        #if(posts!=len(urls)-1):
           #driver.execute_script("window.open('');")
           #chwd = driver.window_handles
#    driver.switch_to.window(chwd[-1])

# you can move to specific handle    
chwd = driver.window_handles
print(chwd)

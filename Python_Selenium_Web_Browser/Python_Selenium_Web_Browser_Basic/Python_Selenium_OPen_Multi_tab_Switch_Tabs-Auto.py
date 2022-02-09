# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 01:20:00 2022

@author: Sajjad

Refs : 
https://www.youtube.com/watch?v=wmw6YyMie30
https://stackoverflow.com/questions/65075832/open-multiple-urls-in-same-browser-with-selenium-python
https://isolution.pro/fr/q/so50086387/selenium-n-ouvrira-pas-de-nouvelle-url-dans-un-nouvel-onglet-python-et-chrome
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# Define Google Chrome driver path on the PC 
# the script use this driver to control chrome (Browser)
# /!\ At the next there is Windows path, it's different on Linux 
driver = webdriver.Chrome(executable_path=r"D:\CODE\Python\Selenium_ChromeDrive\chromedriver.exe")


#driver.maximize_window()
driver.delete_all_cookies()
firstCard = 'https://www.linkedin.com'
secondeCard = 'https://www.google.com' 
thirthCard = 'https://www.yahoo.com'
forthCard = 'https://www.bing.com'
urls = [firstCard, secondeCard, thirthCard, forthCard]

# Login options for to Auto Login to pages 
"""
#login = driver.find_element_by_xpath("//span[text()='Connexion']")
#login.click()
"""


def openPages():
    # Open pages in MultiTabs at the same Window Chrome
    for posts in range(len(urls)):
        print(posts)
        driver.get(urls[posts])    
        if(posts!=len(urls)-1):
            # driver.execute_script("window.open('');")
            # For open Tabs at the same Windows 
            driver.execute_script("window.open('');")
            chwd = driver.window_handles
            # Switch to previos tab recently opened 
            # Il lets to open next page at the same windows at the next Tab  
            driver.switch_to.window(chwd[-1])

def SwitchTabs():
    # Def to switch at the next tab every 2 secondes
    while (True):
        for posts in range(len(urls)):
            # switch to next tab at the same Windows
            driver.switch_to.window(driver.window_handles[posts])
            posts = posts + 1
            # Wait 2 secondes then switch to the next Tab
            time.sleep(2)
            print(posts)
            
            # Show Tabs chwd
            # EXEMPLE :  ['CDwindow-22FA91593C170E1532B67FC1EE40B640', 'CDwindow-D65DD85B90D978EC39F17AF78A7997C6', 'CDwindow-79AB22434C7C43DE456CF8A0AD123A41', 'CDwindow-A9794F346058625B87A1AECBEDCE6691']
            """
            chwd = driver.window_handles
            print(chwd)
            """

if __name__ == '__main__':
    openPages()
    SwitchTabs()

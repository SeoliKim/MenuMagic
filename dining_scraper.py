from re import L
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from datetime import date
import csv
import time

#This is how we catch exceptions 
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
print("Starting program!")

#This connects us to the internet 
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)
browser.maximize_window() # For maximizing window
browser.implicitly_wait(5) #Makes the program wait 20 seconds for everything to load

def check_exists_by_xpath(xpath):
    try:
        browser.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

path = r"diningScraper.csv"
with open(path, 'a', encoding='utf-8', newline='') as f:
   writer = csv.writer(f)
   row1 = ["itemName","type","meal","location","ingredients"]
   writer.writerow(row1)

web_link = "http://menuportal23.dining.rutgers.edu/foodpro/pickmenu.asp?sName=Rutgers+University+Dining&locationNum=04&locationName=Busch+Dining+Hall&naFlag=1"
browser.get(web_link)   
quote = browser.find_element(By.XPATH, '/html/body/div[5]/div/div[1]/div[2]/form/div[1]/div[16]').text
def get_values(meal, location, index):  
   another_item = True
   x = 1
   while(another_item):
      
      try:
         itemXPath = '/html/body/div[5]/div/div[1]/div[2]/form/div[1]/div[{C}]'.format(C=str(index))
         itemName = browser.find_element(By.XPATH, itemXPath).text
         if (itemName != quote):
            typeXPath = '/html/body/div[5]/div/div[1]/div[2]/form/div[1]/p[{Y}]'.format(Y=str(x))
            type = browser.find_element(By.XPATH, typeXPath).text
            type = type.replace("-- ","")
            x_path_input = '/html/body/div[5]/div/div[1]/div[2]/form/div[1]/div[{Z}]'.format(Z=str(index+2))
            browser.find_element(By.XPATH, x_path_input).click()
            if (check_exists_by_xpath('/html/body/div[5]/div[1]/h2[3]') != True):
               ingredients = browser.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[2]/div/p').text
            else:
               ingredients = ""
            browser.back()
            row = [itemName, type.replace(" --",""), meal, location, ingredients.replace("INGREDIENTS:  ","")]
            with open(path, 'a', encoding='utf-8', newline='') as f:
                  writer = csv.writer(f)
                  writer.writerow(row)
            index+=5
         else:
            index+=1
            x+=1
      except NoSuchElementException:
         another_item = False
    
#ATRIUM
web_link = "http://menuportal.dining.rutgers.edu/FoodPro/pickmenu.asp?sName=Rutgers+University+Dining&locationNum=13&locationName=The+Atrium&naFlag=1"
browser.get(web_link)
get_values('Breakfast', 'Atrium', 7)

web_link = "http://menuportal.dining.rutgers.edu/FoodPro/pickmenu.asp?locationNum=13&locationName=The+Atrium&dtdate=10/7/2023&mealName=Lunch+Entree&sName=Rutgers+University+Dining"
browser.get(web_link)
get_values('Lunch', 'Atrium', 7)

web_link = "http://menuportal.dining.rutgers.edu/FoodPro/pickmenu.asp?locationNum=13&locationName=The+Atrium&dtdate=10/7/2023&mealName=Dinner+Entree&sName=Rutgers+University+Dining"
browser.get(web_link)
get_values('Dinner', 'Atrium', 7)

#BUSCH
web_link = "http://menuportal23.dining.rutgers.edu/foodpro/pickmenu.asp?sName=Rutgers+University+Dining&locationNum=04&locationName=Busch+Dining+Hall&naFlag=1"
browser.get(web_link)
get_values('Lunch', 'Busch', 7)

web_link = "http://menuportal23.dining.rutgers.edu/foodpro/pickmenu.asp?locationNum=04&locationName=Busch+Dining+Hall&dtdate=10/7/2023&mealName=Dinner&sName=Rutgers+University+Dining"
browser.get(web_link)
get_values('Dinner', 'Busch', 7)

#LIVINGSTON
web_link = "http://menuportal.dining.rutgers.edu/FoodPro/pickmenu.asp?sName=Rutgers+University+Dining&locationNum=03&locationName=Livingston+Dining+Commons&naFlag="
browser.get(web_link)
get_values('Lunch', 'Livingston', 7)

web_link = "http://menuportal.dining.rutgers.edu/FoodPro/pickmenu.asp?locationNum=03&locationName=Livingston+Dining+Commons&dtdate=10/7/2023&mealName=Dinner&sName=Rutgers+University+Dining"
browser.get(web_link)
get_values('Dinner', 'Livingston', 7)

#NEILSON
web_link = "http://menuportal.dining.rutgers.edu/FoodPro/pickmenu.asp?sName=Rutgers+University+Dining&locationNum=05&locationName=Neilson+Dining+Hall&naFlag=1"
browser.get(web_link)
get_values('Lunch', 'Neilson', 7)

web_link = "http://menuportal.dining.rutgers.edu/FoodPro/pickmenu.asp?locationNum=05&locationName=Neilson+Dining+Hall&dtdate=10/7/2023&mealName=Dinner&sName=Rutgers+University+Dining"
browser.get(web_link)
get_values('Dinner', 'Neilson', 7)

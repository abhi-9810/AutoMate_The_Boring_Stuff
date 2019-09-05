from xlrd import open_workbook
from xlwt import Workbook
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import time
import html5lib
import urllib
from bs4 import BeautifulSoup
import re
from PIL import Image
import string
import xlsxwriter								#NAME OF INPUT FILE CONTAINING ONE SHEET
import re	
import random
wb = open_workbook('chennai.xlsx')														#NAME OF INPUT FILE CONTAINING ONE SHEET
wb_sheet_name="chennai.xlsx"	
link="http://intellify.in/registration/"
chrome_options = webdriver.ChromeOptions()
driver=webdriver.Chrome(executable_path=r"chromedriver.exe")
driver.get(link)
wait = WebDriverWait(driver, 600)
for s in wb.sheets():
	if(s.name==wb_sheet_name):
		for row in range(3,47):
                    inp_xpath = "//*[@id='name']"
                    input_box = wait.until(EC.presence_of_element_located((
                        By.XPATH, inp_xpath)))
                    string1=(s.cell(row,0).value)
                    input_box.send_keys(string1)
                    agree_path="//*[@id='email']"
                    input_box = wait.until(EC.presence_of_element_located((
                        By.XPATH, agree_path)))
                    string1=(s.cell(row,1).value)    
                    input_box.send_keys(string1)
                    inp_xpath = "//*[@id='cpassword1']"
                    input_box = wait.until(EC.presence_of_element_located((
                        By.XPATH, inp_xpath)))
                    string1="isco_2k18_"+str(random.randint(1,1000))
                    input_box.send_keys(string1)

                    inp_xpath = "//*[@id='cpassword2']"
                    input_box = wait.until(EC.presence_of_element_located((
                        By.XPATH, inp_xpath)))
                    input_box.send_keys(string1)

                    inp_xpath = "//*[@id='school']"
                    input_box = wait.until(EC.presence_of_element_located((
                        By.XPATH, inp_xpath)))
                    string1=(s.cell(row,4).value)
                    input_box.send_keys(string1)

                    inp_xpath = "//*[@id='phone1']"
                    input_box = wait.until(EC.presence_of_element_located((
                        By.XPATH, inp_xpath)))
                    string1=str((s.cell(row,2).value))
                    input_box.send_keys(string1)
                    inp_xpath = "//*[@id='phone2']"
                    input_box = wait.until(EC.presence_of_element_located((
                        By.XPATH, inp_xpath)))
                    string1=str((s.cell(row,2).value))
                    input_box.send_keys(string1)

                    inp_xpath = "//*[@id='address']"
                    input_box = wait.until(EC.presence_of_element_located((
                        By.XPATH, inp_xpath)))
                    string1="Not Given"
                    input_box.send_keys(string1)
                    inp_xpath="/html/body/div/div/form/div[12]/button"
                    input_box = wait.until(EC.presence_of_element_located((
                        By.XPATH, inp_xpath))).click()
                    time.sleep(3)
                    driver.get(link)
                    wait = WebDriverWait(driver, 600)



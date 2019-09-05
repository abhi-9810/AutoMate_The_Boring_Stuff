from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
from random import randint
target = input('Enter name of person/group you want to send message to:')

string = input('Enter your message: ')

n = int(input('Enter number of times you want your message to be sent: '))
#System.setProperty("webdriver.chrome.driver","C:\\Users\\dell.DESKTOP-5VND8PJ\\Desktop\\Whatsapp\\chromedriver.exe");		
		
#Webdriver driver = new ChromeDriver();
driver=webdriver.Chrome(executable_path=r"chromedriver.exe")
#driver = webdriver.Chrome('C:\Users\dell.DESKTOP-5VND8PJ\Downloads\chromedriver_win32.exe') 
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
 
x_arg = '//span[contains(@title, '+ '"' +target + '"'+ ')]'
print(x_arg)
person_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
print(person_title)
person_title.click()
inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@dir="ltr"][@data-tab="1"]'
print("Hi")
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
print(input_box)
for i in range(n):
    temp=randint(0, 9)
    string1=""
    for j in range(0,temp):
        string1+="Hi!! "
    input_box.send_keys(string1 + Keys.ENTER)
    time.sleep(1)

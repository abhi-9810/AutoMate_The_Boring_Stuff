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
from io import StringIO
from io import BytesIO
import string
username=""
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox') 
#driver = webdriver.Chrome(chrome_options=chrome_options)
driver=webdriver.Chrome(executable_path=r"chromedriver.exe")
driver.get("https://www.facebook.com/")
wait = WebDriverWait(driver, 600)
k="//*[@id='email']"
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, k))).send_keys(username)
password_box="//*[@id='pass']"
password_input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, password_box)))
string1=""
password_input_box.send_keys(string1 + Keys.ENTER)
#time.sleep(10)
driver.get('https://www.facebook.com/photo.php?fbid=868158163375523&set=t.1785162845&type=3&theater')
data=set()
for i in range(0,50):
	 print(i)
	 driver.find_element_by_css_selector('body').send_keys(Keys.RIGHT)
	 c=driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
	 c=c.encode('utf-8')
	 soup = BeautifulSoup(c,'html5lib')
	 mydivs = soup.find("img", {"class": "spotlight"})
	 data.add(mydivs['src'])
     
name="image_"
i=1
for image in data:
	try:
		print(image)
		r=requests.get(image)
		content=r.content
		img = Image.open(BytesIO(content))
		name1=name+str(i)+".jpg"
		name3="img1/"+name1
		img.save(name3)
		i+=1 
	except Exception as e:
	    print(e)
	    pass

from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as GoogleOptions
from time import sleep

import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument("-g", "--google", help="Usar Google", action="store_true")
parser.add_argument("-f", "--firefox", help="Usar Firefox", action="store_true")
parser.add_argument("-H", "--headless", help="Headless, es visible o no el navegador", action="store_true")
args = parser.parse_args()

def init_client():
	try:
		if args.google:
			chrome_options = GoogleOptions()
			if args.headless:
				chrome_options.add_argument("--headless")
			driver = webdriver.Chrome(options=chrome_options)

		if args.firefox:
			f_profile = webdriver.FirefoxProfile()
			options = FirefoxOptions()
			if args.headless:
				options.headless = True
			driver = webdriver.Firefox(firefox_profile=f_profile, firefox_options=options)
		driver.set_window_size(1000, 700) # optional
		return driver
	except Exception as e:
		raise e
		return 0

def lock_dispositives(i):
	
		val_ip_div="div"+i.replace(".","")
		try:
			button__mac=driver.find_element_by_xpath("//div[@class='module data']//table//tbody//tr//td[1]//div[@id='"+val_ip_div+"']//..//..//td[6]")
			button__mac.click()
			sleep(2)
			button_ok = driver.find_element_by_id("popup_ok")
			button_ok.click()
			sleep(1)
		except Exception as e:
			pass
		try:
			button__mac=driver.find_element_by_xpath("//div[@class='module forms data']//table//tbody//tr//td[1]//div[@id='"+val_ip_div+"']//..//..//td[5]")
			button__mac.click()
			sleep(2)
			button_ok = driver.find_element_by_id("popup_ok")
			button_ok.click()
			sleep(1)
		except Exception as e:
			# raise e
			pass



def login(driver): 
	username = driver.find_element_by_name("loginUsername")
	username.send_keys("user")
	username = driver.find_element_by_name("loginPassword")
	username.send_keys("password")
	button_login=driver.find_element_by_xpath("//input[@class='btn'][@type='submit']")
	button_login.click()



def unlock(i):
	val_ip_td=i.lower().replace(".",":")
	try:
		button__mac=driver.find_element_by_xpath("//div[@id='blocked-devices']//table[@class='data']//tbody//*//td[text()='"+val_ip_td+"']//..//td[5]")
		button__mac.click()
		sleep(2)
		button_ok = driver.find_element_by_id("popup_ok")
		button_ok.click()
		sleep(1)
	except Exception as e:
		print(e)

driver=init_client()


driver.get("http://10.0.0.1/")
sleep(1)
login(driver)
sleep(1)
driver.get("http://10.0.0.1/connected_devices_computers.asp")

IP_list=["A4.FC.77.96.CE.8F","2C.CC.44.EB.86.D5"]
# IP_list=["7C:91:22:52:24:4E"]"72.7A.C2.80.4A.7B"

for i in IP_list:
	lock_dispositives(i)

sleep(3)
button__par=driver.find_element_by_xpath("//li[@class='nav-parental-control']")
button__par.click()
sleep(2)
button__dev=driver.find_element_by_xpath("//li[@class='nav-devices']")
button__dev.click()

try:

	button__mac=driver.find_element_by_xpath("//label[@id='Enable']") 
	button__mac.click()
	sleep(2)
except Exception as e:
	print(e) 


sleep(5)
for i in IP_list: 
	unlock(i)



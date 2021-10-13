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
			#chrome_options.add_argument("--disable-extensions")
			#chrome_options.add_argument("--disable-gpu")
			#chrome_options.add_argument("--no-sandbox") # linux only
			if args.headless:
				chrome_options.add_argument("--headless")
			# chrome_options.headless = True # also works
			driver = webdriver.Chrome(options=chrome_options)

		if args.firefox:
			# driver=webdriver.PhantomJS(service_args=["--load-images=no"])# or add to your PATH
			f_profile = webdriver.FirefoxProfile()
			# #firefox_profile.set_preference('permissions.default.stylesheet', 2)
			# f_profile.set_preference('permissions.default.image',2)
			options = FirefoxOptions()
			if args.headless:
				options.headless = True
			driver = webdriver.Firefox(firefox_profile=f_profile, firefox_options=options)
		driver.set_window_size(1000, 700) # optional
		# driver.set_window_size(1000, 100) # optional

		# driver.get('https://google.com/')	
		return driver
	except Exception as e:
		raise e
		return 0

def lock_dispositives(i):
	
		val_ip_div="div"+i.replace(".","")
		try:
			#online
			# button__mac=driver.find_element_by_xpath
			# ("//div[@class='module forms data']//table")#[@id='"val_ip_div"']//dl[@type='submit']")
			button__mac=driver.find_element_by_xpath("//div[@class='module data']//table//tbody//tr//td[1]//div[@id='"+val_ip_div+"']//..//..//td[6]")
			#[@id='"val_ip_div"']//dl[@type='submit']")
			# print(button__mac.get_attribute('innerHTML'))
			button__mac.click()
			sleep(2)
			button_ok = driver.find_element_by_id("popup_ok")
			button_ok.click()
			sleep(1)
		except Exception as e:
			# print("no normal")
			# raise e
			pass

		# print(button__mac.get_attribute('innerHTML'))
		# button__mac=driver.find_element_by_xpath("//div[@class='module data']//table")#[@id='"val_ip_div"']//dl[@type='submit']")

		try:
			#offline
			button__mac=driver.find_element_by_xpath("//div[@class='module forms data']//table//tbody//tr//td[1]//div[@id='"+val_ip_div+"']//..//..//td[5]")
			#[@id='"val_ip_div"']//dl[@type='submit']")
			# print(button__mac.get_attribute('innerHTML'))
			button__mac.click()
			# script="return FillinFormBlock('1', '"+IP_list[0].lower()+"', '0.0.0.0', '"+name_list[0]+"', 'yes', this);"
			# driver.execute_script(script)
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


def clean(i):
	print("entra clean")
	# val_ip_div="div"+i.replace(".","")
	val_ip_td=i.lower().replace(".",":")
	try:
		print("entra try clean")

		button__mac=driver.find_element_by_xpath("//div[@id='blocked-devices']//table[@class='data']//tbody//*//td[text()='"+val_ip_td+"']//..//td[4]")
		#[@id='"val_ip_div"']//dl[@type='submit']")
		# print("3")
		print(button__mac.get_attribute('innerHTML'))   #*[text() = 'hello']

		# print(len(button__mac.get_attribute('innerHTML')))
		# button__mac.click()
		# sleep(5)
		# button_ok = driver.find_element_by_id("popup_ok")
		# button_ok.click()
		# sleep(1)

		print("access!")


		#online
		# button__mac=driver.find_element_by_xpath
		# ("//div[@class='module forms data']//table")#[@id='"val_ip_div"']//dl[@type='submit']")
		# button__mac=driver.find_element_by_xpath("//input[@id='Enable']")
		# # [@id='"val_ip_div"']//dl[@type='submit']")
		# print("3")
		# print(button__mac.get_attribute('innerHTML'))   #*[text() = 'hello']

		# print(len(button__mac.get_attribute('innerHTML')))
		# button__mac.click()
		# sleep(2)
		# button_ok = driver.find_element_by_id("popup_ok")
		# button_ok.click()
		# sleep(1)
		# print("enabled!")

# falta acomodar bien la funcion de cambio de horario pero por alguna extraña razon se borra 
# al eliminar el lock entonces nos ahorramos ese paso xd


		# button__mac=driver.find_element_by_xpath("//input[@id='yes']")
		# #[@id='"val_ip_div"']//dl[@type='submit']")
		# # print("3")
		# print(button__mac.get_attribute('innerHTML'))   #*[text() = 'hello']

		# # print(len(button__mac.get_attribute('innerHTML')))
		# button__mac.click()
		# sleep(2)
		# # button_ok = driver.find_element_by_id("popup_ok")
		# # button_ok.click()
		# # sleep(1)
		# print("enabled!")

		# button__mac=driver.find_element_by_xpath("//input[@id='submitButton']")
		# #[@id='"val_ip_div"']//dl[@type='submit']")
		# # print("3")
		# print(button__mac.get_attribute('innerHTML'))   #*[text() = 'hello']

		# # print(len(button__mac.get_attribute('innerHTML')))
		# button__mac.click()
		# sleep(2)
		# # button_ok = driver.find_element_by_id("popup_ok")
		# # button_ok.click()
		# # sleep(1)
		# print("enabled!")

	except Exception as e:
		# print("no normal")
		# raise e
		print(e)
		# pass

def unlock(i):
	print("entra unlock")
	# val_ip_div="div"+i.replace(".","")
	val_ip_td=i.lower().replace(".",":")
	try:
		print("entra try unlock")
		#online
		# button__mac=driver.find_element_by_xpath
		# ("//div[@class='module forms data']//table")#[@id='"val_ip_div"']//dl[@type='submit']")
		button__mac=driver.find_element_by_xpath("//div[@id='blocked-devices']//table[@class='data']//tbody//*//td[text()='"+val_ip_td+"']//..//td[5]")
		#[@id='"val_ip_div"']//dl[@type='submit']")
		print("3")
		print(button__mac.get_attribute('innerHTML'))   #*[text() = 'hello']

		# print(len(button__mac.get_attribute('innerHTML')))
		button__mac.click()
		sleep(2)
		button_ok = driver.find_element_by_id("popup_ok")
		button_ok.click()
		sleep(1)
	except Exception as e:
		# print("no normal")
		# raise e
		print(e)
		# pass

driver=init_client()


driver.get("http://10.0.0.1/")
sleep(1)
login(driver)
sleep(1)
driver.get("http://10.0.0.1/connected_devices_computers.asp")
# driver.get("file:/home/okadath/Desktop/raspberry/bot/Connected Devices - Devices - Technicolor.html")


IP_list=["72.7A.C2.80.4A.7B"]#,"A4.FC.77.96.CE.8F","2C.CC.44.EB.86.D5"]
# IP_list=["7C:91:22:52:24:4E"]
# name_list=["android-f548ef3d855cd36f"]

# a="A4.FC.77.96.CE.8F"
# print(a.lower())
# print(a.replace(".",""))


# item=driver.find_element_by_id("div"+IP_list[0].replace(".",""))



for i in IP_list:
	lock_dispositives(i)

# def 
print("acaba lock")
sleep(3)

# driver.get("http://10.0.0.1/managed_sites.asp")
# driver.get("http://10.0.0.1/connected_devices_computers.asp")

# print("acabo")

# sleep(3)
button__par=driver.find_element_by_xpath("//li[@class='nav-parental-control']")
button__par.click()
sleep(2)
button__dev=driver.find_element_by_xpath("//li[@class='nav-devices']")
button__dev.click()


try:
	# pass

	button__mac=driver.find_element_by_xpath("//label[@id='Enable']")
	# [@id='"val_ip_div"']//dl[@type='submit']")
	print("3")
	print(button__mac.get_attribute('innerHTML'))   #*[text() = 'hello']

	# print(len(button__mac.get_attribute('innerHTML')))
	button__mac.click()
	sleep(2)
	# button_ok = driver.find_element_by_id("popup_ok")
	# button_ok.click()
	# sleep(1)
	print("enabled!")
except Exception as e:
	print(e)
	print("ya enabled?")

# driver.get("http://10.0.0.1//managed_devices.asp")
# print("inicia unlock")

# driver.get("file:/home/okadath/Desktop/raspberry/bot/Parental Control > Managed Devices - Technicolor.html")


sleep(3)
for i in IP_list:
	print("ciclo clean")
	clean(i)


sleep(5)
for i in IP_list:
	print("ciclo unlock")
	unlock(i)



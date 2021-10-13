from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36")
base_url = "https://twitter.com"

def login(driver):
	print("logeando")
	driver.get(base_url)
	time.sleep(1)
	username = driver.find_element_by_name("session[username_or_email]")
	password = driver.find_element_by_name("session[password]")
	time.sleep(1)
	username.send_keys("bototuit@mail.com")
	password.send_keys("Qwerty35$")
	time.sleep(1)
	elem = driver.find_element_by_xpath("//input[@class='EdgeButton EdgeButton--secondary EdgeButton--medium submit js-submit'][@type='submit']")
	elem.click()

try:
	print("1")
	# driver=webdriver.PhantomJS(service_args=["--load-images=no"])# or add to your PATH
	f_profile = webdriver.FirefoxProfile()
	# #firefox_profile.set_preference('permissions.default.stylesheet', 2)
	# f_profile.set_preference('permissions.default.image',2)
	driver = webdriver.Firefox(firefox_profile=f_profile)
	print("2")
	driver.set_window_size(1024, 768) # optional
	# driver.get('https://google.com/')
	login(driver)
	driver.save_screenshot('capturas/screen.png')
	
except Exception as e:
	print("error:",e)
finally:
	print("termino")
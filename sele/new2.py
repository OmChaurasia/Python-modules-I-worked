from selenium import webdriver
import time

options = webdriver.ChromeOptions("C:\\chromedriver\\chromedriver_win32\\chromedriver.exe")
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(chrome_options=options)
driver.get('http://codepad.org')

text_area = driver.find_element_by_id('textarea')
text_area.send_keys("This text is send using Python code.")
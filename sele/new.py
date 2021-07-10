from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

# incognito window

chrome_options.add_argument("--incognito")

path="C:\\chromedriver\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://google.com/")

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"))).send_keys("Om Chaurasia")
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()

try:
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"xjs\"]/table/tbody/tr/td[3]/a"))).click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[8]/div/div/div[1]/a"))).click()
except:
    driver.quit()
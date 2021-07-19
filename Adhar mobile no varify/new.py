from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytesseract as tess
tess.pytesseract.tesseract_cmd= r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
from selenium.webdriver.chrome.options import Options
import cv2 as cv
chrome_options = Options()

chrome_options.add_argument("--incognito")

path="C:\\chromedriver\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://resident.uidai.gov.in/verify-email-mobile")

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div/div[4]/form/div/div[1]/div/div/div/div/div/input"))).send_keys("371825600984")

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div/div[4]/form/div/div[2]/div/div/div[1]/input"))).send_keys("7309370691")

driver.execute_script("window.scrollTo(0, 550)") 


driver.save_screenshot('screenshot.png')
img = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div/div[4]/form/div/div[3]/div[1]/div/div/div[2]/img')
loc = img.location.x
print(loc)
image = cv.imread('screenshot.png')
out = cv.CreateImage((150,60), image.depth, 3)
cv.SetImageROI(image, (loc['x'],loc['y'],150,60))
cv.Resize(image, out)
cv.SaveImage('out.jpg', out)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

TARGET = "space.engineers"

#get instagram login
auth = []
with open("../api/instagram") as file:
    d = file.readlines()
    for dat in d:
        auth.append(str(dat.strip("\n")))



#get web speed data
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#log into instagram
driver.get("https://instagram.com")
time.sleep(1)
cookies = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]')
time.sleep(2)
cookies.click()
username = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
username.send_keys(auth[0])
time.sleep(1)
pw = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
pw.send_keys(auth[1])
time.sleep(2)
pw.send_keys(Keys.ENTER)
time.sleep(5)
no_save = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')
no_save.click()
time.sleep(2)
no_notifications = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
no_notifications.click()

#go to target

search = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search.send_keys(TARGET)
time.sleep(1)
search.send_keys(Keys.ENTER)
search.send_keys(Keys.ENTER)
time.sleep(2)
target_followers = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
target_followers.click()
time.sleep(3)
follow = driver.find_elements(By.TAG_NAME, 'Button')
for follower in follow:
    print(follower.text)




time.sleep(100)
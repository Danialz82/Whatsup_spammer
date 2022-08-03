from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
d = webdriver.Chrome()
d.get("https://web.whatsapp.com/")
names = input("enter names with cama(name1, name2,...) : ")
a = names.split(",")
names = list(a)
msg = input("enter msg :")
time = int(input("enter how many : "))
input("enter ")
#user = d.find_element(By.XPATH , f"//span[@title = '{name}']")
#user.click()
#msg_box = d.find_element(By.CLASS_NAME , "fd365im1")
for y in names:
    user = d.find_element(By.XPATH , f"//span[@title = '{y}']")
    user.click()
    msg_box = d.find_element(By.CLASS_NAME , "fd365im1")
    for i in range(time):
        msg_box.send_keys(msg)
        button = d.find_element(By.XPATH , "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[2]/button")
        button.click()

d.quit()
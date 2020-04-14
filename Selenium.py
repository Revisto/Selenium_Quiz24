

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import time
import random

for i in range (3):

    Url=input("URL:")

    for i in range (30):
        Path="/usr/lib/chromium-browser/chromedriver"
        Drive = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        Drive.get(Url)

        time.sleep(5)
    

        SearchBox = Drive.find_elements_by_class_name("form-control")

        SearchBox[0].send_keys("کلاس شما به دلیل فعالیت های مشکوک بسته شده است")
        SearchBox[0].send_keys(Keys.ENTER)

        SearchBox[1].send_keys("0912"+str(random.randint(1000000,9999999)))
        SearchBox[1].send_keys(Keys.ENTER)



        SearchBox[2].send_keys("1234567")
        SearchBox[2].send_keys(Keys.ENTER)


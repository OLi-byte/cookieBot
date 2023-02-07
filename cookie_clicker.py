from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class cookieClicker:
    def __init__(self):
        self.SITE_LiNK = "https://orteil.dashnet.org/cookieclicker/"
        self.SITE_MAP = {
            "buttons": {
                "cookie": {
                    "xpath": "/html/body/div/div[2]/div[15]/div[8]/button"
                },
                "upgrade": {
                    "xpath": "/html/body/div/div[2]/div[19]/div[3]/div[6]/div[$$$NUMBER$$$]"
                },
                "language_selector": {
                    "xpath": "/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[2]"
                }
            }
        }

        self.driver = webdriver.Chrome(executable_path="chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()

    def open_site(self):
        time.sleep(2)
        self.driver.get(self.SITE_LiNK)
        time.sleep(10)

    def language_selector(self):
        self.driver.find_element(By.XPATH, self.SITE_MAP["buttons"]["language_selector"]["xpath"]).click()
        time.sleep(5)

    def click_cookie(self):
        self.driver.find_element(By.XPATH, self.SITE_MAP["buttons"]["cookie"]["xpath"]).click()

    def get_upgrade(self):
        found = False
        current_element = 2

        while not found:
            item = self.SITE_MAP["buttons"]["upgrade"]["xpath"].replace("$$$NUMBER$$$", str(current_element))
            class_item = self.driver.find_element(By.XPATH, item).get_attribute("class")

            if not "enable" in class_item:
                found = True
            else:
                current_element += 1
        return current_element - 1

    def buy_upgrade(self):
        item = self.SITE_MAP["buttons"]["upgrade"]["xpath"].replace("$$$NUMBER$$$", str(self.get_upgrade()))
        self.driver.find_element(By.XPATH, item).click()

cookie = cookieClicker()
cookie.open_site()
cookie.language_selector()

i = 0

while True:
    if i % 500 == 0 and i != 0:
        time.sleep(1)
        cookie.buy_upgrade()
        time.sleep(1)
    cookie.click_cookie()
    i += 1
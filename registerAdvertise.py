from time import sleep

from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import Constants


class RegisterAdvertise:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Constants.PATH)

        # self.service = Service(executable_path=ChromeDriverManager().install())
        # = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()
        self.driver.get(Constants.BASIC_URL)
        self.action = webdriver.ActionChains(self.driver)

    def enter_to_account(self, mobile_number):
        self.driver.find_element(By.XPATH, "//a[text()='ثبت آگهی']").click()
        sleep(5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='شمارهٔ موبایل']").send_keys(mobile_number)
        sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='kt-button kt-button--primary auth-actions__submit-button']").click()
        sleep(10)

    def category_selection(self,category, sub_category):
        category_list = self.driver.find_elements(By.XPATH,"//p[@class='kt-selector-row__title']")
        category_list_names=[]
        sub_category_names=[]
        for item in category_list:
            category_list_names.append(item.text)
        if category in category_list_names:
            self.driver.find_element(By.XPATH, f"//p[@class='kt-selector-row__title' and text()='{category}']").click()
            sleep(3)
            sub_category_list = self.driver.find_elements(By.XPATH,"//p[@class='kt-selector-row__title']")
            for sub_item in sub_category_list:
                sub_category_names.append(sub_item.text)
            print(sub_category_names)
            if sub_category in sub_category_names:
                self.driver.find_element(By.XPATH, f"//p[@class='kt-selector-row__title' and text()='{sub_category}']").click()
            else:
                print(f"This {sub_category} sub_categpry can not be found!")
        else:
            print(f"This {category} categpry can not be found!")





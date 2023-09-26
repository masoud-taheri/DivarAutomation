from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

import Constants


class Booking:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Constants.PATH)

        #self.service = Service(executable_path=ChromeDriverManager().install())
         #= webdriver.Chrome(service=self.service)
        self.driver.maximize_window()
        self.driver.get(Constants.BASIC_URL)
        self.action = webdriver.ActionChains(self.driver)

    # def __quit__(self):
    #     self.driver.quit()

    def select_city(self, city_name):
        search_box = self.driver.find_element(By.XPATH, "//input[@type='text']")
        cities = self.driver.find_elements(By.XPATH,"//h2[@class='city-card__title-be246']")
        city_list=[]
        for city in cities:
            city_list.append(city.text)
        if city_name in city_list:
            self.driver.find_element(By.XPATH, f"//h2[@class='city-card__title-be246' and text()='{city_name}']").click()
        else:
            search_box.send_keys(city_name)
            try:
                sleep(2)
                self.driver.find_element(By.XPATH,"//div[@role='menu']//div[@class='kt-search-result-row'][1]").click()
            except:
                print(f"There is no city like {city_name}")

    def select_category(self, category, sub_category):
        self.driver.find_element(
            By.XPATH,'//button[@class="kt-dropdown-button kt-dropdown-button--medium kt-dropdown-button--inlined"]').click()
        sleep(3)
        try:
            #self.driver.find_element(By.XPATH,f"//a[@class='kt-accordion-item__header kt-accordion-item__header--with-icon' and text()='{category_name}']").click()
            self.driver.find_element(By.XPATH,f'//span[text()="{category}"]').click()
            self.driver.find_element(By.XPATH,f'//a[text()="{sub_category}"]').click()
        except:
            print(f'There is no category like "{category}"')

    def select_price(self, lowest, highest):
        self.driver.find_element(By.ID, 'khesht-3').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '//div[@class="kt-dropdown-menu kt-select-drop-down kt-ftr__control"][1]').click()
        sleep(2)
        selectable_prices = self.driver.find_elements(By.XPATH, "//li[@class='kt-dropdown-item kt-dropdown-item--small']")
        all_prices = []
        highest_prices = []

        for prices in selectable_prices:
            all_prices.append(prices.text)
        if lowest in all_prices:
            self.driver.find_element(By.XPATH, f"//li[@class='kt-dropdown-item kt-dropdown-item--small' and text()='{lowest} ']").click()
        else:
            self.driver.find_element(By.XPATH, "//li[text()='وارد کردن مقدار دلخواه']").click()
            desired_amount = self.driver.find_element(By.ID, 'min-1088541640')
            desired_amount.send_keys(lowest)
            desired_amount.send_keys(Keys.ENTER)
        sleep(2)

        self.driver.find_element(By.XPATH,
                                 "//div[@class='kt-dropdown-menu kt-select-drop-down kt-ftr__control'][2]").click()
        if highest in all_prices:
            self.driver.find_element(By.XPATH, f"//li[@class='kt-dropdown-item kt-dropdown-item--small' and text()='{highest} ']").click()
        else:
            self.driver.find_element(By.XPATH, "//li[text()='وارد کردن مقدار دلخواه']").click()
            desired_amount = self.driver.find_element(By.ID, 'max-1088541640')
            desired_amount.send_keys(highest)
            desired_amount.send_keys(Keys.ENTER)
        sleep(2)













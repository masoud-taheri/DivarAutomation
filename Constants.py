from selenium import webdriver

BASIC_URL='https://divar.ir/'
PATH="C:\chromedriver\chromedriver.exe"


def __init__(self):
    self.driver = webdriver.Chrome(executable_path=PATH)

    # self.service = Service(executable_path=ChromeDriverManager().install())
    # = webdriver.Chrome(service=self.service)
    self.driver.maximize_window()
    self.driver.get(BASIC_URL)
    self.action = webdriver.ActionChains(self.driver)
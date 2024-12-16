from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    JAVA_SCRIPT_ALERTS_LINK = (By.LINK_TEXT, 'JavaScript Alerts')
    def navigate_to_homepage(self):
        self.driver.get('https://the-internet.herokuapp.com/')
    def click_javascript_alerts_link(self):
        self.driver.find_element(*self.JAVA_SCRIPT_ALERTS_LINK).click()
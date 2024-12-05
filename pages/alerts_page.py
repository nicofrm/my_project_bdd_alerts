from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AlertsPage(BasePage):
    ALERT_CONFIRM = (By.XPATH, '//button[contains(text(), "Click for JS Alert")]')
    ALERT_CONFIRM_RESULT_TEXT = (By.ID, 'result')

    def click_javascript_alert(self):
        self.driver.find_element(*self.ALERT_CONFIRM).click()

    def accept_alert(self):
        self.driver.switch_to_alert.accept()

    def check_alert_results_text(self, alert_text):
       actual_text = self.driver.find_element(*self.ALERT_CONFIRM_RESULT_TEXT).text
       assert alert_text == actual_text, f"Error: Expected text: {alert_text}, Actual text: {actual_text} "

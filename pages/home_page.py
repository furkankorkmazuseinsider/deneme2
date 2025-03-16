from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    COMPANY_MENU = (By.XPATH, "//a[contains(text(),'Company')]")
    CAREERS_LINK = (By.XPATH, "//a[contains(text(),'Careers')]")

    def navigate_to_careers(self):
        self.click_element(self.COMPANY_MENU)
        self.click_element(self.CAREERS_LINK)

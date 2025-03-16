import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CareersPage(BasePage):
    LOCATIONS_SECTION = (By.XPATH, "//h2[contains(text(),'Locations')]")
    TEAMS_SECTION = (By.XPATH, "//h2[contains(text(),'Teams')]")
    LIFE_AT_INSIDER_SECTION = (By.XPATH, "//h2[contains(text(),'Life at Insider')]")
    QA_JOBS_BUTTON = (By.XPATH, "//a[contains(text(),'See all QA jobs')]")
    SEE_ALL_TEAMS = (By.XPATH, "//a[contains(text(),'See all teams')]")
    QUALITY_ASSURANCE = (By.XPATH, "//h3[text()='Quality Assurance']/ancestor::a")

    def navigate_to_qa_jobs(self):
        button = self.find_element(self.SEE_ALL_TEAMS)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",button)
        time.sleep(1)
        button.click()
        qa_section = self.find_element(self.QUALITY_ASSURANCE)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", qa_section)
        time.sleep(1)
        qa_section.click()
        
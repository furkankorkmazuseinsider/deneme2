from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver import ActionChains
import time


class QAJobsPage(BasePage):
    LOCATIONS_SECTION = (By.XPATH, "//h2[contains(text(),'Locations')]")
    TEAMS_SECTION = (By.XPATH, "//h2[contains(text(),'Teams')]")
    LIFE_AT_INSIDER_SECTION = (By.XPATH, "//h2[contains(text(),'Life at Insider')]")
    LOCATION_FILTER = (By.XPATH, "//span[contains(text(),'Location')]")
    ISTANBUL_OPTION = (By.XPATH, "//span[contains(text(),'Istanbul, Turkey')]")
    DEPARTMENT_FILTER = (By.XPATH, "//span[contains(text(),'Department')]")
    JOB_LISTINGS = (By.XPATH, "//div[@class='job-listing']")
    VIEW_ROLE_BUTTON = (By.XPATH, "//a[contains(text(), 'View Role')]")
    QA_JOBS_BUTTON = (By.XPATH, "//a[contains(text(),'See all QA jobs')]")
    JOB_LISTING = (By.XPATH, "//div[contains(@class, 'position-list-item-wrapper')]")

    def filter_jobs(self):
        self.click_element(self.QA_JOBS_BUTTON)
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0, 800);")
        time.sleep(5)
        job_listing = self.find_element(self.JOB_LISTING)
        actions = ActionChains(self.driver)
        actions.move_to_element(job_listing).perform()
        view_role_button = self.find_element(self.VIEW_ROLE_BUTTON)
        view_role_button.click()
        time.sleep(3)

        """self.click_element(self.LOCATION_FILTER)
        time.sleep(2)
        self.click_element(self.ISTANBUL_OPTION)
        self.click_element(self.DEPARTMENT_FILTER)
        self.click_element(self.QA_OPTION)
        time.sleep(2)"""

    def verify_job_listings(self):
        jobs = self.find_elements(self.JOB_LISTINGS)
        assert len(jobs) > 0, "No job listings found for QA in Istanbul"

        for job in jobs:
            position = job.find_element(By.XPATH, ".//span[contains(@class, 'position')]").text
            department = job.find_element(By.XPATH, ".//span[contains(@class, 'department')]").text
            location = job.find_element(By.XPATH, ".//span[contains(@class, 'location')]").text
            assert "Quality Assurance" in position, f"Position '{position}' does not contain 'Quality Assurance'"
            assert "Quality Assurance" in department, f"Department '{department}' does not contain 'Quality Assurance'"
            assert "Istanbul, Turkey" in location, f"Location '{location}' does not contain 'Istanbul, Turkey'"

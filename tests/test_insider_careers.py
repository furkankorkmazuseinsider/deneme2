import time
import unittest
import pytest
import self
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.careers_page import CareersPage
from pages.home_page import HomePage
from pages.qa_jobs_page import QAJobsPage


@pytest.fixture(scope="function")
def driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-notifications')

    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def test_insider_careers(driver):
    home_page = HomePage(driver)
    home_page.driver.get("https://useinsider.com")
    print("✅ Insider Homepage loaded successfully.")
    home_page.navigate_to_careers()
    careers_page = CareersPage(driver)
    careers_page.navigate_to_qa_jobs()
    qa_jobs_page = QAJobsPage(driver)
    qa_jobs_page.filter_jobs()
    #qa_jobs_page.verify_job_listings()

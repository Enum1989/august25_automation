from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest



@pytest.fixture()
def browser():
   chrome_browser = webdriver.Chrome()
   chrome_browser.maximize_window()
   return chrome_browser

def test_massage(driver):
    driver.get()
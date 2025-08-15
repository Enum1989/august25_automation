import pytest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver


  
def test_open_s6(browser):
    browser.get('https://demoblaze.com')
    galaxy_s6 = browser.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
    galaxy_s6.click()
    title = browser.find_element(By.CSS_SELECTOR, 'h2.name')
    assert title.text == 'Samsung galaxy s6'

def test_two_monitors(browser):
        browser.get('https://demoblaze.com')
        monitor_link = browser.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
        monitor_link.click()
        time.sleep(2)
        monitors = browser.find_elements(By.CSS_SELECTOR,'.card')
        assert len(monitors) == 2
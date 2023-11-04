import os

import webdriver_manager.firefox
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def createDriver(headless=True):
    s = Service(f"geckodriver.exe")
    options = webdriver.FirefoxOptions()
    if headless:
        options.add_argument('--headless')  # headless or not
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-setuid-sandbox")
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("privacy.trackingprotection.enabled", False)
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0'
    options.set_preference("general.useragent.override", user_agent)

    driver = webdriver.Firefox(service=s, options=options)
    driver.set_window_size(1920, 1080)
    return driver

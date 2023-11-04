import traceback
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait(driver, xpath, delay=20, debug=True):
    try:
        WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    except:
        if debug:
            driver.save_screenshot(
                f"Logs/Imgs/wait_error_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.jpg")
            print(f"Cannot find {xpath} Traceback")
            print(traceback.format_exc())
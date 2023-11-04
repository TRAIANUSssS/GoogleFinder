import time
import traceback

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Selenium.findElementByXpathToSelenium import search


def click(driver, xpathOrElement, debug=True, timer=2):
    try:
        if type(xpathOrElement).__name__ == "str":
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpathOrElement)))
            element = search(driver, xpathOrElement, debug=debug)
        else:
            element = xpathOrElement
        if 'firefox' in driver.capabilities['browserName']:
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto',block: 'center',inline: 'center'});", element)
        ActionChains(driver).scroll_to_element(element).move_to_element(element).click(element).perform()
        time.sleep(timer)
        return element
    except:
        if debug:
            print(xpathOrElement)
            print(traceback.format_exc())
        return None

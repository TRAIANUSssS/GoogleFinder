import time
import traceback
from datetime import datetime

from Selenium.StartSelenium import createDriver


class Scrapping(object):
    def __init__(self, headless: bool):
        self.headless = headless

    def create_driver(self):
        self.driver = createDriver(headless=self.headless)
        try:
            self.child.doAfterCreateDriver()
        except:
            self.driver.switch_to.default_content()
            self.driver.save_screenshot(
                f"Logs/Imgs/{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.jpg")
            print(traceback.format_exc())
        finally:
            time.sleep(3)
            self.driver.close()
            self.driver.quit()
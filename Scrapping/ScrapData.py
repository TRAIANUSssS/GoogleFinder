import time
import traceback
from datetime import datetime

from Selenium.SeleniumClick import click
from Selenium.StartSelenium import createDriver
from Selenium.WaitUntilElementClickable import wait
from Scrapping import Constants as con
from Scrapping import Link_file
from Scrapping import ParsePage


class Scrapping(object):
    def __init__(self, headless: bool):
        self.headless = headless

        self.driver = None

    def create_driver(self):
        self.driver = createDriver(headless=self.headless)
        try:
            self.start_parse()
        except:
            self.driver.switch_to.default_content()
            self.driver.save_screenshot(
                f"Logs/Imgs/{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.jpg")
            print(traceback.format_exc())
        finally:
            time.sleep(3)
            self.driver.close()
            self.driver.quit()

    def start_parse(self):
        self.driver.get(con.MAP_URL)
        self.get_data_from_page()

        while not Link_file.stop_parsing:
            print("PARSING!!!")
            time.sleep(1)

    def get_data_from_page(self):
        page_parse_obj = ParsePage.ParsePage(self.driver.page_source)
        page_parse_obj.find_data()

    def next(self):
        click(self.driver, "//button[@id = 'go-button']")
        wait(self.driver, "//button[@id = 'go-button']", delay=20, debug=True)
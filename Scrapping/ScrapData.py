import time
import traceback
from datetime import datetime

from PickleFiles.GetIndex import find_index
from Selenium.SeleniumClick import click
from Selenium.StartSelenium import createDriver
from Selenium.WaitUntilElementClickable import wait
from Scrapping import Constants as con
from Scrapping import Link_file
from Scrapping import ParsePage
from PickleFiles.WriteToPickleFile import write


class Scrapping(object):
    def __init__(self, headless: bool):
        self.headless = headless
        self.global_iteration = find_index()
        self.current_iteration = 0

        self.errors = 0

        self.start_time_datetime_format = datetime.now()
        self.start_time_time_format = time.time()

        self.driver = None
        self.data = []

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

        self.start_time_datetime_format = datetime.now()
        self.start_time_time_format = time.time()

        while not Link_file.stop_parsing:
            try:
                self.get_data_from_page()
                self.next()
            except:
                print(traceback.format_exc())
                self.errors += 1

    def get_data_from_page(self):
        page_parse_obj = ParsePage.ParsePage(self.driver.page_source)
        page_parse_obj.find_data()
        self.data = page_parse_obj()
        result = write(self.data, self.global_iteration + self.current_iteration)
        self.current_iteration += result
        self.print_stat()

    def next(self):
        click(self.driver, "//button[@id = 'go-button']")
        wait(self.driver, "//button[@id = 'go-button']", delay=20, debug=True)

    def print_stat(self):
        time_spend = datetime.now() - self.start_time_datetime_format
        time_per_iteration = (time.time() - self.start_time_time_format) / self.current_iteration
        hour_iteration_count = 3600 / time_per_iteration

        left_sec = (100000 - self.global_iteration + self.current_iteration) * time_per_iteration
        days = int(left_sec // 86400)
        hours = int((left_sec % 86400) // 3600)
        mins = int(((left_sec % 86400) % 3600) // 60)
        secs = int(((left_sec % 86400) % 3600) % 60)

        print(f"\rtime spend: {time_spend}, "
              f"{round(time_per_iteration, 2)} sec/iter, "
              f"{round(hour_iteration_count, 2)} iter/h, "
              f"curr iter: {self.current_iteration}, "
              f"total iter: {self.global_iteration + self.current_iteration}, "
              f"time left {days}:{hours}:{mins}:{secs}, "
              f"errors: {self.errors} "
              f"data: {self.data}", end="")

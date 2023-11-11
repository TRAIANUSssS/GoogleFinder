from Scrapping import SepThreads, ScrapData


def scrap_data():
    SepThreads.create_waiting_thread()
    scrap_obj = ScrapData.Scrapping(headless=True)
    scrap_obj.create_driver()


if __name__ == "__main__":
    scrap_data()

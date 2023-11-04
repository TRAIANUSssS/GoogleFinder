import json

from bs4 import BeautifulSoup


class ParsePage(object):
    def __init__(self, source: str):
        self.source = source
        self.soup = None

    def get_soup_page(self):
        soup = BeautifulSoup(self.source, "html.parser")
        return soup

    def find_data(self):
        self.soup = self.get_soup_page()
        print(self.soup.prettify())


        panoId = self.get_panoID()

    def find_link(self):
        link = self.soup.find("div", {"class": "gm-iv-address-link"}).find("a").get("href")
        

    def get_panoID(self):
        script_list = self.soup.find_all('script', type='text/javascript')

        script = self.find_script(script_list)
        if script is not None:
            panoID = self.find_panoID_from_script(script)
            return panoID
        else:
            print("Cannot find script element with panoID")
            return None

    def find_script(self, script_list: list):
        for script in script_list:
            if not script.has_attr('src'):
                return script.text
        else:
            return None

    def find_panoID_from_script(self, script: str):
        print(script)
        splited_script = script.split("\n")
        for line in splited_script:
            if line.count("initPanoId"):
                panoID = line[line.find('"')+1:line.find(';')-1]
                print("panoID:", panoID)
                return panoID
        return None


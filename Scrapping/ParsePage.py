import json

from bs4 import BeautifulSoup


class ParsePage(object):
    def __init__(self, source: str):
        self.source = source
        self.soup = None
        self.info_dict = []

    def get_soup_page(self):
        soup = BeautifulSoup(self.source, "html.parser")
        return soup

    def __call__(self, *args, **kwargs):
        return self.info_list

    def find_data(self):
        self.soup = self.get_soup_page()

        link, world_position, pano_ID = self.find_position_in_world()
        self.info_list = [world_position, pano_ID, link]
        # print(self.info_list)

    def find_position_in_world(self):
        link = self.soup.find("div", {"class": "gm-iv-address-link"}).find("a").get("href")

        info_line = link[link.find("@") + 1:link.find("/data")]
        splited_line = info_line.split(",")
        latitude = splited_line[0]
        longitude = splited_line[1]
        angle_X = [element for element in splited_line if element.count("h")]
        angle_X = angle_X[0] if len(angle_X) > 0 else None
        angle_Y = [element for element in splited_line if element.count("t")]
        angle_Y = angle_Y[0] if len(angle_Y) > 0 else None

        world_position = [latitude, longitude, angle_X, angle_Y]

        if link.find("!2e0?source=apiv3") != -1:
            pano_ID = link[:link.find("!2e0?source=apiv3")]
        else:
            pano_ID = link[:link.find("!2e10?source=apiv3")]
        pano_ID = pano_ID.split("!")[-1].replace("1s", "")
        # print(link)
        # print(world_position)
        return link, world_position, pano_ID

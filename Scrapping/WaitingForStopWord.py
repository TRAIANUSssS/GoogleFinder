from Scrapping import Link_file


class Waiting(object):
    def wait(self):
        stop_word = ""
        while stop_word != "stop" and stop_word != "s":
            stop_word = input("input 'stop' or 's' for stop scrapping\n")
        print("parsing stopped")
        Link_file.stop_parsing = True

    def start_waiting(self):
        if not Link_file.stop_parsing:
            Link_file.stop_parsing = False
        self.wait()

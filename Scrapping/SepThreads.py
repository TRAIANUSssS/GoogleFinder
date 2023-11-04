import traceback
from threading import Thread

from Scrapping.WaitingForStopWord import Waiting


class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        if self.name == 'Scrap_data':
            pass
        if self.name == 'waiting_for_stop':
            waiting_obj = Waiting()
            waiting_obj.start_waiting()


def create_waiting_thread():
    try:
        windowThread = MyThread('waiting_for_stop')
        windowThread.daemon = False
        windowThread.start()
    except:
        print(traceback.format_exc())

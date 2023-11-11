import os
import pickle


def write(data: list, iteration: int):
    PATH = f"{os.getcwd()}/Data/Separated/{iteration // 100}.pkl"
    if len(data) != 0:
        if os.path.exists(PATH):
            old_data = pickle.load(open(PATH, "rb"))
        else:
            old_data = []
        pickle.dump(old_data + [data], open(PATH, "wb"))
        return True
    return False

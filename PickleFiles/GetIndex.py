import os
import pickle


def find_index():
    files = os.listdir(f"{os.getcwd()}/Data/Separated/")
    max_index = -1

    for file in files:
        if file.count(".pkl"):
            index = file.replace(".pkl", "")
            if int(index) > max_index:
                max_index = int(index)

    if max_index != -1:
        data = pickle.load(open(f"{os.getcwd()}/Data/Separated/{max_index}.pkl", "rb"))
        index = max_index * 100 + len(data)
        print("index is:", index)
        print("\n")

        return index
    else:
        return 0

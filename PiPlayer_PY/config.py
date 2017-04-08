#Music Directories
#Database File
from os import open
from json import load, json_data

def loadConfig(path):
    try:
        with open(path) as json_data:
            d = load(json_data)
            json_data.close()
            return d
    except IOError as e:
        raise e


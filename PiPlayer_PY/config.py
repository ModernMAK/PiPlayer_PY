#Music Directories
#Database File
import os
import json

def loadConfig(path):
    try:
        with open(path) as json_data:
            d = json.load(json_data)
            json_data.close()
            return d
    except IOError as e:
        raise e
        #handle this later     
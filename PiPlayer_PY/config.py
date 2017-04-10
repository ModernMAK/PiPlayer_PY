#Music Directories
#Database File
import json
import os 

def loadConfig(path:str):
    try:
        with os.open(path) as json_data:
            d = json.load(json_data)
            json_data.close()
            return d
    except IOError as e:
        raise e



# Json files manager

import json
import os

prjPath = 'C:\Users\Ivan\YandexDisk\Work_sinc\scripts\py_scripts\pw_course'
jsonName = 'settings.json'

class settings(object):
    def __init__(self):
        self.fullPath = os.path.join(prjPath, jsonName)
        if not os.path.exists(self.fullPath):
            a = {}
            json.dump(a, open(self.fullPath, 'w'), indent=4)

    def __readFile(self):
        return json.load(open(self.fullPath, 'r'))


    def __writeFile(self, data):
        return json.dump(data, open(self.fullPath, 'w'), indent=4)

    def readSettings(self):
        data = self.__readFile()
        return data

    def writeSetings(self, data):
        data = self.__writeFile(data)
        return data

    def readValue(self, key):
        data = self.__readFile()
        return data[key]

    def writeValue(self, key, value):
        data = self.__readFile()
        data[key] = value
        self.__writeFile(data)

s = settings()
# s.writeValue('key1', 3)
# s.writeValue('key2', 333)
# s.readValue('key1')
# data = s.readSettings()
# d = {'key4':333, 'key5':666}
# s.writeSetings(d)
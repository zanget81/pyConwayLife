import json

from ___init___.constants import Constants

class AppLocale(object):
    resourceTable = {}

    def __init__(self, locale):
        filePath = Constants.TEXT + '/' + locale + '/' + 'resources.json'

        with open(filePath) as f:
            self.resourceTable = json.loads(f.read())

    def getString(self, str):
        return self.resourceTable.get(str, str)
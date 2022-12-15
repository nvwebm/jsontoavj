from Converter.Converter import handleJsonString
import json
class JsonBridge:
    __jsonString = {}
    __avjScheme = None

    def setJson(self, jsonString):
        self.__jsonString = jsonString

    def convertToAvj(self):
        self.__avjScheme = handleJsonString(self.__jsonString)

    def getScheme(self):
        return json.dumps(self.__avjScheme)

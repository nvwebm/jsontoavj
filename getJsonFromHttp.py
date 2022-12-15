from Converter import JsonBridge
import requests


class httpJson(JsonBridge):
    __response = '{}'
    def __init__(self, url):
        self.__url = url
    def fetchJson(self):
        self.__response = requests.get(self.__url)    
    def setJsonFromResponse(self):
        self.setJson(self.__response.text)    

jsonGetter = httpJson('https://jsonplaceholder.typicode.com/posts/1')
jsonGetter.fetchJson()
jsonGetter.setJsonFromResponse()
jsonGetter.convertToAvj()
print(jsonGetter.getScheme())

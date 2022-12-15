from Converter import JsonBridge


class fileJson(JsonBridge):
    __fileContent = '{}'

    def __init__(self, filePath):
        self.__filePath = filePath

    def fetchJson(self):
        content = '{}'
        with open(self.__filePath, 'r', encoding = 'utf-8') as f:
            content = f.readlines()
        self.__fileContent = "".join(content)

    def setJsonFromFile(self):
        self.setJson(self.__fileContent)


jsonGetter = fileJson('example.json')
jsonGetter.fetchJson()
jsonGetter.setJsonFromFile()
jsonGetter.convertToAvj()
print(jsonGetter.getScheme())

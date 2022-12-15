import json
import numbers
def parseJson(jsonString):
    return json.loads(jsonString)


def handleJsonObject(jsonObj):
    return buildAvjScheme(jsonObj)

def buildAvjScheme(jsonObj):
    scheme = {}
    for field in jsonObj:
        scheme[field] = getValueType(jsonObj[field])
        if (scheme[field] == "object"):
            scheme[field] = buildAvjScheme(jsonObj[field])
    return scheme


def getValueType(value):
    if isinstance(value, numbers.Number):
        return "number"
    if isinstance(value, str):
        return "string"
    if isinstance(value, list):
        return "array"
    if isinstance(value, dict):
        return "object"
    return None

def handleJsonString(jsonString):
    jsonObj = parseJson(jsonString)
    scheme = handleJsonObject(jsonObj)
    return scheme


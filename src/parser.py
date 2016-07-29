import json

class DataParser(object):

    def parse(self, jsonFilePath, objectHook):
        mappingPathList = []
        jsonList = self.readJson(jsonFilePath)
        for jsonData in jsonList:
            jsonStr = json.dumps(jsonData)
            obj = json.loads(jsonStr, object_hook = objectHook)
            mappingPathList.append(obj)
        return mappingPathList

    def readJson(self, filePath):
        with open(filePath) as jsonFile:
            json_data = json.load(jsonFile)
        return json_data
	    



class PathConverter(object):

    def __init__(self, correlatePathList):
        self.__correlatePathList = correlatePathList

    def convert(self, filePath):
        return self.__replacePath(filePath)

    def __replacePath(self, filePath):
        if len(filePath) == 0:
            raise Exception('No file is staged status')

        for correlatePath in self.__correlatePathList:
            if correlatePath.srcPath in filePath:
                return correlatePath.convertPath(filePath)
        raise Exception('"%s" cannot found any correlate path.' % filePath)

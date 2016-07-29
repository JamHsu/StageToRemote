import utils
from abc import ABCMeta, abstractmethod

class BaseObject(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def hook(self, dct):
        """
        this is class method, override it with @classmethod!
        """
        pass

class CorrelatePath(BaseObject):

    def __init__(self, name, srcPath, targetPath):
        self.__name = name
        self.__srcPath = utils.removeStartSlash(srcPath)
        self.__targetPath = utils.appendStartSlash(targetPath)

    def __str__(self):
        return 'name:%s, src:%s, target:%s' % (self.__name, self.__srcPath, self.__targetPath)

    @property
    def name(self):
        return self.__name

    @property
    def srcPath(self):
        return self.__srcPath

    @property
    def targetPath(self):
        return self.__targetPath

    def convertPath(self, fullPath):
        if self.__srcPath in fullPath:
            return fullPath.replace(self.__srcPath, self.__targetPath)
        return fullPath

    @classmethod
    def hook(self, dct):
        return self(dct['name'], dct['src'], dct['target'])
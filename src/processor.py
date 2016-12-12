import config
import converter
import json
import parser
import paramiko
import logger
import model
import ssh
import utils

from abc import ABCMeta, abstractmethod
from scp import SCPClient
from git import Repo

class BaseProcessor(object):
    __metaclass__ = ABCMeta

    def __init__(self, start_code, end_code):
        self.__logger = logger.createLogger(self.__class__.__name__)
        self.__configInfo = config.ConfigInfo('config.ini')
        repoPath = self.__configInfo.repo_path
        self.__rootPath = utils.appendEndSlash(repoPath)
        self.__start_commit_code = start_code
        self.__end_commit_code = end_code

    @property
    def logger(self):
        return self.__logger
    
    @property
    def configInfo(self):
        return self.__configInfo

    @property
    def rootPath(self):
        return self.__rootPath

    def process(self):
        self.logger.debug('---- Start Process ----')

        repoPath = self.configInfo.repo_path
        diffFilesPath = findDiffStagedFile(repoPath,
                                           self.__start_commit_code,
                                           self.__end_commit_code)
        mappingPathList = parser.DataParser().parse('correlate_path.json', model.CorrelatePath.hook)
        self.do_process(mappingPathList, diffFilesPath)

        self.logger.debug('---- End Process ----')

    @abstractmethod
    def do_process(self, mappingPathList, diffFilesPath):
        pass

class AutoProcessor(BaseProcessor):

    def do_process(self, mappingPathList, diffFilesPath):
        sshConnection = ssh.SSHConnection(self.configInfo.ssh_ip, self.configInfo.ssh_acount, self.configInfo.ssh_password)
        success = 0
        fails = 0
        pathConverter = converter.PathConverter(mappingPathList)
        for file_path in diffFilesPath.split('\n'):
            try:
                source = self.rootPath + file_path
                remote = pathConverter.convert(file_path)
                sshConnection.copyFile(source, remote)
                self.logger.info("copy file from %s to %s" % (source, remote))
                success += 1
            except Exception as e:
                fails += 1
                self.logger.exception(e.message)

        self.logger.debug('Total copy %d files to %s.' % (success, self.configInfo.ssh_ip))
        self.logger.debug('Total %d files copy failed.' % fails)

class PrintCmdProcessor(BaseProcessor):

    def do_process(self, mappingPathList, diffFilesPath):
        simpleCmdGenerate = SimpleScpCmd(self.configInfo.ssh_ip, self.configInfo.ssh_acount)
        pathConverter = converter.PathConverter(mappingPathList)
        for file_path in diffFilesPath.split('\n'):
            try:
                source = self.rootPath + file_path
                remote = pathConverter.convert(file_path)
                self.logger.info(simpleCmdGenerate.toCmd(source, remote))
            except Exception as e:
                self.logger.warn(e.message)

class SimpleScpCmd(object):

    def __init__(self, ip, account):
        self.__defaultRemotePrefix = account + '@' + ip + ':'

    def toCmd(self, source, target):
        target = self.__defaultRemotePrefix + target
        return "scp %s %s" % (source, target)

def findDiffStagedFile(repoPath, start, end):
    repo = Repo(repoPath)
    if start and end:
        diffFiles = repo.git.diff(start, end, '--name-only')
    else:
        diffFiles = repo.git.diff('--staged', '--name-only')
    return diffFiles






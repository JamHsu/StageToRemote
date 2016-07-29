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

    def __init__(self, *args, **kwargs):
        self.__logger = logger.createLogger(self.__class__.__name__)
        self.__configInfo = config.ConfigInfo('config.ini')
        repoPath = self.__configInfo.repo_path
        diffFilesPath = findDiffStagedFile(repoPath)
        self.__rootPath = utils.appendEndSlash(repoPath)

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
        diffFilesPath = findDiffStagedFile(repoPath)
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
                self.logger.warn(e.message)

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

def findDiffStagedFile(repoPath):
    repo = Repo(repoPath)
    diffFiles = repo.git.diff('--staged', '--name-only')
    # diffFiles = repo.git.diff('6a4f56f', '3982f81', '--name-only')
    return diffFiles
# class AutoDeployProcessor(object):

#     def __init__(self, *args, **kwargs):
#         self._logger = logger.createLogger(__name__)

#     def process(self):
        
#         self._logger.debug('---- Start Process ----')

#         configInfo = config.ConfigInfo('config.ini')
#         repoPath = configInfo.repo_path
#         diffFiles = findDiffStagedFile(repoPath)
#         rootPath = appendSlash(repoPath)
#         mappingPathList = parser.DataParser().parse('mapping_path.json')
#         simpleCmdGenerate = SimpleScpCmd(configInfo.ssh_ip, configInfo.ssh_acount)
#         # sshConnection = SSHConnection(configInfo.ssh_ip, configInfo.ssh_acount, configInfo.ssh_password)

#         success = 0
#         fails = 0
#         pathConverter = converter.PathConverter(mappingPathList)
#         for file_path in diffFiles.split('\n'):
#             try:
#                 source = rootPath + file_path
#                 remote = pathConverter.convert(file_path)
#                 self._logger.debug(simpleCmdGenerate.toCmd(source, remote))
#                 # sshConnection.copyFile(source, pathConverter.convert(file_path))
#                 # self._logger.debug("copy file from %s to %s" % (local, remote))
#                 success += 1
#             except Exception as e:
#                 fails += 1
#                 self._logger.warn(e.message)

#         self._logger.debug('Total copy %d files to %s.' % (success, configInfo.ssh_ip))
#         self._logger.debug('Total %d files copy failed.' % fails)

#         self._logger.debug('---- End Process ----')




# class SSHConnection(object):

#     def __init__(self, host, user, password):
#         self.__logger = logger.createLogger(__name__)
#         self.__ssh = paramiko.SSHClient()
#         self.__ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         self.__ssh.connect(hostname=host, username=user, password=password)

#     def __del__(self):
#         self.__ssh.close()

#     def copyFile(self, local, remote):
#         try:
#             with SCPClient(self.__ssh.get_transport()) as scp:
#                 scp.put(local, remote)
#         except Exception as e:
#             self.logger.exception('Copy file occur exception.')

#     def execCommand(self, cmd):
#         return self.__ssh.exec_command(cmd)






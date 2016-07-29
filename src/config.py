from ConfigParser import SafeConfigParser

class ConfigInfo(object):

    def __init__(self, configFilePath):
        parser = SafeConfigParser()
        parser.read(configFilePath)
        self.__repoPath = parser.get('Repo', 'repo_path')
        self.__ssh_ip = parser.get('SSH', 'ip')
        self.__ssh_account = parser.get('SSH', 'user')
        self.__ssh_password = parser.get('SSH', 'password')

    @property
    def repo_path(self):
        return self.__repoPath

    @property
    def ssh_ip(self):
        return self.__ssh_ip

    @property
    def ssh_acount(self):
        return self.__ssh_account

    @property
    def ssh_password(self):
        return self.__ssh_password

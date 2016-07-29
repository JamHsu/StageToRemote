import paramiko

class SSHConnection(object):

    def __init__(self, host, user, password):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=host, username=user, password=password)

    def __del__(self):
        self.ssh.close()

    def copyFile(self, local, remote):
        print "copy file from %s to %s" % (local, remote)
        with SCPClient(self.ssh.get_transport()) as scp:
            scp.put(local, remote)

    def execCommand(self, cmd):
        return self.ssh.exec_command(cmd)
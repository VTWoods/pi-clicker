import subprocess
import paramiko
from paramiko import client

# Devices
TV = 1
AUDIO = 2

# Codes
POWER_ON = 1
POWER_OFF = 2
device_map = {
    AUDIO : 'Audio',
    TV : 'VizioTv',
}
code_map = {
    POWER_ON : 'KEY_POWER',
    POWER_OFF : 'KEY_POWER2',
}

class LircCommander(object):
    instance = None

    def SetupSsh(self):
        ssh_client = client.SSHClient()
        ssh_client.load_system_host_keys()
        ssh_client.set_missing_host_key_policy(
            paramiko.AutoAddPolicy())
        ssh_client.connect('10.0.0.122',
                           username='pi')
        self.client = ssh_client

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(LircCommander, cls).__new__(
                                cls, *args, **kwargs)
            cls.instance.SetupSsh()
        return cls.instance

    def send(self, device, code):
        device = device_map[device]
        code = code_map[code]
        command = 'irsend SEND_ONCE %s %s' % (device, code)
        print 'Sending %s to %s' % (device, code)
        self.client.exec_command(command)

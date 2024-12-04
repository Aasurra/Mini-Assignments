#student name: Michael Lin
#student ID: 101484021

import paramiko
from datetime import datetime

class SSHClient:
    def __init__(self, hostname, port, username, password):
        self.__hostname = hostname
        self.__port = port
        self.__username = username
        self.__password = password
        self.__client = None
        self.__shell = None
        self.connect()

    def connect(self):
        self.__client = paramiko.SSHClient()
        self.__client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.__client.connect(hostname = self.__hostname, port = self.__port, username = self.__username, password = self.__password)

    def invoke_shell(self):
        self.__shell = self.__client.invoke_shell()
        return self.__shell

    def start_command_exec(self):
        self.__shell = self.invoke_shell()

    def exec_command(self, command):
        stdin, stdout, stderr = self.__client.exec_command(command)
        output = stdout.read().decode('utf-8') + stderr.read().decode('utf-8')
        return output

    def save_output(self, output):
        today = datetime.now()
        year = today.strftime("%Y")
        month = today.strftime("%B")
        day = today.strftime('%d')
        hour = today.strftime("%H")
        minute = today.strftime("%M")
        filename = f"command_{day}_{month}_{year}-{hour}{minute}.txt"
        with open(filename, 'w') as file:
            file.write(output)

    def __del__(self):
        if self.__client:
            self.__client.close()
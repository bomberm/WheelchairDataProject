#!/usr/bin/env python

import base64
import paramiko
import readTestFile

def sshConnect():
        testData = readTestFile.readFile("test.test")
        sshIP = str(testData['IP'])
        sshPort = int(testData['port'])
        sshUser = str(testData['User'])
        sshPass = str(testData['Password'])
        baseKey = str(testData['serverKey'])
        key = paramiko.RSAKey(data=base64.b64decode(baseKey))
        client = paramiko.SSHClient()
        client.get_host_keys().add(sshIP, 'ssh-rsa', key)
        client.connect(sshIP, username=sshUser, password=sshPass)
        stdin, stdout, stderr = client.exec_command('ls')
        for line in stdout:
                print('... ' + line.strip('\n'))

def sshDisconnect():
        client.close()
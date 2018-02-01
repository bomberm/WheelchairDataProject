#! /usr/bin/env python
#
# Support module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Feb 01, 2018 01:55:14 AM


import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

def initializeConnection():
    from readTestFile import readFile
    contents = readFile("Chiron.test")
    print contents
    sshIP = str(testFileContents['IP'])
    sshPort = int(testFileContents['port'])
    sshUser = str(testFileContents['User'])
    sshPass = str(testFileContents['Password'])
    baseKey = str(testFileContents['serverKey'])
    key = paramiko.RSAKey(data=base64.b64decode(baseKey))
    client = paramiko.SSHClient()
    client.get_host_keys().add(sshIP, 'ssh-rsa', key)
    client.connect(sshIP, username=sshUser, password=sshPass)
    stdin, stdout, stderr = client.exec_command('echo hello?')
    if("hello?" in stdout):
        w.connectionStatus.configure(text='''Connected to Wheelchair''')
        sys.stdout.flush()
        return 1
    else:
        w.connectionStatus.configure(text='''Connection Failed''')
        sys.stdout.flush()
        return 0


def record():
    print('interface_support.record')
    sys.stdout.flush()
    if(initializeConnection()):
        if(w.recordingStatus):
            w.recordingStatus = 0
            w.but38.configure(text='''Record Bag''')
        else:
            w.recordingStatus = 1
            w.but38.configure(text='''Stop''')



def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import interface
    interface.vp_start_gui()

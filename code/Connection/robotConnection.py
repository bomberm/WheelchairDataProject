#!/usr/bin/env python

import readTestFile
import re
import ftplib
import socket

def connectToIP():
        with open(readTestFile.testFile) as f:
                for line in f:
                        if re.match("(.*)IP(.*)", line):
                                print("" + re.sub('IP: ','',line))
                                FtpIP = re.sub('IP: ','',line).strip("' \n")
                                print("IP = " + repr(FtpIP))
        ftp = ftplib.FTP()
        print(FtpIP)
        try:
                ftp.connect(FtpIP)
                print("Connection Successful! \n")
        except socket.error:
                print("Unable to connect to IP \n")

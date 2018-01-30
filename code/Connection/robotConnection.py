#!/usr/bin/env python

import readTestFile
import re
import socket

#function to connect to the IP given in the test file on the port given
def connectToIP():
	testData = readTestFile.readFile("TestFileTemplate.test")
	FtpIP = str(testData['IP'])
	FtpPort = int(testData['port'])

	print FtpIP
	print FtpPort

	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	client_socket.connect((FtpIP, FtpPort))

def disconnectFromIP():
	client_socket.close()

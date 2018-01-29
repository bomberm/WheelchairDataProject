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

	#Connection run until q is inputted, then connection stops
	while 1:
			data = client_socket.recv(512)
			if ( data == 'q' or data == 'Q'):
					client_socket.close()
					break;
			else:
					print "Received:" , data
					data = raw_input("Type q and hit enter to quit: " )
					if (data <> 'Q' and data <> 'q'):
							client_socket.send(data)
					else:
							client_socket.send(data)
							client_socket.close()

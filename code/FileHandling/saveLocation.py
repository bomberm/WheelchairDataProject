from createFilesystem import secureName

def startSave(theID, testFile):
	if 'IDs' in testFile:
		fileLocation = './'+testFile['Name']+'/'+str(theID)+'/'
	else:
		if testFile['Secure'] == 1:
			fileLocation = './'+testFile['Name']+'/'+secureName(theID, testFile)
		else:
			fileLocation = './'+testFile['Name']+'/'+theID

	print fileLocation

import os
from createFilesystem import secureName

def startSave(theID, testFile):
	if 'IDs' in testFile:
		fileLocation = './'+testFile['Name']+'/'+str(theID)+'/'
	else:
		if int(testFile['Secure']) == 1:
			fileLocation = './'+testFile['Name']+'/'+secureName(theID, testFile)
		else:
			fileLocation = './'+testFile['Name']+'/'+theID

	if not os.path.exists(fileLocation):
		print "File not found!"
		return False
	else:
		return True

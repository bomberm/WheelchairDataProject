import os, errno, shutil
import hashlib

def secureName(name, testFile):
	salt = testFile['Salt']
	return hashlib.sha256(salt.encode()+name.rstrip().encode()).hexdigest()

def createIDFiles(numIDs, dirName):
	for i in range(0, numIDs):
		if not os.path.exists(str(i)):
			os.makedirs(dirName+'/'+str(i)+'/')
	return	

def createFilesystem(testFile):
	#get directory name
	if not type(testFile) is dict:
		return False 

	dirName = testFile['Name']
	dirName = dirName.strip()

	#Create 'root' of test storage
	if not os.path.exists(dirName):
		os.makedirs(dirName)
	else:
		#handle editing current dir
		print 'Filesystem exists' #remove print once real functionality is added

	#Begin populating storage directory
	shutil.copy(testFile['FileName'], './'+dirName+'/')	
	

	#Test Participant Data - This will need to be updated to include logic for IDs
	if not 'Participant Data' in testFile:
		try:
			numIDs = int(testFile['IDs'])
			createIDFiles(numIDs, dirName)
			return True
		except:
			raise
			return False
	else:
		shutil.copy(testFile['Participant Data'], './'+dirName+'/')	
		participantFile = open(testFile['Participant Data'], 'r')	
	
	#Set up for security
	if int(testFile['Secure']) == 1:
		secure = True
	
	#Create subDirs for each participant
	for name in participantFile:
		if secure:
			workName = secureName(name, testFile).decode()
		else:
			workName = name
		if not os.path.exists(workName):
			os.makedirs(dirName+'/'+workName+'/')

	return True	

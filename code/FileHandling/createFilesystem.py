import os, errno, shutil
import hashlib
import json
from pathlib2 import Path
from sys import argv

def secureName(name, testFile):
	salt = testFile['salt']
	return hashlib.sha256(salt.encode()+name.rstrip().encode()).hexdigest()[:6]

def createIDFiles(numIDs, dirName):
	for i in range(0, numIDs):
		if not os.path.exists(str(i)):
			os.makedirs(dirName+'/'+str(i)+'/')
	return	


#get directory name
if not len(argv) == 2:
	raise IOError('Usage: '+argv[0]+' <test.json file>')

checkIfExists = Path(argv[1])                                   
if checkIfExists.is_file:
	testFile = checkIfExists.open()
else:
	raise IOError('Usage: '+argv[1]+'must be a .json file')

data = json.load(testFile)
dirName = data['name']

if not os.path.exists(dirName):
	os.makedirs(dirName)

#Begin populating storage directory
shutil.copy(argv[1], './'+dirName+'/')	
	

#Test Participant Data - This will need to be updated to include logic for IDs
if not 'names' in data.keys():
	try:
		numIDs = int(data['count_ids'])
		createIDFiles(numIDs, dirName)
		exit(0)
	except:
		raise
		exit(-1)
else:
	participantFile = data['names']
	

#Create subDirs for each participant
for name in participantFile:
	workName = secureName(name, data).decode()
	if not os.path.exists(workName):
		os.makedirs(dirName+'/'+workName+'/')


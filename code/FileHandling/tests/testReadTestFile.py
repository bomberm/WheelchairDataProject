import sys
sys.path.append("../")
import readTestFile as handle

theFile = handle.readFile("../../Templates/TestFileTemplate.test")

for key, value in theFile.iteritems():
	print (key, value)

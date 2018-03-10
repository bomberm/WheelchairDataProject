import subprocess

topics = open('topics.list', 'w')
output = subprocess.Popen(['rostopic', 'list'], stdout=topics)
#sleep(100)
topics.close()

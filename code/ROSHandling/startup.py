import subprocess
import signal

output = subprocess.Popen('roscore', stdin=subprocess.PIPE) 
store_pid = open("core.pid", 'w')
store_pid.write(str(output.pid))
store_pid.close()

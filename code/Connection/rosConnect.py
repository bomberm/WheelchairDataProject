#!/usr/bin/env python

import rospy
import os
import sys:q
import roslaunch
import subprocess
import rosbag
import signal
from std_msgs.msg import Int32, String

path1 = "../wheelchair_description/launch/wheelchair_bringup.launch"
path2 = "../wheelchair_description/launch/wheelchair_merger.launch"
path3 = "../wheelchair_navigation/launch/move_base_local.launch"

def rosStartup():
	roscore = subprocess.Popen('roscore')

def rosScriptsStart():
	rospy.init_node('launchFiles', anonymous=True)
	#rospy.on_shutdown(self.shutdown)

	uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
	roslaunch.configure_logging(uuid)
	launch1 = roslaunch.parent.ROSLaunchParent(uuid, [path1])
	launch2 = roslaunch.parent.ROSLaunchParent(uuid, [path2])
	launch3 = roslaunch.parent.ROSLaunchParent(uuid, [path3])

	launch1.start()
	launch2.start()
	launch3.start()

def rosScriptsEnd():
	launch1.shutdown()
	launch2.shutdown()
	launch3.shutdown()

def recordBag(location):
	rosbag = subprocess.Popen(['rosbag', 'record', 'tf', 'scan_multi', 'pose_stamped', '-o', location], preexec_fn=os.setsid)
	return rosbag

def writePidFile():
    pid = str(os.getpid())
    f = open('rosbag.pid', 'w')
    f.write(pid)
    f.close()	
	
def stopRecordBag(rosbag):
	os.killpg(rosbag.pid, signal.SIGINT)

#rosStartup()
#bag = recordBag('./test/')
#x = raw_input()
#stopRecordBag(bag)

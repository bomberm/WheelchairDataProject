#!/usr/bin/env python

import rospy
import os
import sys
import roslaunch
import subprocess
import rosbag
import signal
import rosConnect
from std_msgs.msg import Int32, String

rosbag = int(open(rosbag.pid).read())

def stopRecordBag(rosbag):
        os.killpg(rosbag.pid, signal.SIGINT)

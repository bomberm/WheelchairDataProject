#!/usr/bin/env bash

if [ $# -lt 2 ]
then
	echo "Usage: $0 <recording location> <topics to record>"
	exit -1
fi


source /opt/ros/kinetic/setup.bash
roscore &
launchScripts.sh
/opt/ros/kinetic/bin/rosbag record -o $@ &
pgrep -u $USER roscore > core.pid
sleep 5
pgrep -u $USER record > bag.pid

#!/usr/bin/env bash

if [ $# -lt 2 ]
then
	echo "Usage: $0 <recording location> <topics to record>"
	exit -1
fi

echo "$$" > bag.pid

source /opt/ros/kinetic/setup.bash
roscore &
echo `/opt/ros/kinetic/bin/rosbag record -o $@`

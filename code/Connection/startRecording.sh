#!/usr/bin/env bash

if [ $# -lt 2 ]
then
	echo "Usage: $0 <recording location> <topics to record>"
	exit -1
fi

echo "$$" > bag.pid

where=`which rosbag`
#source /opt/ros/kinetic/setup.bash
echo `$where record -o $@`

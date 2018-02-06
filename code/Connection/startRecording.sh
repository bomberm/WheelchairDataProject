#!/usr/bin/env bash

if [ $# -lt 2 ]
then
	echo "Usage: $0 <recording location> <topics to record>"
	exit -1
fi

source ～/.bashrc
echo `rosbag record -o $@`

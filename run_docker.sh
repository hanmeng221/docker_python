#!/bin/bash

docker_image_name="docker_python"

filepath=$(dirname $(readlink -f $0))

help_flag=0

wrong_flag=0

while [ -n "$1" ]
do
    case "$1" in
	-h)
		help_flag=1
		;;
	-f)
		if [ -d $2 ]; then
			filepath=$2
		else
			echo "the filepath is not available"	
			wrong_flag=1
		fi
		shift
		;;
	-i)
		docker_image_name=$2
		shift
		;;
	*)
		wrong_flag=1
		;;
	esac
	shift
done

if [ 1 -eq $wrong_flag ]; then
	echo "Parameter input error"
else
	if [ 1 -eq $help_flag ]; then
		sudo docker run $docker_image_name python execution_exe.py -h
	else
		sudo docker run -v $filepath:/usr/goal $docker_image_name python execution_exe.py /usr/goal
	fi
fi

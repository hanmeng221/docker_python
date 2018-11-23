# docker_python
use docker to package a python file and run

STtech_test

This is a interview test of Sensetime. It will:

    read all of the executable files from the gedit directory
    execute these files according to alphabet order
    if the executable file has the output, then print them to the terminal
    we provide two method to achieve it: run python script or run shell script

Usage

build a image
    open the terminal
    run :
    docker build -t docker_python
    
run the image
    run :
    docker run -v [your target directory path]:/usr/goal  docker_python

       

Exit Code:

    0: Success
    1: Target directory is empty
    2: Target directory is not existed
    3: Missing directory parameters

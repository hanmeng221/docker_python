# docker_python
use docker to package a python file and run


This is a interview test of Sensetime. It will:

    read all of the executable files from the gedit directory
    execute these files according to alphabet order
    if the executable file has the output, then print them to the terminal
    we provide two method to achieve it: run python script or run shell script

Usage

1.Install the docker(more detail show in Note)

2.Open the terminal

3.Build the image

    run:
       docker build -t docker_python .
       
4.Run the image
    run :
    
        docker run -v [your target directory path]:/usr/goal  docker_python python execution_exe.py /usr/goal
    
    or:
    
        ./run_docker.sh
  
 5.Both of the two script will return the exit code. If you want to call our script, you can judge it success or not by this

 6. the shell have some optional parameters
 
    SYNOPSIS
        run_docker.sh [OPTION] ... 
        
    DESCRIPTION
    
        -h  display the help of this program
        
        -i  docker_image_name   use another docker_image file name insist of docker_python
        
        -f target_directory_path   Set the target_directory_path that you want to  test
Note

    1. This code can only run on Linux.
    
    2. You can use the "targetDir" to test like:
    
        docker run -v ./targetDir:/usr/goal docker_python python execution_exe.py /usr/goal
        
        or
        
        ./run_docker.sh -f ./targetDir
    
    3.Install docker in Ubuntu
        3.1 Make sure the version of your system is higher than 3.10
        3.2 Open the terminal
        3.3 Run:
                
                wget -qO- https://get.docker.com/ | sh
        3.4 Start the docker service
               run: 
                sudo service docker start
    4. When you build a image successfully, you can use " docker images;" to show more details about this image.
    
    5. If you want to run docker when you are not the root, you can use " sudo usermod -aG docker runoob" and then re-entry.
    
Exit Code:

    0: Success
    1: Target directory is empty
    2: Target directory is not existed
    3: Missing directory parameters

import os
import subprocess
import sys

'''
Used to excute the file which is judged as an executable file in the target path.

@param {string} path - the full target file path include the filename.
'''
def execu(path):
    result = os.system(path)
    return result
    #print(result)

'''
Used to get all of the files in the target directory recursively, and order them, 
then send each of them to judge whether they are executable file.

@param {string} path - the target file path not include the filename.
'''
def readFile(path):
    if not os.path.isdir(path):
        print("Error: It's not a directory or not exist.")
        return 2
    elif not os.listdir(path):
        print("Warning: Empty directory.")
        return 1
    else:
        success = 0
        fail = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                result = judgeFilename(os.path.join(dirpath, filename))
                if result == 0:
                    success = success + 1;
                else:
                    fail = fail + 1;
        print("Success.\r"+str(success)+" succeeded, "+str(fail)+" failed.")
        return 0

'''
Used to judge the executable file. Used the method of pipe, redefine the output stream, put the result
from the terminal into the buffer memory. Then analysis the result, if the string has 'x', then it can be
executed.

@param {string} path - the full target file path include the filename.
'''
def judgeFilename(path):
    if(os.access(path, os.X_OK)):
        print("Now executing the file: " + path)
        result = execu(path)
        print('\r')
        return result


'''
Main function, input the target directory path.
'''
if __name__ == "__main__":
    try:
        path = sys.argv[1]
        if (path == "-h" or path == "--help"):
            print(
                "usage: ./execution_exe.sh [the target directory path]\n[your target directory path]: it's the absolute path or relative path in the file system.\n-h: print this help message and exit(also - -help)\nExit:\n0: Success\n1: Target directory is empty\n2: Target directory is not existed\n3: Missing directory parameters")
        else:
            # path = "./targetDir"
            result = readFile(path)
            exit(result)
    except:
        print("Error: Missing directory parameters.You can input:\n    'python execution_exe.py -h'\nto get help.")
        exit(3)








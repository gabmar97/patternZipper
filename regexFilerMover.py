import sys, getopt
import os
import re
import shutil   

class regexFileMover:
    # Class to run processes through a given directory
    def __init__(self):
         self.__file_path = sys.argv[1]
         # self.__file_dest = os.path.dirname(os.path.dirname(__file_path))
         
         self.__ParseDirectory()
    
    def __ParseDirectory(self):
        regexp1 = re.compile('[-]')
        regexp2 = re.compile('(png)+$')
        for root, dirs, files in os.walk(self.__file_path, followlinks=False):
            for f in files:
                if regexp1.search(f) and regexp2.search(f):
                    print("Moving " + f + " one directory up")
                    dir = os.path.join(root, f)
                    dest = os.path.dirname(os.path.dirname(root))
                    shutil.move(dir, dest)
    
if __name__ == "__main__":
    parser = regexFileMover()
    # print(sys.argv[1])

    sys.exit(0)
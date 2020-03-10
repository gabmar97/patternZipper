# Copyright 2020 Gabriel Martinez
import sys
import re
import os
import shutil
import zipfile

class patternZipper:
    # Class to run processes through a given directory
    def __init__(self):
         self.__root_path = sys.argv[1]
         self.__zip_dest = sys.argv[2]
         self.__zip_name = sys.argv[3]
         self.__zipFiles()
         self.__deleteDirectoryContents(self.__root_path)
         
    
    # Given regexs, a file will be moved one directory up if file name matches
    def __zipFiles(self):
        # Constraints for files to be moved and archived
        regexp1 = re.compile('[-]')
        regexp2 = re.compile(r'png')
        
        # Zips files that match regexps to temp folder
        os.chdir(os.path.dirname(self.__zip_dest))
        zf = zipfile.ZipFile(self.__zip_name, "w")
        for root, dirs, files in os.walk(self.__root_path, followlinks=False):
            for f in files:
                zf.write(root)
                if regexp1.search(f) and regexp2.search(f):
                    # dir = os.path.join(root, f)
                    print("zipping " + f)
                    zf.write(os.path.join(root, f))
                    
    # Deletes all subdirs and files from given dir
    def __deleteDirectoryContents(self, dir):
        # Emptying subdirectories
        for root, dirs, files in os.walk(dir, followlinks=False):
            for f in files:
                print("Deleting file: " + f)
                os.remove(os.path.join(root, f))
        # Deleting empty subdirectories
        for root, dirs, files in os.walk(dir, followlinks=False):
            for d in dirs:
                print("Deleting folder: " + d)
                os.rmdir(os.path.join(root, d))
                
                
if __name__ == "__main__":
    parser = patternZipper()
    sys.exit(0)

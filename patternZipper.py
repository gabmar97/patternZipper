import os
import re
import sys
import zipfile
from tkinter import filedialog, messagebox
from tkinter import *

# Class to zip files to a given directory that match a pattern
class regexFileMover:
    def __init__(self):
        self.__root_path = ""
        self.__dest_path = ""
        self.__zip_name = ""
        self.__to_delete = False
        self.__gui()
        sys.exit(0)

    # Mutator functions
    def setRoot(self, event):
        self.__root_path = filedialog.askdirectory()
        print(self.__root_path)
    def setDest(self, event):
        self.__dest_path = filedialog.askdirectory()
        print(self.__dest_path)
    def setZipName(self, event):
        print(self.__zip_name)
    def setDelete(self, event):
        if(not self.__to_delete):
            self.__to_delete = True
        else:
            self.__to_delete = False
        print(self.__to_delete)
    # Function to run zipping after variables are set
    def zipRunner(self, event):
        # Making sure input is no longer empty
        root_check = self.__root_path != ""
        dest_check = self.__dest_path != ""
        name_check = self.__zip_name != ""

        checks = root_check and dest_check and name_check

        # Zips files if input is non-empty
        if(checks):
            self.__zipFiles()
            self.__deleteDirectoryContents()
            messagebox.showinfo("Pattern Zipper", "Files Zipped!")

    # Creates GUI to recieve Input and run code
    def __gui(self):
        # initializing tk window
        window = Tk()
        window.title('Pattern Zipper')
        window.geometry('400x500')


        # initializing tk objects
        button_root = Button(window, text = "Root Directory")
        button_dest = Button(window, text = "Destination Directory")
        button_zip = Button(window, text = "Zip Files")
        label_zip = Label(window, text = "Archive Name: ")
        entry_zip_name = Entry(window)
        delete_box = Checkbutton(window, text = "Delete Root Contents:")

        # placing tk objects on window
        button_root.place(anchor = W, relx = .1, rely = .15)
        button_dest.place(anchor = E, relx = .9, rely = .15)
        button_zip.place(anchor = CENTER, relx = .5, rely = .8)
        label_zip.place(anchor = CENTER, relx = .5, rely = .4)
        entry_zip_name.place(anchor = CENTER, relx = .5, rely = .45)
        delete_box.place(anchor = CENTER, relx = .5, rely = .6)


        # setting actions to tk objects
        button_root.bind("<Button-1>", self.setRoot)
        button_dest.bind("<Button-1>", self.setDest)
        button_zip.bind("<Button-1>", self.zipRunner)
        delete_box.bind("<Button-1>", self.setDelete)
        
        # run window
        window.mainloop()

    # Given regexs, a file will be moved one directory up if file name matches
    def __zipFiles(self):
        # Constraints for files to be moved and archived
        regexp = re.compile('.*-+.*(.png)$')

        # Zips files that match regexps to temp folder
        os.chdir(os.path.dirname(self.__dest_path))
        zf = zipfile.ZipFile(self.__zip_name, "w")
        for root, dirs, files in os.walk(self.__root_path, followlinks=False):
            for f in files:
                if regexp.search(f):
                    print("zipping " + f)
                    zf.write(os.path.join(root, f))
                    
    # Deletes all subdirs and files from given dir
    def __deleteDirectoryContents(self):
        if(self.__to_delete):
            # Emptying subdirectories
            for root, dirs, files in os.walk(self.__root_path, 
                followlinks=False):
                for f in files:
                    print("Deleting file: " + f)
                    os.remove(os.path.join(root, f))

            # Deleting empty subdirectories
            for root, dirs, files in os.walk(self.__root_path, 
                followlinks=False):
                for d in dirs:
                    print("Deleting folder: " + d)
                    os.rmdir(os.path.join(root, d))
        else:
            print("Files not deleted")
if __name__ == "__main__":
    zipper = regexFileMover()
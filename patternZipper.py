import os
import re
import sys
import zipfile
import shutil
from tkinter import filedialog, messagebox
from tkinter import *


# Class to zip files to a given directory that match a pattern
class RegexFileMover:
    def __init__(self):
        # initializing tk window
        self.__window = Tk()
        self.__window.title("Pattern Zipper")
        self.__window.iconbitmap(r'Tkinter_icon.ico')
        self.__root_path = ""
        self.__dest_path = ""
        self.__zip_name = ""
        self.__zip_var = StringVar()
        self.__to_delete = False
        self.__gui()
        sys.exit(0)

    # Mutator functions
    def __set_root(self, event):
        self.__root_path = filedialog.askdirectory()
        self.__root_path = self.__root_path + "/"
        label_root_dir = Label(
            self.__window, 
            text=self.__root_path, 
            bg='gray28', 
            fg = 'gray64')
        label_root_dir.place(anchor=N, relx=.5, rely=.155)

    def __set_dest(self, event):
        self.__dest_path = filedialog.askdirectory()
        self.__dest_path = self.__dest_path + "/"
        label_dest_dir = Label(
            self.__window, 
            text=self.__dest_path,
            bg='gray28', 
            fg = 'gray64')
        label_dest_dir.place(anchor=N, relx=.5, rely=.325)

    def __set_zip_name(self, event):
        self.__zip_name = str(self.__zip_var.get())

    def __set_delete(self, event):
        if (not self.__to_delete):
            self.__to_delete = True
        else:
            self.__to_delete = False

    # Function to run zipping after variables are set
    def __run(self, event):
        # Making sure input is no longer empty
        
        self.__zip_name = self.__zip_var.get()

        # Zips files if input is non-empty
        self.__zipFiles()
        self.__deleteDirectoryContents()

        messagebox.showinfo("Pattern Zipper", "Files Zipped!")
        
    # Creates GUI to recieve Input and run code
    def __gui(self):
        # setting window parameters
        self.__window.title('Pattern Zipper')
        self.__window.geometry('650x450')
        self.__window.configure(bg='gray28')

        # initializing tk objects
        button_root = Button(
            self.__window, text="Root Directory", 
            bg='gray28', fg = 'gray64', 
            activebackground = 'gray28',
            activeforeground ='gray64')
        button_dest = Button(
            self.__window, 
            text="Destination Directory", 
            bg='gray28', 
            fg = 'gray64', 
            activebackground ='gray28',
            activeforeground ='gray64')
        button_zip = Button(
            self.__window, 
            text="Zip Files", 
            bg='gray28',
            fg = 'gray64',
            activebackground ='gray28',
            activeforeground ='gray64')
        label_zip = Label(
            self.__window, 
            text="Archive Name: ", 
            bg='gray28', 
            fg = 'gray64')
        entry_zip_name = Entry(
            self.__window, 
            textvariable=self.__zip_var, 
            bg='gray64')
        delete_box = Checkbutton(
            self.__window, 
            text="Delete Root Contents:", 
            bg='gray28', 
            fg = 'gray64')

        # placing tk objects on window
        button_root.place(anchor=S, relx=.5, rely=.15)
        button_dest.place(anchor=S, relx=.5, rely=.32)
        button_zip.place(anchor=CENTER, relx=.5, rely=.8)
        label_zip.place(anchor=S, relx=.5, rely=.45)
        entry_zip_name.place(anchor=N, relx=.5, rely=.45)
        delete_box.place(anchor=CENTER, relx=.5, rely=.65)

        # setting actions to tk objects
        button_root.bind("<Button-1>", self.__set_root)
        button_dest.bind("<Button-1>", self.__set_dest)
        delete_box.bind("<Button-1>", self.__set_delete)
        button_zip.bind("<Button-1>", self.__set_zip_name)
        button_zip.bind("<Button-1>", self.__run)

        # run window
        self.__window.mainloop()

    # Given regexs, a file will be moved one directory up if file name matches
    def __zipFiles(self):
        print(self.__root_path)
        print(self.__dest_path)
        print(self.__zip_name)
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
        try:
            if (self.__to_delete):
                # Deleting subdirectories
                shutil.rmtree(self.__root_path)
            else:
                print("Files not deleted")
        except:
            print ("PermissionError")

if __name__ == "__main__":
    zipper = RegexFileMover()

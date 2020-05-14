# RegEx-File-Mover
A python program that will automatically move contents within a directorie's sub-directories if the content's titles match a pattern using regex
---

* **USAGE:** 
  * Code currently only tested with Ubuntu bash
  * When given a directory path, a destination path, and an archive name (including extension) through command line when calling the program, the program zips all the matched file names within every directory and sub-directory in directory and zips them to a file in the destination path. After zipping matched files to the destination path the directory path's contents are deleted.
  * For Example: python3 patternZipper.py directoryPath destinationPath archiveName
  
* **NOTES:** 
  * Currently matches a hard coded pattern

  * Matches files that contain a '-' and end in jpg

  * Zips files whose names match the hardcoded pattern in a zip archive. Once the program has ran through all sub-directories it deletes everything within the given directroy path. 
Instructions

* **WARNING:** 
  * Save a backup of all the data before zipping. This program is meant to clean up temporary folders and only keep what is required. 


# RegEx-File-Mover
A python program that will automatically move contents within a directorie's sub-directories if the content's titles match a pattern using regex
---

* Currently matches a hard coded pattern

* Matches files that contain a '-' and end in jpg

* Zips files whose names match the hardcoded pattern in a zip archive. Once the program has ran through all sub-directories it deletes everything within the given directroy path. 
Instructions
---
* Code currently only tested with Ubuntu bash
Use:  When given a directory path, a destination path, and an archive name (including extension), the program zips all the matched file names within every directory and sub-directory and zips them to a file in the destination path. 


============================================================
  Empty File and Folder Cleaner
============================================================
Author: Andrea Agosti
Date: 2025-05-07

Description:
This script recursively scans a selected directory and:
  - Deletes all files that are 0 bytes in size.
  - Deletes all empty folders after file cleanup.

It uses a graphical user interface (GUI) to prompt the user
to select the root folder, making it user-friendly and safe
for non-technical users.

Requirements:
  - Python 3.x
  - tkinter (standard in most Python installations)

Usage:
  1. Run the script.
  2. A dialog will appear asking you to select a folder.
  3. The script will delete empty files and folders inside.
  4. A summary will be shown at the end.

Note:
  - Only files with 0 bytes will be deleted.
  - Only folders that are completely empty will be deleted.
  - The script prints and logs each deletion action.

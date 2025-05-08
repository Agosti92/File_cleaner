"""
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

============================================================
"""

import os
import tkinter as tk
from tkinter import filedialog, messagebox

def delete_empty_files_and_folders(start_path):
    deleted_files = 0
    deleted_dirs = 0

    # First pass: delete 0-byte files
    for root, dirs, files in os.walk(start_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                if os.path.getsize(file_path) == 0:
                    os.remove(file_path)
                    print(f"Deleted empty file: {file_path}")
                    deleted_files += 1
            except Exception as e:
                print(f"Error deleting file {file_path}: {e}")

    # Second pass: delete empty folders (bottom-up)
    for root, dirs, files in os.walk(start_path, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                if not os.listdir(dir_path):
                    os.rmdir(dir_path)
                    print(f"Deleted empty folder: {dir_path}")
                    deleted_dirs += 1
            except Exception as e:
                print(f"Error deleting folder {dir_path}: {e}")
    
    return deleted_files, deleted_dirs

def main():
    # GUI setup
    root = tk.Tk()
    root.withdraw()  # Hide main window

    print("=" * 60)
    print("  Empty File and Folder Cleaner")
    print("=" * 60)

    folder_path = filedialog.askdirectory(title="Select Folder to Clean")
    if not folder_path:
        print("No folder selected. Exiting.")
        return

    if not os.path.isdir(folder_path):
        messagebox.showerror("Invalid Path", "Selected folder is not valid.")
        return

    print(f"Cleaning folder: {folder_path}")
    deleted_files, deleted_dirs = delete_empty_files_and_folders(folder_path)

    print(f"\nSummary:")
    print(f"  Deleted files: {deleted_files}")
    print(f"  Deleted folders: {deleted_dirs}")
    messagebox.showinfo("Cleanup Complete", f"Deleted {deleted_files} files and {deleted_dirs} folders.")

if __name__ == "__main__":
    main()
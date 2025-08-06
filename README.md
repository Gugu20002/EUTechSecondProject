# EUTechSecondProject


 What It Does

1. You choose a **source** and **destination** folder via the GUI.
2. Enter a version number (e.g., `1.2.0`).
3. Choose whether to compress the backup as a ZIP file.
4. The program:
   - Adds a timestamp and version to the backup folder name.
   - Copies or zips the contents from source to destination.
   - Logs the backup activity in a `.log` file.
5. It remembers your preferences (folders, version, zip setting) for next time.


Before

Source Folder/
├── report.docx
├── image.png


After
Destination Folder/
├── backup_2025-08-07_14-50-22_v1-2-0/
│ ├── report.docx
│ ├── image.png

Running the App

file_backup_logger/
├── main.py # Entry point of the application
├── gui.py # tkinter GUI for selecting folders and options
├── backup.py # Core logic for copying or zipping files
├── logger.py # Handles log file creation and formatting
├── utils.py # Utility functions (timestamp formatting, etc.)
├── config.json # Stores saved user preferences
├── logs/
│ └── backup.log # Backup log file (auto-created)


Below are the screenshots of the process:
[photo1.jpg]










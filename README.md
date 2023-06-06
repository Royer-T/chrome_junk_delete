# Junk Delete Script

A script for deleting specific folders based on substring matches.

## Description

This script utilizes the `Junkdelete` class from the `junk_delete.deletion` module to delete folders that contain a specified substring. It performs deletion tasks in two directories: C:\Program Files (x86) and C:\Program Files.

The script is designed to be easily configurable by modifying the `constants.py` file.

## Prerequisites

- Python 3.x
- Required packages:
  - `junk_delete` module

## Usage

1. Clone the repository:
2. git clone https://github.com/Royer-T/chrome_junk_delete
3. Install the required packages:
   (WIP: add some yaml stuff?)
4. Configure the script by modifying the `constants.py` file:

```python
# constants.py

# Log directory
LOGDIRECTORY = "logs"

# Log file name
LOG_FILE = "junk_delete.log"

# Directory paths
INX86 = "C:/Program Files (x86)"
INPROGRAM = "C:/Program Files"
```
1. run the script: python junk_delete_script.py
2. Check the log file for details on the deleted folders: logs/junk_delete.log

Feel free to modify the content according to your specific requirements and add any additional information as needed.
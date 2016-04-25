import os
import time

# 1. The files and directions to be backed up are
# specified in a list
# Example on Windows:
# source = ["C:\\MyDocuments".'C:\\Code']
# Example on Mac OS X and Linux

source = ['F:\Work\Source\Python\Work']
# Notice we had to use double quotoes inside the string
# for names with spaces in it.

# 2. The backup must be stored in a
# main backup directory
# Example on Windows:
# target_dir = "E:\\Backup"
# Example on Mac OS and Linux
target_dir = 'F:\Work\Source\Python\backup'
# Remember to change this to which folder you will be using
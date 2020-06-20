#!/usr/bin/env python3

#Program to sort my photo files between Sony RAW and JPG files. Sorts into two separete directores so I can chooose what to import into Lightroom.

import os
import shutil

# ask for the name of the directory
SORT_DIR = os.getcwd()

DIRECTORY = input("What is the name of the Directory to be created? ")


DIRECTORY_RAW = (DIRECTORY + '_RAW')
DIRECTORY_JPG = (DIRECTORY + '_JPG')



# List the files in the source directory
list_ = os.listdir(SORT_DIR)

# rename the files based on the requested directory name
INCR = 0

for file_ in list_:
    name, ext = os.path.splitext(file_)
    INCR = INCR +1
    os.rename(file_, ((DIRECTORY) + "-" + str(INCR) + ext))


# create a directory for jpg
# create a directory for raw files

os.mkdir(DIRECTORY_RAW)
os.mkdir(DIRECTORY_JPG)

CURRENT_DIR = os.getcwd()

list1_ = os.listdir(SORT_DIR)

# Sort the photos into the directories, but do not sort the directory

for file1_ in list1_:
    if file1_.endswith('.ARW'):
        shutil.move(((CURRENT_DIR) + "/" + (file1_)), ((CURRENT_DIR) + "/" + (DIRECTORY_RAW)))
    if file1_.endswith('.JPG'):
        shutil.move(((CURRENT_DIR) + "/" + (file1_)), ((CURRENT_DIR) + "/" + (DIRECTORY_JPG)))
    else:
        continue
        
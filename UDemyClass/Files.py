# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 06:18:37 2016

@author: bkunneke
"""
import os, glob

# Open a file for writing and put some text in
fileObject = open('newfile.txt', 'w')
fileObject.write('A line of text\n')
fileObject.write('Another line of text\n')
fileObject.close()

# Open the file and read it
fileObject = open('newfile.txt', 'r')
fileContent = fileObject.read()
print(fileContent)  # fileContent is a text object containing the contents read
fileObject.close()

# Open the file and append text  NOTE the 'a' parameter
fileObject = open('newfile.txt', 'a')
fileObject.write('A newly appended line of text\n')
fileObject.close()

# Using the with operator to open a file
with open('newfile.txt', 'a') as fileObject:
    fileObject.write('Here is a new line added using with\n')


# Get current working directory from the os
oldPath = os.getcwd()
os.chdir('/Users/bkunneke/Downloads')  # NOTE The ~ Mac shortcut doesn't work

print('Original path ' + oldPath)
print('Current path ' + os.getcwd())

# Get a list of all png files from Downloads
imgList = glob.glob(os.getcwd() + '/*.png')
print(imgList)

# Now reset the path back
os.chdir(oldPath)
# Make a new directory, if the dir already exists an error is raised
if not os.path.isdir(os.getcwd()+'/temp'):
    os.makedirs('temp')

# List files in a directory
dirList = os.listdir(oldPath)
print(dirList)
for fileName in os.listdir(oldPath):
    print(fileName)

# Get the basename from a full file name
fullFileName = os.getcwd() + '/newfile.txt'  # File we created earlier
print(os.path.basename(fullFileName))
print(os.path.splitext(fullFileName))  # Basename with path, extension
print(os.path.splitext(os.path.basename(fullFileName)))  # Just base and ext
print(os.path.splitext(os.path.basename(fullFileName))[0])  # Just base
print(os.path.exists(fullFileName))  # Does the file exist?
print(os.path.exists(os.path.split(fullFileName)[0]))  #Does the path exist





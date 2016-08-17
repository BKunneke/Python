# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 07:07:44 2016

@author: bkunneke
"""

# Lists are sequences of objects
myList = [1, 2, 3, 4, 5]
# Add new items to the list
myList.append(6)
myList.append("Butter")

# Lists are indexed
print(myList[2])
print(myList[len(myList)-1])  # Last Item in the list
print(type(myList))

# Tuples are immutable
myTuple = (1, 2, 2, 2, 3, 4, 5)
# append is not an attribute of a tuple
print(myTuple.count(2))

# Sets and Dictionaries are collections
# Sets are colletions of unique items
mySet = {1, 2, 3, 4}

# Add duplicate item to previous list
myList.append(1)
# Convert to set and the duplicate is gone
mySet = set(myList)

# Dictionaries are collections of key/value pairs 
myDict = {"some_key":1, "another_key":"another brick in the wall", "3":"3"}
# Two ways to access the dictionary, both yield the same result
print(myDict.get('another_key'))
print(myDict['another_key'])

# Lists can be converted to sets and vice versa
myNewList = list(mySet)
myNewSet = set(myList)

# Range function can generate a sequence
print(range(1, 10, 2))  # Start at 1, stop at 10, count by 2
myEvenNewerList = list(range(1, 100, 3))
# Range of a list
print(myEvenNewerList[1:4])  # Prints items 2, 3, and 4 in the list
myEvenNewerList[0:3]  # First 3 items
myEvenNewerList[:3]   # Also the first 3 items
myEvenNewerList[10:]  # All items from the 10th element on
myEvenNewerList[-3:-1]  # Start at the 3rd from the last and stop at second from last

# Strings are basically lists of bytes
myString = "Bill Kunneke"
myString[1:9]  # Yields "ill Kunn"

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 06:07:36 2016

@author: bkunneke
"""

import pandas

"""
File related pandas stuff, reading and writing csv/excel/etc
"""

# Read a csv into a dataframe with an infered header and a default index col
dataFrame = pandas.read_csv('filename.csv')

# Read a csv into a dataframe with no header and a specified index col
dataFrame = pandas.read_csv('filename.csv', header=None, index_col=3)
# index_col is a zero based index in the input file to use as my index 

# Read a space separated file into a dataFrame NOTE single space separated
dataFrame = pandas.read_csv('filename.csv', sep=' ')
# And for multiple spaces of varying lengths, regular expression
dataFrame = pandas.read_csv('filename.csv', sep='\s+')

# Read a fixed width file, NOTE all other params are the same as read_csv
dataFrame = pandas.read_fwf('filename.fwf')

dataFrame.head()    # Shows the header and the first n rows as a quick view

# Write a dataframe to a csv file
dataFrame.to_csv('filename.csv')

# Write a dataframe to a csv file with no header and no index
dataFrame.to_csv('filename.csv', header=None, index=None)

# Write a dataframe to html
dataFrame.to_html('filename.html')


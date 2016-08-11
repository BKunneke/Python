# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 05:33:22 2016

@author: bkunneke
"""

import os, pandas
os.chdir('/Users/bkunneke/Code/python/UdemyClass')

# The first 3 rows are comments to skip.  
dataFrame = pandas.read_excel('Income-By-State-1984.xls', skiprows=3)

# The first column is an index column, need to skip it
dataFrame.to_csv("Income-By-State-1984.csv",index=0)


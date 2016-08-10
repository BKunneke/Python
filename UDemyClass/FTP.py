# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 09:20:42 2016

@author: bkunneke
"""

from ftplib import FTP
import os

def ftpDownloader(filename, host="ftp.pyclass.com", user="student@pyclass.com", pwd="student123"):
    ftp=FTP(host)
    ftp.login(user, pwd)
    os.chdir('/Users/bkunneke/Downloads')
    ftp.cwd('Data')
    with open(filename, 'wb') as file:
        ftp.retrbinary('RETR %s' % filename, file.write)
        
    #print(ftp.nlst())
    ftp.close()
    
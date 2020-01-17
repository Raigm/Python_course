# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 23:06:40 2019

@author: raigo
"""
import os 
def rename_files():
    #get the filenames
    file_list = os.listdir(r'C:/Users/raigo/Documents/Python_course/prank/prank')
    print (file_list)
    saved_path = os.getcwd()
    print ("the current path is "+ saved_path)
    os.chdir(r'C:/Users/raigo/Documents/Python_course/prank/prank')
    
    #change the filenames
    for file_name in file_list:
       os.rename(file_name, file_name.translate(None, "0123456789"))
 
rename_files()
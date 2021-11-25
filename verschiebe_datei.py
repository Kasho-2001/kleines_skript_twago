import os
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import shutil



#Variablendefinition
old_target_number = '123'
old_target_directory = ('.')
new_target_directory = ('/new_dir')
new_target_filename =  ('neindasistdieneuedatei.txt')


Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename(filetypes=[('all including old_target_number', '*'+old_target_number+'*')]) # show an "Open" dialog box and return the path to the selected file
print(filename)
shutil.copy(filename,new_target_directory+new_target_filename)

all_files = os.listdir(old_target_directory)
print(all_files)
for i in all_files:
    #print(i) 
    position = i.find(old_target_number)
    if position != -1:
        print(i)
import os
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import shutil
from tkinter import simpledialog


#Variablendefinition
ausgangsverzeichnis = ('/home/kasho/Documents/twago/kleines_skript/quelle')         #Quelle der Dateien
zielverzeichnis = ('neues_verzeichnis/')                                            #Ziel der Datei 
zieldateiname =  ('dieneuedatei.txt')                                               #Name der Zieldatei 

while True:
    
    #Eingabe
    ROOT = Tk()
    ROOT.withdraw()
    target_number = simpledialog.askstring(title="Nummerneingabe", prompt="Bitte hier die Auftragsnummer eingeben:")
    print("Auftragsnummer: ", target_number)


    #Dateienauswahl
    filename = askopenfilename(initialdir = ausgangsverzeichnis, filetypes=[('allle mit >target_number<', '*'+target_number+'*')])
    print(filename)

    #Kopieren
    shutil.copy(filename,zielverzeichnis+zieldateiname)
import os
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import shutil
from tkinter import simpledialog
from configparser import ConfigParser


#config.ini auslesen und Variablen übergeben
config_object = ConfigParser()
config_object.read("config.ini")

variablen = config_object["variablen"]

#Variablendefinition
ausgangsverzeichnis = variablen["ausgangsverzeichnis"]                              #Quelle der Dateien
zielverzeichnis = variablen["zielverzeichnis"]                                      #Ziel der Datei 
zieldateiname =  variablen["zieldateiname"]                                         #Name der Zieldatei 
print(ausgangsverzeichnis,'83')
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
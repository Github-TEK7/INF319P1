# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 22:42:22 2021

@author: jm_vi
"""
#PYTHON Y PROLOG CON ARCHIVO.PL
from pyswip import Prolog
prolog=Prolog()
prolog.consult("declaraciones.pl")
#RELACION DE PADRE
for elem in prolog.query("padre(X,Y)"):
    print(elem["X"], "es el padre de", elem["Y"])
print()
#RELACION DE HIJO
for elem in prolog.query("hijo(X,Y)"):
    print(elem["X"], "es el hijo de", elem["Y"])
print()
#RELACION DE HERMANO
for elem in prolog.query("hermano(X,Y)"):
    print(elem["X"], "es el hermano de", elem["Y"])
print()
#RELACION DE ABUELO
for elem in prolog.query("abuelo(X,Y)"):
    print(elem["X"], "es el abuelo de", elem["Y"])
print()
#RELACION DE FAMILIAR
for elem in prolog.query("familiar(X,Y)"):
    print(elem["X"], "es el familiar de", elem["Y"])

#consultas
print("Ingrese al PRIMER miembro que desea verificar si tienen una relacion de hermano")
Y=input();
print("Ingrese al SEGUNDO miembro que desea verificar si tienen una relacion de hermano")
Z=input()
valor=bool(list(prolog.query("hermano("+Y+","+Z+")")));
print(valor)
if(valor):
    print("Si, "+Y+" es hermano de "+Z)
else:
    print(Y+" NO es hermano de "+Z)
    
print("Ingrese al PRIMER miembro que desea verificar si tienen una relacion de abuelo")
Y=input();
print("Ingrese al SEGUNDO miembro que desea verificar si tienen una relacion de abulo")
Z=input()
valor=bool(list(prolog.query("abuelo("+Y+","+Z+")")));
print(valor)
if(valor):
    print("Si, "+Y+" es abuelo de "+Z)
else:
    print(Y+" NO es abuelo de "+Z)












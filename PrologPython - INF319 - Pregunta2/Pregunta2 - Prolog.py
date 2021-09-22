# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 09:45:33 2021

@author: jm_vi
"""

from pyswip import Prolog
prolog=Prolog()
prolog.assertz("padre(juan,maría)")
prolog.assertz("padre(pablo,juan)")
prolog.assertz("padre(pablo,marcela)")
prolog.assertz("padre(carlos,débora)")

#lista de padres (no lo utilizo porque se duplican valores al hacerlo correr mas de 2 veces)
#list(prolog.query("padre(X,Y)")) == [{'X': 'Y'}, {'X': 'Y'}]
#for elem in prolog.query("padre(X,Y)"):
#    print(elem["X"], "es el padre de", elem["Y"])


#CONSULTA DE RELACION DE PADRE
print("Ingrese al PRIMER miembro que desea verificar si tienen una relacion de padre")
Y=input();
print("Ingrese al SEGUNDO miembro que desea verificar si tienen una relacion de padre")
Z=input()
print(Y+" es padre de "+Z+"?")
valor=bool(list(prolog.query("padre("+Y+","+Z+")")))
if(valor):
    print("Si, "+Y+" es padre de "+Z)
else:
    print(Y+" NO es padre de "+Z)

#CONSULTA DE RELACION DE HERMANO
print("Ingrese al PRIMER miembro que desea verificar si tienen una hermandad")
Y=input();
print("Ingrese al SEGUNDO miembro que desea verificar si tienen una hermandad")
Z=input()
print(Y+" es hermano de "+Z+"?")
valor=bool(list(prolog.query("padre(X,"+Y+"), padre(X,"+Z+"), ("+Y+"\=="+Z+")" )))
if(valor):
    print("Si, "+Y+" es hermano de "+Z)
else:
    print(Y+" NO es hermano de "+Z)

#CONSULTA DE RELACION DE ABUELO
print("Ingrese al PRIMER miembro que desea verificar si tienen una relacion de abuelo")
Y=input();
print("Ingrese al SEGUNDO miembro que desea verificar si tienen una relacion de abuelo")
Z=input()
print(Y+" es abuelo de "+Z+"?")
valor=bool(list(prolog.query("padre("+Y+",X), padre(X,"+Z+")")))
if(valor):
    print("Si, "+Y+" es abuelo de "+Z)
else:
    print(Y+" NO es abuelo de "+Z)

#CONSULTA DE RELACION DE FAMILIAR
print("Ingrese al PRIMER miembro que desea verificar si tienen una relacion de parentezco")
Y=input();
print("Ingrese al SEGUNDO miembro que desea verificar si tienen una relacion de parentezco")
Z=input()
print(Y+" es familiar de "+Z+"?")
valor1=bool(list(prolog.query("padre("+Y+","+Z+")")))
valor2=bool(list(prolog.query("padre("+Y+",X), padre(X,"+Z+")")))
valor3=bool(list(prolog.query("padre(X,"+Y+"), padre(X,"+Z+"), ("+Y+"\=="+Z+")" )))
valor4=bool(list(prolog.query("padre("+Z+","+Y+")")))#relacion de hijo
valor5=bool(list(prolog.query("padre(X,"+Y+"), padre("+Z+",X)")))#relacion de nieto
if(valor1 or valor2 or valor3 or valor4 or valor5):
    print("Si, "+Y+" es familiar de "+Z)
else:
    print(Y+" NO es familiar de "+Z)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
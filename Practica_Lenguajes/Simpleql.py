import sys
import re
import time
import json
from reporte import reporte
registros = [ ]


def cargar(op):
    op.remove("cargar")
    #nombres_archivos = op[0].split(",")
    for x in op:
        efe = x
        print (x)
        if x.__contains__(","):
            
            efe = x.replace(",","")
        with open (efe) as file:
            data = json.load(file)
            registros.extend(data)
            print(registros)



def seleccionar (op):
     #print(len(registros))    
     op.remove("seleccionar")              #[0]                       [1]     [2]   [3]  [4] 
     #arregloAux = op[0].split(" ")     # nombre,edad,promedio,activo DONDE nombre  =  "Ruben"
     if op[0] == "*":
         for x in registros:
             print( "Nombre---->" +x["nombre"],"Edad----> "+str(x["edad"]),"Activo---->" +x["activo"],"Promedio---->"+str(x["promedio"]) )

    





def maximo(op):

   op.remove("maximo")

   if op[0] == "edad":
       items = [reg ["edad"] for reg in registros]
       print(max(items))
          
      
        
   elif op[0] == "promedio":
        item1 = [reg ["promedio"] for reg in registros]
        print(float(max(item1)))

    

def minimo(op):
    op.remove("minimo")

    if op[0] == "edad":
        items = [reg ["edad"] for reg in registros]
        print (min(items))

    elif op[0] == "promedio":
        items = [reg ["promedio"] for reg in registros]
        print (float(min(items)))

def suma(op):

    op.remove ("suma")

    if op[0] == "edad":
        items = [reg ["edad"]for reg in registros]
        print (sum(items))

    elif op[0]==("promedio"):
        items = [reg ["promedio"]for reg in registros]
        print (float(sum(items)))

def cuenta (op):
    print(len(registros))

  
def generar_reporte (nreg):
    try:

        nreg=int(nreg)
        if nreg <= len(registros) :

            reporte(registros,nreg)
        else:
            print("No hay pan")
        
    except:
        print("ERROR SE ESPERABA UN VALOR NUMERICO ")
    


def funciones():
    
    funcion = True 
    while funcion:
        
        op = input("Escribe una funcion ").split(" ")
        op[0]= op[0].lower()
        

        if op[0] == "cargar":
            cargar(op)      
            
        elif op[0] == "seleccionar":
            seleccionar (op)   
        
        elif op[0] == "maximo":
            maximo(op)
        
        elif op[0]=="minimo":
            minimo(op)   
        
        elif op[0]=="suma":
            suma(op)                              # Utilizo el .lower() ya sea Cargar, CARGAR o CaRgAr

        elif op [0]== "cuenta":
            cuenta(op)

        elif op[0]=="reportar":
            generar_reporte(op[1])
        elif op[0]== "salir":
            break

        else :
            print("Error de comando")
funciones()    
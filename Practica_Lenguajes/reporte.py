import json
import webbrowser
from os import linesep
import os


def reporte(registros,nreg):
   
   
    
    report = open("reporte.html","w") # para abrir el archivo
    report.write("<!DOCTYPE html>"
+"<html>"
    +"<head>"
        +"<title>REPORTE</title>"
         + "<meta charset=\"utf-8\">"
          +"<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
          +"<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css\"> "
          +"<style>"
    
    +"body {"
        +"background-color: Slategray;"
    +"}"
+"</style>"
    +"</head>"
    +"<body>"
        +"<div class=\"container\">"
  +"<h1>REPORTE  </h1>"
  
  +"<table class=\"table\">"
    +"<thead>"
      +"<tr>"
        +"<th>Nombre</th>"
        +"<th>Edad</th>"
        +"<th>Activo</th>"
        +"<th>Promedio </th>"
      +"</tr>"
    +"</thead>"
    +"<tbody>      "+linesep
            
            )
    cont_alternacion = 0
    for i in range (0, nreg):
    
        clasetr = ""
        if cont_alternacion == 0:
            clasetr = "<tr class=\"table-primary\">"
            cont_alternacion += 1
        elif cont_alternacion == 1:
            clasetr = "<tr class=\"table-success\">"
            cont_alternacion += 1
        elif cont_alternacion == 2:
            clasetr = "<tr class=\"table-danger\">"
            cont_alternacion +=1

        elif cont_alternacion == 3:
            clasetr = "<tr class=\"table-info\">"
            cont_alternacion = 0

        x = registros[i]


        report.write(clasetr  + "\n"
    + "<td>"+x["nombre"]+"</td>"   
    + "<td>"+str(x["edad"])+"</td>"   
    + "<td>"+x["activo"]+"</td>"   
    + "<td>"+str(x["promedio"])+"</td>"   
        
      +"</tr>"
    + linesep
    
        
    )

    report.write(
          "</tbody>"
  +"</table>"
+"</div>"


    +"</body>"
+"</html>"
    ) 
    report.close()
    os.system("reporte.html")

    


    




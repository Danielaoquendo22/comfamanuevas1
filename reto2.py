#ENTRADA

mesAño =int (input("digita mes del año"))

#CAMINOS
if mesAño == "Marzo" or mesAño == "Abril" or mesAño =="Mayo":
    print ("Primavera")
elif mesAño == "Junio" or mesAño == "Julio" or mesAño == "Agosto" :
    print ("Verano")
elif mesAño == "Septiembre" or mesAño == "Octubre" or mesAño== "Noviembre":
    print ("Otoño")
elif mesAño == "Diciembre" or mesAño == "Enero" or mesAño =="Febrero":
    print ("Invierno")
else:
    print ("Mes no valido")
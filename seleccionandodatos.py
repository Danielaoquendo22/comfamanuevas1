#ENTRADAS DEL PROBLEMA 

nivelAgua = int (input ("digita el nivel de agua"))

#EVALUANDO CAMINOS MULTIPLES (MAS DE 2)
if nivelAgua <= 100: 
    print("Bajo nivel de agua")
elif nivelAgua >100 and nivelAgua <400:
    print("operacion optima")
elif nivelAgua >= 400:
    print ("peligro.....")
else:
    print ("nivel de agua no valido")

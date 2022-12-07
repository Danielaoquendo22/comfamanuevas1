opcion=100

print("empanadas el machetico")
print("**************************\n")

print("1. Registrar empanadas")
print("2. Ver empanada")
print("0. SALIR")


empanadas=[]
while opcion != 0:
    opcion=int(input("digita una opcion: "))
    if opcion ==1:
        empanada=input("registre el nombre de la empanada a registrar: ")
        empanadas.append(empanada)
    elif opcion ==2:
        for empanada in empanadas:
            print(f"la empanada es:{empanada}")
            
    elif opcion ==0:
        break
    else:
        print("Apreciado usuario, debe seleccionar una opcion valida...")
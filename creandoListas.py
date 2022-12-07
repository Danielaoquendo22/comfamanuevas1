#una lista es una variable

from cgi import print_arguments


numeros= [1,2,3,4,5]
nombres= ["Juan","Sara","Carlos","Martha"]

'''print(numeros)
print(numeros[4])'''

#recorrer una lista 

#FOR CON UN RANGO   
'''for auxiliar in range(len(nombres)):
    print(nombres[auxiliar])'''

#FOR CON UNA LISTA
for nombre in nombres: 
    print(nombre)
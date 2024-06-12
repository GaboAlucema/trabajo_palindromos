''' 
Descripcion: Programa que recibe una cadena de texto y devuelve el numero minimo de cortes que se deben hacer para que cada subcadena sea un palindromo
'''
import time
inicio = time.time()

#Funcion que recibe una cadena de texto y devuelve el numero minimo de cortes que se deben hacer para que cada subcadena sea un palindromo
def palindromos (cadena):
    n = len(cadena)

    C = [[0 for _ in range(n)] for _ in range(n)]                  #Matriz de cortes
    P = [[False for _ in range(n)] for _ in range(n)]        #Matriz de palindromos

    for i in range(n):
        P[i][i] = True                                       

    for longitud in range(2, n+1):                          
        for i in range(n - longitud + 1):                       
            j = i + longitud - 1                                

            if longitud == 2:                           
                P[i][j] = (cadena[i] == cadena[j])       
            else:
                P[i][j] = (cadena[i] == cadena[j]) and P[i + 1][j - 1]    

    for i in range(n):
        if P[0][i]:      
            C[0][i] = 0
        else:
            C[0][i] = float('inf')     
            for j in range(i):
                if P[j + 1][i] and 1 + C[0][j] < C[0][i]:      
                    C[0][i] = 1 + C[0][j]
    return C[0][n-1]

#Funcion para leer archivo
def leerarchivo(nombre):
    ejemplos = []
    with open(nombre, "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            cadena = linea.strip()
            ejemplos.append(cadena)
    return ejemplos


#Ejecucion de la funcion
nombre_archivo = "12000palabras.txt"
ejemplos = leerarchivo(nombre_archivo)

for cadena in ejemplos:
    resultado = palindromos(cadena)
    print(f"Cadena: '{cadena}', Resultado: {resultado}")

final = time.time()
print("Tiempo de ejecucion: ", (final - inicio)*1000, "milisegundos")
    
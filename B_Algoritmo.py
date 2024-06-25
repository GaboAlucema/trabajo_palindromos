''' 
Descripcion: Programa que recibe una cadena de texto y devuelve el numero minimo de cortes que se deben hacer para que cada subcadena sea un palindromo
'''
import time
inicio = time.time()

def minCortePalindromo(s):
    n = len(s)
    # Crear una matriz para almacenar los resultados de los subproblemas
    minCorteDp = [float('inf')] * n
    # Crear una matriz para almacenar si una subcadena es palindromica o no
    esPalindromo = [[False] * n for _ in range(n)]

    for i in range(n):
        minCorteDp[i] = i
        esPalindromo[i][i] = True  
    for i in range(1, n):
        for j in range(i + 1):
            # Comprobar si la subcadena s[j:i+1] es palindromica
            if s[j] == s[i] and (i - j <= 1 or esPalindromo[j + 1][i - 1]):
                esPalindromo[j][i] = True
                # Actualizar el numero minimo de cortes necesarios
                if j == 0:
                    minCorteDp[i] = 0
                else:
                    minCorteDp[i] = min(minCorteDp[i], minCorteDp[j - 1] + 1)

    return minCorteDp[n - 1]

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
    resultado = minCortePalindromo(cadena)
    print(f"Cadena: '{cadena}', Resultado: {resultado}")

final = time.time()
print("Tiempo de ejecucion: ", (final - inicio)*1000, "milisegundos")

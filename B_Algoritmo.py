''' 
Descripcion: Programa que recibe una cadena de texto y devuelve el numero minimo de cortes que se deben hacer para que cada subcadena sea un palindromo
'''
import time
inicio = time.time()

def minCutPalindrome(s):
    n = len(s)
    # Crear una matriz para almacenar los resultados de los subproblemas
    minCutDp = [float('inf')] * n
    # Crear una matriz para almacenar si una subcadena es palindrómica o no
    isPalindrome = [[False] * n for _ in range(n)]

    for i in range(n):
        minCutDp[i] = i  # En el peor caso, se necesitan i cortes para una cadena de longitud i+1
        isPalindrome[i][i] = True  # Una sola letra siempre es palindrómica

    for i in range(1, n):
        for j in range(i + 1):
            # Comprobar si la subcadena s[j:i+1] es palindrómica
            if s[j] == s[i] and (i - j <= 1 or isPalindrome[j + 1][i - 1]):
                isPalindrome[j][i] = True
                # Actualizar el número mínimo de cortes necesarios
                if j == 0:
                    minCutDp[i] = 0
                else:
                    minCutDp[i] = min(minCutDp[i], minCutDp[j - 1] + 1)

    return minCutDp[n - 1]

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
    resultado = minCutPalindrome(cadena)
    print(f"Cadena: '{cadena}', Resultado: {resultado}")

final = time.time()
print("Tiempo de ejecucion: ", (final - inicio)*1000, "milisegundos")
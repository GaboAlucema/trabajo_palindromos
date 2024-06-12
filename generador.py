import random

def generar_palabra_aleatoria():
    longitud = random.randint(3, 15)  # Longitud aleatoria entre 3 y 15
    caracteres = ''.join(random.choices('abcdefg', k=longitud))
    return caracteres

def generar_n_palabras_aleatorias(n):
    palabras = [generar_palabra_aleatoria() for _ in range(n)]
    return palabras

def guardar_palabras_en_archivo(palabras, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for palabra in palabras:
            archivo.write(palabra + '\n')

# Ejemplo de uso
n = 12000  # Número de palabras a generar
palabras_aleatorias = generar_n_palabras_aleatorias(n)
guardar_palabras_en_archivo(palabras_aleatorias, '12000palabras.txt')

#!/usr/bin/env python3

import sys

# Palabras comunes del español para comparar
PALABRAS_CLAVE = {
    "hola", "el", "la", "de", "que", "en", "y", "a", "es", "un",
    "por", "con", "no", "una", "su", "para", "como", "más", "pero", "yo"
}

# Colores ANSI para resaltar en verde
VERDE = "\033[92m"
RESET = "\033[0m"

def descifrar_cesar(texto, desplazamiento):
    resultado = ''
    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            descifrado = chr((ord(caracter) - base - desplazamiento) % 26 + base)
            resultado += descifrado
        else:
            resultado += caracter
    return resultado

def puntuacion_probabilidad(texto):
    palabras = texto.lower().split()
    return sum(1 for palabra in palabras if palabra in PALABRAS_CLAVE)

def main():
    if len(sys.argv) != 2:
        print("Uso: ./cesar_crack.py \"TextoCifrado\"")
        sys.exit(1)

    texto_cifrado = sys.argv[1]
    mejores_resultados = []
    puntuacion_max = -1

    for d in range(26):
        descifrado = descifrar_cesar(texto_cifrado, d)
        puntuacion = puntuacion_probabilidad(descifrado)

        if puntuacion > puntuacion_max:
            puntuacion_max = puntuacion
            mejores_resultados = [(d, descifrado)]
        elif puntuacion == puntuacion_max:
            mejores_resultados.append((d, descifrado))

    print("Posibles descifrados:")
    for d in range(26):
        descifrado = descifrar_cesar(texto_cifrado, d)
        texto_mostrar = f"[{d:02d}] {descifrado}"
        if any(d == mejor_d for mejor_d, _ in mejores_resultados):
            print(VERDE + texto_mostrar + RESET)
        else:
            print(texto_mostrar)

if __name__ == "__main__":
    main()

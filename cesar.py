#!/usr/bin/env python3

import sys

def cifrado_cesar(texto, desplazamiento):
    resultado = ''
    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            cifrado = chr((ord(caracter) - base + desplazamiento) % 26 + base)
            resultado += cifrado
        else:
            resultado += caracter
    return resultado

def main():
    if len(sys.argv) != 3:
        print("Uso: ./cesar.py \"Texto a cifrar\" desplazamiento")
        sys.exit(1)
    
    texto = sys.argv[1]
    try:
        desplazamiento = int(sys.argv[2])
    except ValueError:
        print("El desplazamiento debe ser un número entero.")
        sys.exit(1)

    texto_cifrado = cifrado_cesar(texto, desplazamiento)
    print(texto_cifrado)

if __name__ == "__main__":
    main()

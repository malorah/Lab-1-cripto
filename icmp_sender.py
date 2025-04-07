#!/usr/bin/env python3

from scapy.all import IP, ICMP, send
import sys
import time

def enviar_icmp_por_caracter(destino, texto):
    for i, caracter in enumerate(texto):
        paquete = IP(dst=destino)/ICMP(type=8)/caracter
        print(f"[{i+1}/{len(texto)}] Enviando: '{caracter}' → {destino}")
        send(paquete, verbose=0)
        time.sleep(0.2)  # pausa entre paquetes

def main():
    if len(sys.argv) != 3:
        print("Uso: sudo ./icmp_sender.py <destino> <texto>")
        sys.exit(1)
    
    destino = sys.argv[1]
    texto = sys.argv[2]

    enviar_icmp_por_caracter(destino, texto)

if __name__ == "__main__":
    main()

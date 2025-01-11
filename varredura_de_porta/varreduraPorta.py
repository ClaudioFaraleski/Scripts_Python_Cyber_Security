#Autor: Claudio Faraleski
#Updated: 11/01/2025

import socket

def scan_ports(ip):
    active_ports = []
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389]  # Lista de portas comuns
    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            active_ports.append(port)
        sock.close()
    return active_ports

if __name__ == "__main__":
    while True:
        ip = input("Digite o IP para varredura (ou 'sair' para encerrar): EX:192.168.1.1\n")
        if ip.lower() == 'sair':
            break
        print(f"Varredura de portas ativas no IP: {ip}")
        print("Aguarde, este processo pode demorar um pouco...")
        active_ports = scan_ports(ip)
        if active_ports:
            print("Portas ativas:")
            for port in active_ports:
                print(f" - Porta {port}")
        else:
            print("Nenhuma porta ativa encontrada.")

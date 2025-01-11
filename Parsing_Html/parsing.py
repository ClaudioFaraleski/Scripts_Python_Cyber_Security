#Autor: Claudio Faraleski
#Updated: 11/01/2025
#Descrição: Programa que coleta informações de hosts, como endereços IP e subdomínios, a partir de um domínio fornecido pelo usuário.
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import socket
import json
import time

def get_ip_addresses(domain):
    try:
        ip_addresses = socket.gethostbyname_ex(domain)[2]
        return ip_addresses
    except Exception as e:
        print(f"Erro ao obter endereços IP: {e}")
        return []

def get_subdomains(domain):
    try:
        response = requests.get(f"http://{domain}")
        soup = BeautifulSoup(response.text, 'html.parser')
        subdomains = set()
        for a in soup.find_all('a', href=True):
            subdomain = urlparse(a['href']).netloc
            if subdomain and subdomain != domain and domain in subdomain:
                subdomains.add(subdomain)
        return list(subdomains)
    except Exception as e:
        print(f"Erro ao buscar subdomínios: {e}")
        return []

if __name__ == "__main__":
    print("Bem-vindo ao programa de coleta de informações de hosts.")
    print("______________________________________________________")
    print("EX de dominio: google.com - Não é necessario Digitar www")
    print("")
    domain = input("Digite o Dominio: ")
    print("Escaneando...")
    time.sleep(5)
    print("Pronto!")
    time.sleep(3)
    print("Aqui estão as informações coletadas:")
    time.sleep(3)
    print("")
    data = {}
    
    ip_addresses = get_ip_addresses(domain)
    if ip_addresses:
        print(f"Endereços IP para {domain}: {ip_addresses}")
        data[domain] = ip_addresses
    
    subdomains = get_subdomains(domain)
    if subdomains:
        print(f"Subdomínios encontrados: {subdomains}")
        for subdomain in subdomains:
            subdomain_ips = get_ip_addresses(subdomain)
            if subdomain_ips:
                print(f"Endereços IP para {subdomain}: {subdomain_ips}")
                data[subdomain] = subdomain_ips
    else:
        print("Subdominios Não encontrados.")
    
    with open('hosts_info.json', 'w') as file:
        json.dump(data, file, indent=4)

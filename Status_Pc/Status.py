# Autor: Claudio Faraleski
# Data: 11/01/2025

import os
import time
import getpass
import psutil

# Função para obter o tempo de atividade do sistema
def get_system_uptime():
    return time.time() - psutil.boot_time()

# Função para obter o diretório atual
def get_current_directory():
    return os.getcwd()

# Função para obter o usuário atual
def get_current_user():
    return getpass.getuser()

# Função para converter segundos em horas e minutos
def convert_seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return int(hours), int(minutes)

# Função para obter os serviços ativos
def get_active_services():
    services = [service.name() for service in psutil.win_service_iter() if service.status() == 'running']
    return services

if __name__ == "__main__":

    print("#########Status do PC#############")
   
    print(f"CPU: {psutil.cpu_percent()}%")
    print(f"Memória: {psutil.virtual_memory().percent}%")
    uptime_seconds = get_system_uptime()
    hours, minutes = convert_seconds_to_hms(uptime_seconds)
    print(f"Tempo de atividade do sistema: {hours} horas e {minutes} minutos")
    print(f"Diretório atual: {get_current_directory()}")
    print(f"Usuário atual: {get_current_user()}")
    print("Serviços ativos:")
    for service in get_active_services():
        print(f" - {service}")
    

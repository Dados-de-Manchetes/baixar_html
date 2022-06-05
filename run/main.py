#!/usr/bin/python3
import sys
import time
from datetime import datetime
from datetime import timedelta
import logging
sys.path.append("./repository")
sys.path.append("./service")

from service.instancias_service import em_processamento

APP_NAME = "run-download-paginas"

def init_log():
    logging.basicConfig(
        level=logging.INFO,format='[%(levelname)s] %(asctime)s >>> %(message)s',
        handlers=[
            logging.FileHandler(f'{APP_NAME}.log',),
            logging.StreamHandler()
        ])

'''
    Esse código funciona depois da criação dos recurso via terraform. Ele fica
    verificando se a instancia criada, pelo terraform, foi finalizada. Para isso
    consulta os arquivos de execução do terrafor e realiza uma consulta na AWS
'''
if __name__ == "__main__":
   
    init_log()  
    logging.info("Inicio da espera")
    
    tempo_maximo = datetime.now() + timedelta(minutes=30)
    while em_processamento() and datetime.now() < tempo_maximo:
        logging.info("Ainda não finalizou...")
        time.sleep(5)

    if datetime.now() > tempo_maximo:
        logging.error("Estouro de tempo de processamento")
    
    logging.info("Processo finalizado")
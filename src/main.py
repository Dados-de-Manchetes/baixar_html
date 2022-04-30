#!/usr/bin/python3
import sys
import logging
sys.path.append("./repository")
sys.path.append("./service")

from service.download_page_service import download_page_service
from service.dados_pagina_service import dados_pagina_service

APP_NAME="download-paginas"

def init_log():
    logging.basicConfig(
        level=logging.INFO,format='[%(levelname)s] %(asctime)s >>> %(message)s',
        handlers=[
            logging.FileHandler(f'{APP_NAME}.log',),
            logging.StreamHandler()
        ])

if __name__ == "__main__":

    init_log()

    logging.info("Iniciando o processo de download dos sites")
    for url in dados_pagina_service.find_lista_urls():
        logging.info(f"Iniciando o processo de downlaod para {url}")
        try:
            html = download_page_service.get(url)
            error = False
            logging.info(f"Processo de download ocorreu com sucesso {url}" )
        except Exception as e:
            html = download_page_service.get_code()
            error = True
            logging.error(f"Erro ao realizar o processo de download {url},\n{e}")


        dados_pagina_service.add_code(url, html, error)

    download_page_service.exit()
    logging.info("Processo de download finalizado")
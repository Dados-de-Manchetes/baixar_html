import logging

from repository.url_list_repository import url_list_repository
from repository.url_data_repository import url_data_repository

'''
    Classe responsável em gerenciar os dados sobre quais paginas devem ser
    baixadas e onde devem ser armazenadas.
'''
class DadosPaginaService:
    @classmethod
    def find_lista_urls(cls):
        return url_list_repository.find_lista_urls()

    @classmethod
    def add_code(cls, url, html, error)->None:
        try:
            url_data_repository.add_code(url,html,error)
            logging.info(f"Armazenamento dos dados do site aconteceu com sucesso {url} com tamanho de {len(html)}")
        except Exception as e:
            logging.error(f"Erro ao realizar o armazenamento de dados {url} com tamanho de {len(html)} {e}")

dados_pagina_service = DadosPaginaService()

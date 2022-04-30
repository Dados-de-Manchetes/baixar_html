from selenium import webdriver
from pyvirtualdisplay import Display

import logging

'''
    Classe responsavel em realizar o download do código das páginas atravez do 
    selenium. Por conta de rodar em um ambinte sem parte gráfica é necessário 
    virtualizar uma atravez do pyvirtualdisplay.
'''
class DownloadPageService:
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    }

    def __init__(cls):
        cls.display = Display(visible=0, size=(1024, 768))
        cls.display.start()
        cls.driver = webdriver.Firefox()
        cls.driver.set_page_load_timeout(60)
        cls.url = ''

    def get(cls, url):
        cls.url = url
        cls.driver.get(url)
        return str(cls.driver.page_source)

    def get_code(cls):
        try:
            return str(cls.driver.page_source)
        except:
            logging.error(f"Erro ao tentar capturar o código da página {cls.url}")
            return ''

    def __exit__(cls, exc_type, exc_val, exc_tb):
        cls.exit()

    def exit(cls):
        logging.info("Fechando o controlador de downloads")
        if cls.driver is not None:
            logging.info("Finalizando o selenium")
            cls.driver.close()

        if cls.display is not None:
            logging.info("Finalizando o displayvirtual")
            cls.display.stop()

download_page_service = DownloadPageService()
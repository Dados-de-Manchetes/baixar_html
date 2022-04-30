import boto3
import json

'''
    Acessa um s3 para capiturar quais devem ser os sites que devem baixados
'''
class UrlListRepository:
    BUCKETNAME = 'manchetes-dados'
    FILE_KEY = "url.list"
    
    def __init__(cls) -> None:
        pass

    @classmethod
    def _s3_resource(cls):
        return boto3.resource('s3')
        
    @classmethod
    def find_lista_urls(cls)->list:
        s3 = cls._s3_resource()
        obj = s3.Object(cls.BUCKETNAME, cls.FILE_KEY)

        arquivo = obj.get()['Body'].read()
        return json.loads(arquivo.decode())

url_list_repository = UrlListRepository()
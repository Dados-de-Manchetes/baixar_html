import json
import boto3
import uuid
import lzma
import datetime
import urllib.parse

'''
    Armazena os dados do site em um s3, os dados são compactados primeiro.
'''
class UrlDataRepository:
    BUCKET_NAME = 'manchetes-url-data'

    @classmethod
    def _s3_client(cls):
        return boto3.client('s3')

    @classmethod
    def add_code(cls,url: str, body: str, error: bool):
        s3_client = cls._s3_client()
        key = uuid.uuid4().hex
        tag = cls.generate_tags(key, url, error)
        file = cls.generate_file(key, url, body, error)
        file_comress = cls.compress(file)

        s3_client.put_object(
            Bucket=cls.BUCKET_NAME,
            Key=key,
            Body=file_comress,
            Tagging=tag
        )

    @classmethod
    def generate_file(cls, key: str, url: str, body: str,error: bool) -> bytes:
        file = dict()
        file['key'] = key
        file['url'] = url
        file['body'] = body
        file['compress'] = 'lzma'
        file['date_time'] = datetime.datetime.now().isoformat()
        if error:
            file['error'] = True
        return json.dumps(file).encode()

    @classmethod
    def generate_tags(cls, key: str , url: str, error: bool) ->str:
        tags = dict()

        tags['url'] = url
        tags['compress'] = 'lzma'
        tags['date_time'] = datetime.datetime.now().isoformat()
        if error:
            tags['error'] = True
        return urllib.parse.urlencode(tags)

    @classmethod
    def compress(cls, file):
        return lzma.compress(file)
    
url_data_repository = UrlDataRepository()
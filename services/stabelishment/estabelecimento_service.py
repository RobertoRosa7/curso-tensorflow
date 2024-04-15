# -*- coding: utf-8 -*-

import json
from urllib import request as req
from environment.env import environment

from reactivex import of

class EstabelecimentoService:

    def get_url(self, path: str) -> str:
        return '{}:{}{}'.format(environment.get('URL'), environment.get('PORT'), path)

    def get_csv(self, url: str) -> str:
        api = req.Request(self.get_url(url), method="GET")
        api.add_header('Content-type', 'text/csv')

        response = req.urlopen(api)
        raw_data = response.read()
        encoding = response.info().get_content_charset('utf8')

        return raw_data.decode(encoding)

    def delete_all(self, url: str, data: dict) -> dict:
        api = req.Request(self.get_url(url), method="POST")
        api.add_header('Content-type', 'application/json')

        response = req.urlopen(api, data=bytes(json.dumps(data), encoding='utf-8'))
        raw_data = response.read()
        encoding = response.info().get_content_charset('utf8')

        return raw_data.decode(encoding)

    def post_all(self, url: str, data: dict) -> dict:
        api = req.Request(self.get_url(url), method="POST")
        api.add_header('Content-type', 'application/json')

        response = req.urlopen(api, data=bytes(json.dumps(data), encoding='utf-8'))
        raw_data = response.read()
        encoding = response.info().get_content_charset('utf8')

        return raw_data.decode(encoding)
    
    def check_base(self, url: str):
        api = req.Request(self.get_url(url), method="GET")
        response = req.urlopen(api)
        raw_data = response.read()
        encoding = response.info().get_content_charset('utf8')
        
        return of(raw_data.decode(encoding))
    

from welkin.api_resources.abstract.api_resource import APIResource
from welkin.auth import Auth

import requests

class CreateableAPIResource(APIResource):
    @classmethod
    def create(cls, client_id, client_secret, data):
        url = cls.class_url()
        headers = Auth().get_headers(client_id, client_secret)
        resp = requests.post(url, headers=headers, json=data).json()
        return resp
        
    

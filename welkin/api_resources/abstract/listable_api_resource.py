from welkin.api_resources.abstract.api_resource import APIResource
from welkin.auth import Auth
import welkin.util as wu


import requests

class ListableAPIResource(APIResource):
    @classmethod
    def find(cls, client_id, client_secret):
        url = url = cls.class_url()
        headers = Auth().get_headers(client_id, client_secret)
        # resp = requests.get(url, headers=headers).json()
        try:
            resp = wu.process_request(url=url, headers=headers, method='get')
        except Exception as err:
            raise Exception(err)
        try:
            r_data = resp.json()
        except ValueError as err:
            raise Exception(err)
        return r_data

    
        
        

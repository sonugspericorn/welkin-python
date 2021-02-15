from welkin.api_resources.abstract.api_resource import APIResource
from welkin.auth import Auth

import requests

class UpdateableAPIResource(APIResource):
    @classmethod
    def modify(cls, client_id, client_secret, iden, data):
        url = cls.class_url() + "/" + iden
        headers = Auth().get_headers(client_id, client_secret)
        resp = request.put(url, headers=headers, json=data).json()
        return resp

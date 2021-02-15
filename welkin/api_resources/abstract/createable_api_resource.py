from welkin.api_resources.abstract.api_resource import APIResource
from welkin.auth import Auth
import welkin.util as wu


class CreateableAPIResource(APIResource):
    @classmethod
    def create(cls, client_id, client_secret, data):
        url = cls.class_url()
        headers = Auth().get_headers(client_id, client_secret)
        r_data = None
        # requests.post(url, headers=headers, json=data)
        try:
            resp = wu.process_request(url=url, headers=headers, json_data=data, method='post')
        except Exception as err:
            raise Exception(err)
        try:
            r_data = resp.json()
        except ValueError as err:
            raise Exception(err)
        return r_data

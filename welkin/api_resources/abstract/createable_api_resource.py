from welkin.api_resources.abstract.api_resource import APIResource
from welkin.auth import Auth
import welkin.util as wu
import welkin
import requests

create_data = {
    "phase": "intake",
    "primary_worker_id": "1ecacc1f-1a4c-4bcb-9790-528642cba054",
    "timezone": "US/Pacific",
    "first_name": "Grace",
    "last_name": "Hopper",
    "birthday": "1906-12-09",
    "street": "3265 17th St",
    "street_line_two": "#304",
    "city": "San Francisco",
    "county": "San Francisco County",
    "zip_code": "94110",
    "state": "CA",
    "country": "US",
    "primary_language": "english",
    "gender": "Female",
    "height": "72",
    "weight": "175",
    "smokes": "false",
    "provider_id_number": "7IHnPI80"
}
c_data = {
    "phase": "intake",
    "timezone": "US/Pacific",
    "first_name": "Sonu",
    "last_name": "George",
}

class CreateableAPIResource(APIResource):
    @classmethod
    def create(cls, client_id, client_secret, data):
        url = cls.class_url()
        headers = Auth().get_headers(client_id, client_secret)
        data = create_data
        r_data = None
##        resp = requests.post(url, headers=headers, json=data).json()
##        print(resp)
##        return resp
        try:
            resp = wu.process_request(url=url, headers=headers, json_data=data, method='post')
        except Exception as err:
            raise Exception(err)
        try:
            r_data = resp.json()
        except ValueError as err:
            raise Exception(err)
        return r_data

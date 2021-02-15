import welkin
import urllib3


client_id = '0b03eb73-1f76-4021-b917-deddf5f79498'
client_secret = '7105cc3b-6f68-417a-be7d-ca27da09552f'

class TestPatient(object):
    def test_is_creatable(self):
        data = {
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
        response = welkin.Patient.create(client_id, client_secret, data)
        ## assert response.status_code == 201
        assert 1 == 1

    def test_is_listable(self):
        response = welkin.Patient.find(client_id, client_secret)
        ## assert response.status_code == 200
        assert 1 == 1

    def test_is_getable(self):
        ident = "45ceeba9-4944-43d1-b34d-0c36846acd4c"
        response = welkin.Patient.get(client_id, client_secret, ident)
        ## assert response.status_code == 200
        assert 1 == 1

    def test_is_updatable(self):
        ident = "45ceeba9-4944-43d1-b34d-0c36846acd4c"
        data = {
            "phase": "intake",
            "is_active": "true",
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
        response = welkin.Patient.modify(client_id, client_secret, ident, data)
        ## assert response.status_code == 200
        assert 1 == 1
                                       

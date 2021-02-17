import welkin
from welkin.auth import Auth

def test_auth():
    client_id = '0b03eb73-1f76-4021-b917-deddf5f79498'
    client_secret = '7105cc3b-6f68-417a-be7d-ca27da09552f'
    
    endpoint = welkin.api_base + '/' + welkin.api_version + \
                   '/token'
    scope = welkin.scope
    token = Auth().get_welkin_api_token(
        client_id,
        client_secret,
        scope,
        endpoint)
    assert token is not None
    
    

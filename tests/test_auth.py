from welkin.auth import Auth
import welkin

class TestAuth(object):
    def test_get_welkin_api_token(self):
        client_id =  '54637'# welkin.client_id
        client_secret = '43215'# welkin.client_secret
        endpoint = welkin.api_base + '/' + welkin.api_version + \
                   '/token'
        scope = welkin.scope
        
        
        
    

import arrow
import jwt
import requests
import welkin
from welkin import util
from welkin import auth_error
JWT_BEARER_URI = 'urn:ietf:params:oauth:grant-type:jwt-bearer'

class Auth:
    
    def get_welkin_api_token(self, client_id, client_secret, scope, endpoint):
      claim = {
        'iss': client_id,
        'aud': endpoint,
        'exp': arrow.utcnow().shift(seconds=3600).timestamp,
        'scope': scope,
      }
      assertion = jwt.encode(claim, client_secret, algorithm='HS256')
      params = {
        'assertion': assertion,
        'grant_type': JWT_BEARER_URI
      }
      resp = requests.post(endpoint, data=params)
      if resp.status_code == 400:
          util.log_debug('Key Error')
          raise KeyError(
              "Wrong client_id or client_secret provided "
              )
        
      token = resp.json()['access_token']
      return token

    def get_headers(self, client_id, client_secret):
        endpoint = welkin.api_base + '/' + welkin.api_version + \
                   '/token'
        scope = welkin.scope
        token = self.get_welkin_api_token(client_id,
                                     client_secret,
                                     scope,
                                     endpoint)
        headers = {"Authorization": "Bearer "+token}
        return headers
        
        

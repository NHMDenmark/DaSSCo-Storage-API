import time
import requests
from dasscostorageclient.exceptions import APIError

class AuthManager:

   def __init__(self, auth_url: str, realm: str, client_id: str, client_secret: str):
       self.auth_url = auth_url
       self.realm = realm
       self.client_id = client_id
       self.client_secret = client_secret
       self._obtain_token()

   def _obtain_token(self):
       body = {
           "grant_type": "client_credentials",
           "client_id": self.client_id,
           "client_secret": self.client_secret,
           "scope": "openid"
       }

       res = requests.post(self._token_endpoint(), data=body)

       if res.status_code != 200:
           raise APIError(res)

       token_data = res.json()

       self.token = token_data["access_token"]
       self.expires_at = time.time() + token_data["expires_in"] - 5

   def _token_endpoint(self) -> str:
       return f"{self.auth_url}/realms/{self.realm}/protocol/openid-connect/token"

   def get_token(self):
       if time.time() >= self.expires_at:
           self._obtain_token()
       return self.token
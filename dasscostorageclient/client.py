import requests
from dasscostorageclient.auth import AuthManager
from dasscostorageclient.constants import DASSCO_AUTH_URL, DASSCO_REALM, ARS_BASE_URL
from dasscostorageclient.exceptions import APIError
from dasscostorageclient.resources.assets import AssetResource
from dasscostorageclient.resources.fileproxy import FileProxyResource
from dasscostorageclient.resources.institutions import InstitutionResource

class DaSSCoStorageClient:

    def __init__(self, client_id: str, client_secret: str):
        self.auth_manager = AuthManager(
            auth_url=DASSCO_AUTH_URL,
            realm=DASSCO_REALM,
            client_id=client_id,
            client_secret=client_secret
        )

        self.ars_url = f"{ARS_BASE_URL}/ars/api"
        self.file_proxy_url = f"{ARS_BASE_URL}/file_proxy/api"

        self.institutions = InstitutionResource(self)
        self.assets = AssetResource(self)
        self.files = FileProxyResource(self)

    def request(self, method: str, path: str, json: dict = None, data = None, use_file_proxy: bool = False) -> requests.Response:
        base_url = self.file_proxy_url if use_file_proxy else self.ars_url
        api_url = f"{base_url}{path}"

        content_type = (
            "application/octet-stream" if use_file_proxy and method.upper() == "PUT"
            else "application/json"
        )

        headers = {
            "Authorization": f"Bearer {self.auth_manager.get_token()}",
            "Content-Type": content_type
        }

        res = requests.request(method, api_url, headers=headers, json=json, data=data)

        if 200 <= res.status_code <= 299:
            return res
        else:
            raise APIError(res)
class BaseResource:
   def __init__(self, client, prefix: str, use_file_proxy: bool = False):
       self._client = client
       self._prefix = prefix
       self.use_file_proxy = use_file_proxy

   def _get(self, path: str = ""):
       request_path = f"{self._prefix}{path}"
       return self._client.request("GET", request_path, use_file_proxy=self.use_file_proxy)

   def _post(self, path: str = "", body: dict = None):
       request_path = f"{self._prefix}{path}"
       return self._client.request("POST", request_path, json=body, use_file_proxy=self.use_file_proxy)

   def _put(self, path: str = "", body: dict = None, data = None):
       request_path = f"{self._prefix}{path}"
       return self._client.request("PUT", request_path, json=body, data=data, use_file_proxy=self.use_file_proxy)

   def _delete(self, path: str = ""):
       request_path = f"{self._prefix}{path}"
       return self._client.request("DELETE", request_path, use_file_proxy=self.use_file_proxy)
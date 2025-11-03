class APIError(Exception):
    def __init__(self, response):
        self.response = response
        self.status_code = response.status_code
        super().__init__(self._create_message())

    def _create_message(self):
        return f"API request failed with status code {self.status_code}: {self.response.content}"


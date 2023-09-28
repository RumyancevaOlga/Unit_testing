class HttpClient:

    def get(self, url: str) -> str:
        return f'Возвращаю по {url} какую-то строку'


class WebService:

    def __init__(self, http_client: HttpClient):
        self._http_client = http_client

    @property
    def http_client(self):
        return self._http_client

    def data(self, url: str) -> None:
        self._http_client.get(url)

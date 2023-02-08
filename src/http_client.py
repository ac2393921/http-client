from typing import Protocol, Optional

from requests.models import Response
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from requests import Session


class HttpClient(Protocol):
    def get(self) -> Response:
        raise NotImplementedError

    def post(self) -> Response:
        raise NotImplementedError


class DefaultHttpClient:
    def __init__(self, retry_time: int = 3, backoff_factor: int = 1):
        retry_strategy = Retry(
            total=retry_time,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=backoff_factor,
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        http = Session()
        http.mount("http://", adapter)
        http.mount("https://", adapter)
        self.client: Session = http

    def get(
        self,
        url: str,
        params: Optional[dict] = None,
        connect_timeout: float = 3,
        read_timeout: float = 3,
    ) -> Response:
        return self.client.get(
            url=url, params=params, timeout=(connect_timeout, read_timeout)
        )

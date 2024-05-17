from typing import Optional, Dict, Any, Literal, overload
import requests


class BaseApi:

    def __init__(self, base_url: str, header: Dict[str, str]):
        self.base_url = base_url
        self.headers = header

    @overload
    def _request(
        self,
        method: Literal["GET", "OPTIONS", "HEAD", "POST", "PUT", "PATCH",
                        "DELETE"],
        endpoint: str,
        headers: Optional[Dict[str, str]] = None,
        body: Optional[Any] = None,
    ) -> requests.Response:
        ...

    def _request(
        self,
        method: Literal["GET", "OPTIONS", "HEAD", "POST", "PUT", "PATCH",
                        "DELETE"],
        endpoint: str,
        headers: Optional[Dict[str, str]] = None,
        body: Optional[Any] = None,
    ) -> requests.Response:
        final_headers = self.headers.copy()
        if headers:
            final_headers.update(headers)

        if 'content-type' not in final_headers:
            final_headers['content-type'] = 'application/json'

        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.request(method,
                                        url,
                                        headers=final_headers,
                                        json=body)
            response.raise_for_status()
            return response
        except requests.HTTPError as e:
            raise
        except requests.RequestException as e:
            raise

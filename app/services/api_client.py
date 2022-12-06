"""
APIRequest
"""
import json
import logging
from urllib.parse import urljoin

import requests

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class APIRequest(object):
    def __init__(self, base_url, headers=None):
        if not base_url.endswith("/"):
            base_url += "/"
        self._base_url = base_url

        if headers is not None:
            self._headers = headers
        else:
            self._headers = {}

    def send_request(self, method, route, params=None, **kwargs):
        """
        Send a request to an endpoint
        Args:
            method: str
            route: str
            **kwargs
        """
        if route.startswith("/"):
            route = route[1:]

        url = urljoin(self._base_url, route, allow_fragments=False)

        headers = kwargs.pop("headers", {})
        headers.update(self._headers)

        response = requests.request(
            method=method, url=url, headers=headers, params=params, **kwargs
        )

        if "data" in kwargs:
            log.info(
                "{} {} with headers:\n{}\nand data:\n{}".format(
                    method,
                    url,
                    json.dumps(headers, indent=4),
                    json.dumps(kwargs["data"], indent=4),
                )
            )
        elif "json" in kwargs:
            log.info(
                "{} {} with headers:\n{}\nand JSON:\n{}".format(
                    method,
                    url,
                    json.dumps(headers, indent=4),
                    json.dumps(kwargs["json"], indent=4),
                )
            )
        else:
            log.info(
                "{} {} with headers:\n{}".format(
                    method, url, json.dumps(headers, indent=4)
                )
            )

        log.info(
            "Response to {} {} => {} {}\n{}".format(
                method,
                url,
                response.status_code,
                response.reason,
                response.text[:100],
            )
        )

        return response

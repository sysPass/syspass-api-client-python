import os

import requests


class ApiError(Exception):
    pass


class JsonRpcApi:
    _request_id = 0

    def __init__(self,
                 url: str = None,
                 auth_token: str = None):
        """"
        :param url: sysPass API URL for requests
        :param auth_token: sysPass API authorization token
        """
        self.url = url
        self.auth_token = auth_token

        self._get_settings_from_env()

    def _get_settings_from_env(self):
        """
        Try to set the API setting from the environment variables
        """
        if not self.url:
            self.url = os.environ.get("SYSPASS_API_URL")

        if not self.auth_token:
            self.auth_token = os.environ.get("SYSPASS_API_TOKEN")

    def _pre_flight_check(self):
        """
        Check for required setting before making the request
        """
        if not self.url:
            raise ApiError("API URL not set")

        if not self.auth_token:
            raise ApiError("API Token not set")

    def _build_json_rpc(self, method: str, params: dict) -> dict:
        """
        Builds a JSON-RPC request with the given data
        :param method: method to request for
        :param params: parameters to pass to the API
        :return:
        """
        out_params = {}

        if params:
            out_params.update(params)

        out_params["authToken"] = self.auth_token

        self._request_id += 1

        return {
            "jsonrpc": "2.0",
            "method": method,
            "params": out_params,
            "id": self._request_id
        }

    def call_api(self, method: str, params: dict) -> dict:
        """
        Makes an API call with the given data and settings
        :param method: method to request for
        :param params: parameters to pass to the API
        :return:
        """
        self._pre_flight_check()

        r = requests.post(self.url,
                          json=self._build_json_rpc(method, params),
                          verify=False)

        r.raise_for_status()

        out = r.json()

        if out.get("error"):
            raise ApiError("Sorry, there was an error: {0} ({1})"
                           .format(out["error"]["message"], out["error"]["code"]))

        return out


class ApiBase:
    def __init__(self, api: JsonRpcApi):
        """
        :param api: The Api object
        """
        self.api = api

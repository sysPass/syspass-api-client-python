import unittest
from unittest.mock import patch

import requests

from syspass_api_client import api
from tests import data_mocks


class TestApi(unittest.TestCase):

    def test_call_api_no_url(self):
        with self.assertRaises(api.ApiError):
            api.JsonRpcApi() \
                .call_api(method="method/action", params={})

    def test_call_api_no_token(self):
        with self.assertRaises(api.ApiError):
            api.JsonRpcApi(url="http://syspass.org/api.php") \
                .call_api(method="method/action", params={})

    @patch("syspass_api_client.api.requests.post")
    def test_call_api(self, mock_requests):
        mock_requests.return_value.status_code = 200
        mock_requests.return_value.json.return_value = data_mocks.accounts

        o_api = api.JsonRpcApi(url="http://syspass.org/api.php", auth_token="syspass")
        data = o_api.call_api(method="method/action", params={})

        self.assertEqual(data, data_mocks.accounts)

    @patch("syspass_api_client.api.requests.post")
    def test_call_api_error_data(self, mock_requests):
        mock_requests.return_value.status_code = 200
        mock_requests.return_value.json.return_value = data_mocks.error_request

        o_api = api.JsonRpcApi(url="http://syspass.org/api.php", auth_token="syspass")

        with self.assertRaises(api.ApiError):
            o_api.call_api(method="method/action", params={})

    def test_call_api_error_request(self):
        o_api = api.JsonRpcApi(url="http://example.com/api.php", auth_token="syspass")

        with self.assertRaises(requests.exceptions.HTTPError):
            o_api.call_api(method="method/action", params={})


if __name__ == "__main__":
    unittest.main()

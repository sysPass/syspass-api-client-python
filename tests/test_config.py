import unittest
from unittest.mock import patch

from syspass_api_client import api, config


class TestConfig(unittest.TestCase):

    def setUp(self) -> None:
        self.config = config.Config(api.JsonRpcApi(url="http://syspass.org/api.php", auth_token="syspass"))

    @patch.object(api.JsonRpcApi, "call_api")
    def test_export(self, mock_call_api):
        self.config.export(path="/test/path", password="test_pass")

        mock_call_api.assert_called_with(params={"path": "/test/path", "password": "test_pass"},
                                         method='config/export')

    @patch.object(api.JsonRpcApi, "call_api")
    def test_backup(self, mock_call_api):
        self.config.backup(path="/test/path")

        mock_call_api.assert_called_with(params={"path": "/test/path"}, method='config/backup')

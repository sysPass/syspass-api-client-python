import unittest
from unittest.mock import patch

from syspass_api_client import api, client
from tests import data_mocks


class TestClient(unittest.TestCase):

    def setUp(self) -> None:
        self.client = client.Client(api.JsonRpcApi(url="http://syspass.org/api.php", auth_token="syspass"))

    @patch.object(api.JsonRpcApi, "call_api")
    def test_search(self, mock_call_api):
        mock_call_api.return_value = data_mocks.clients

        data = self.client.search()

        mock_call_api.assert_called_with(params={}, method='client/search')

        self.assertEqual(6, len(data))

        self.client.search(text="Google", count=10)

        expected_params = {
            "text": "Google",
            "count": 10,
        }

        mock_call_api.assert_called_with(params=expected_params, method='client/search')

    @patch.object(api.JsonRpcApi, "call_api")
    def test_view(self, mock_call_api):
        self.client.view(client_id=2)

        mock_call_api.assert_called_with(params={"id": 2}, method='client/view')

    @patch.object(api.JsonRpcApi, "call_api")
    def test_create(self, mock_call_api):
        client_data = client.ClientData(name="Test Python",
                                        description="test",
                                        is_global=True)

        self.client.create(client_data)

        mock_call_api.assert_called_with(params=client_data.params, method='client/create')

    @patch.object(api.JsonRpcApi, "call_api")
    def test_edit(self, mock_call_api):
        client_data = client.ClientData(name="Test Python",
                                        description="test",
                                        is_global=True,
                                        client_id=1)

        self.client.edit(client_data)

        mock_call_api.assert_called_with(params=client_data.params, method='client/edit')

    @patch.object(api.JsonRpcApi, "call_api")
    def test_delete(self, mock_call_api):
        self.client.delete(client_id=2)

        mock_call_api.assert_called_with(params={"id": 2}, method='client/delete')


if __name__ == "__main__":
    unittest.main()

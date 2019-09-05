import time
import unittest
from unittest.mock import patch

from syspass_api_client import api, account
from tests import data_mocks


class TestAccount(unittest.TestCase):

    def setUp(self) -> None:
        self.account = account.Account(api.JsonRpcApi(url="http://syspass.org/api.php", auth_token="syspass"))

    @patch.object(api.JsonRpcApi, "call_api")
    def test_search(self, mock_call_api):
        mock_call_api.return_value = data_mocks.accounts

        data = self.account.search()

        mock_call_api.assert_called_with(params={}, method='account/search')

        self.assertEqual(10, len(data))

        self.account.search(text="Google", count=10, category_id=1, client_id=1, tags_id=[2], operator="or")

        expected_params = {
            "text": "Google",
            "count": 10,
            "categoryId": 1,
            "clientId": 1,
            "tagsId": [2],
            "op": "or"
        }

        mock_call_api.assert_called_with(params=expected_params, method='account/search')

    @patch.object(api.JsonRpcApi, "call_api")
    def test_view(self, mock_call_api):
        mock_call_api.return_value = data_mocks.accounts

        self.account.view(account_id=2)

        mock_call_api.assert_called_with(params={"id": 2}, method='account/view')

    @patch.object(api.JsonRpcApi, "call_api")
    def test_view_pass(self, mock_call_api):
        mock_call_api.return_value = data_mocks.accounts

        self.account.view_pass(account_id=2)

        mock_call_api.assert_called_with(params={"id": 2, "tokenPass": self.account.token_pass},
                                         method='account/viewPass')

    @patch.object(api.JsonRpcApi, "call_api")
    def test_create(self, mock_call_api):
        account_data = account.AccountData(name="Test Python",
                                           category_id=1,
                                           client_id=1,
                                           tags_id=[2],
                                           url="http://syspass.org",
                                           login="test",
                                           password="test123",
                                           notes="notes for the account",
                                           private=True,
                                           private_group=True,
                                           expire_date=int(time.time()))

        self.account.create(account_data)

        expected_params = {"tokenPass": self.account.token_pass}
        expected_params.update(account_data.params)

        mock_call_api.assert_called_with(params=expected_params, method='account/create')

    @patch.object(api.JsonRpcApi, "call_api")
    def test_edit(self, mock_call_api):
        account_data = account.AccountData(name="Test Python",
                                           category_id=1,
                                           client_id=1,
                                           tags_id=[2],
                                           url="http://syspass.org",
                                           login="test",
                                           password="test123",
                                           notes="notes for the account",
                                           private=True,
                                           private_group=True,
                                           expire_date=int(time.time()),
                                           account_id=1)

        self.account.edit(account_data)

        expected_params = {"tokenPass": self.account.token_pass}
        expected_params.update(account_data.params)

        mock_call_api.assert_called_with(params=expected_params, method='account/edit')

    @patch.object(api.JsonRpcApi, "call_api")
    def test_delete(self, mock_call_api):
        mock_call_api.return_value = data_mocks.accounts

        self.account.delete(account_id=2)

        mock_call_api.assert_called_with(params={"id": 2}, method='account/delete')


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from syspass_api_client import api, user_group
from tests import data_mocks


class TestUserGroup(unittest.TestCase):

    def setUp(self) -> None:
        self.user_group = user_group.UserGroup(api.JsonRpcApi(url="http://syspass.org/api.php", auth_token="syspass"))

    @patch.object(api.JsonRpcApi, "call_api")
    def test_search(self, mock_call_api):
        mock_call_api.return_value = data_mocks.user_groups

        data = self.user_group.search()

        mock_call_api.assert_called_with(params={}, method='userGroup/search')

        self.assertEqual(2, len(data))

        self.user_group.search(text="Google", count=10)

        expected_params = {
            "text": "Google",
            "count": 10,
        }

        mock_call_api.assert_called_with(params=expected_params, method='userGroup/search')

    @patch.object(api.JsonRpcApi, "call_api")
    def test_view(self, mock_call_api):
        self.user_group.view(user_group_id=2)

        mock_call_api.assert_called_with(params={"id": 2}, method='userGroup/view')

    @patch.object(api.JsonRpcApi, "call_api")
    def test_create(self, mock_call_api):
        user_group_data = user_group.UserGroupData(name="Test Python",
                                                   description="test",
                                                   users_id=[2, 3])

        self.user_group.create(user_group_data)

        mock_call_api.assert_called_with(params=user_group_data.params, method='userGroup/create')

    @patch.object(api.JsonRpcApi, "call_api")
    def test_edit(self, mock_call_api):
        user_group_data = user_group.UserGroupData(name="Test Python",
                                                   description="test",
                                                   users_id=[2, 3],
                                                   user_group_id=1)

        self.user_group.edit(user_group_data)

        mock_call_api.assert_called_with(params=user_group_data.params, method='userGroup/edit')

    @patch.object(api.JsonRpcApi, "call_api")
    def test_delete(self, mock_call_api):
        self.user_group.delete(user_group_id=2)

        mock_call_api.assert_called_with(params={"id": 2}, method='userGroup/delete')


if __name__ == "__main__":
    unittest.main()

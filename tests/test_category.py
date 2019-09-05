import unittest
from unittest.mock import patch

from syspass_api_client import api, category
from tests import data_mocks


class TestCategory(unittest.TestCase):

    def setUp(self) -> None:
        self.category = category.Category(api.JsonRpcApi(url="http://syspass.org/api.php", auth_token="syspass"))

    @patch.object(api.JsonRpcApi, "call_api")
    def test_search(self, mock_call_api):
        mock_call_api.return_value = data_mocks.categories

        data = self.category.search()

        mock_call_api.assert_called_with(params={}, method='category/search')

        self.assertEqual(7, len(data))

        self.category.search(text="Google", count=10)

        expected_params = {
            "text": "Google",
            "count": 10,
        }

        mock_call_api.assert_called_with(params=expected_params, method='category/search')

    @patch.object(api.JsonRpcApi, "call_api")
    def test_view(self, mock_call_api):
        self.category.view(category_id=2)

        mock_call_api.assert_called_with(params={"id": 2}, method='category/view')

    @patch.object(api.JsonRpcApi, "call_api")
    def test_create(self, mock_call_api):
        category_data = category.CategoryData(name="Test Python",
                                              description="test")

        self.category.create(category_data)

        mock_call_api.assert_called_with(params=category_data.params, method='category/create')

    @patch.object(api.JsonRpcApi, "call_api")
    def test_edit(self, mock_call_api):
        category_data = category.CategoryData(name="Test Python",
                                              description="test",
                                              category_id=1)

        self.category.edit(category_data)

        mock_call_api.assert_called_with(params=category_data.params, method='category/edit')

    @patch.object(api.JsonRpcApi, "call_api")
    def test_delete(self, mock_call_api):
        self.category.delete(category_id=2)

        mock_call_api.assert_called_with(params={"id": 2}, method='category/delete')


if __name__ == "__main__":
    unittest.main()

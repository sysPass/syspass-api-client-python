import unittest
from unittest.mock import patch

from syspass_api_client import api, tag
from tests import data_mocks


class TestTag(unittest.TestCase):

    def setUp(self) -> None:
        self.tag = tag.Tag(api.JsonRpcApi(url="http://syspass.org/api.php", auth_token="syspass"))

    @patch.object(api.JsonRpcApi, "call_api")
    def test_search(self, mock_call_api):
        mock_call_api.return_value = data_mocks.tags

        data = self.tag.search()

        mock_call_api.assert_called_with(params={}, method='tag/search')

        self.assertEqual(12, len(data))

        self.tag.search(text="Google", count=10)

        expected_params = {
            "text": "Google",
            "count": 10,
        }

        mock_call_api.assert_called_with(params=expected_params, method='tag/search')

    @patch.object(api.JsonRpcApi, "call_api")
    def test_view(self, mock_call_api):
        self.tag.view(tag_id=2)

        mock_call_api.assert_called_with(params={"id": 2}, method='tag/view')

    @patch.object(api.JsonRpcApi, "call_api")
    def test_create(self, mock_call_api):
        tag_data = tag.TagData(name="Test Python")

        self.tag.create(tag_data)

        mock_call_api.assert_called_with(params=tag_data.params, method='tag/create')

    @patch.object(api.JsonRpcApi, "call_api")
    def test_edit(self, mock_call_api):
        tag_data = tag.TagData(name="Test Python", tag_id=1)

        self.tag.edit(tag_data)

        mock_call_api.assert_called_with(params=tag_data.params, method='tag/edit')

    @patch.object(api.JsonRpcApi, "call_api")
    def test_delete(self, mock_call_api):
        self.tag.delete(tag_id=2)

        mock_call_api.assert_called_with(params={"id": 2}, method='tag/delete')


if __name__ == "__main__":
    unittest.main()

from syspass_api_client import api

METHODS = {
    "search": "tag/search",
    "view": "tag/view",
    "create": "tag/create",
    "edit": "tag/edit",
    "delete": "tag/delete",
}


class TagData:
    """
    Data class for tag's values
    """

    def __init__(self,
                 name: str,
                 tag_id: int = None):
        self.params = {
            "id": tag_id,
            "name": name
        }


class Tag(api.ApiBase):
    def search(self,
               text: str = None,
               count: int = None) -> dict:
        """
        Search for tags
        :param text: Text string for filtering results
        :param count:  Number of results to return
        :return: a list of dictionaries containing the tag' values
        """
        params = {}

        if text:
            params["text"] = text

        if count:
            params["count"] = count

        data = self.api.call_api(method=METHODS["search"], params=params)

        return data["result"]["result"]

    def view(self, tag_id: int) -> dict:
        """
        :param tag_id: Tag's ID
        :return: a dictionary with the tag's data
        """
        params = {
            "id": tag_id
        }

        data = self.api.call_api(method=METHODS["view"], params=params)

        return data["result"]["result"]

    def create(self, data: TagData) -> dict:
        """
        :param data: TagData object with the tag's values
        :return: a dictionary with the tag's ID and data
        """
        return self.api.call_api(method=METHODS["create"], params=data.params)

    def edit(self, data: TagData) -> dict:
        """
        :param data: TagData object with the tag's values. The tag's ID must be set
        :return: a dictionary with the tag's ID and data
        """
        if not data.params["id"]:
            raise api.ApiError("Tag ID not set")

        return self.api.call_api(method=METHODS["edit"], params=data.params)

    def delete(self, tag_id: int):
        """
        :param tag_id: Tag's ID to delete
        """
        params = {
            "id": tag_id
        }

        return self.api.call_api(method=METHODS["delete"], params=params)

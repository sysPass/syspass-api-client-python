from syspass_api_client import api

METHODS = {
    "search": "category/search",
    "view": "category/view",
    "create": "category/create",
    "edit": "category/edit",
    "delete": "category/delete",
}


class CategoryData:
    """
    Data class for category's values
    """

    def __init__(self,
                 name: str,
                 description: str = None,
                 category_id: int = None):
        self.params = {
            "id": category_id,
            "name": name,
            "description": description
        }


class Category(api.ApiBase):
    def search(self,
               text: str = None,
               count: int = None) -> list:
        """
        Search for categories
        :param text: Text string for filtering results
        :param count:  Number of results to return
        :return: a list of dictionaries containing the categories' values
        """
        params = {}

        if text:
            params["text"] = text

        if count:
            params["count"] = count

        data = self.api.call_api(method=METHODS["search"], params=params)

        return data["result"]["result"]

    def view(self, category_id: int) -> dict:
        """
        :param category_id: Category's ID
        :return: a dictionary with the category's data
        """
        params = {
            "id": category_id
        }

        data = self.api.call_api(method=METHODS["view"], params=params)

        return data["result"]["result"]

    def create(self, data: CategoryData) -> dict:
        """
        :param data: CategoryData object with the category's values
        :return: a dictionary with the category's ID and data
        """
        return self.api.call_api(method=METHODS["create"], params=data.params)

    def edit(self, data: CategoryData) -> dict:
        """
        :param data: CategoryData object with the category's values. The category's ID must be set
        :return: a dictionary with the category's ID and data
        """
        if not data.params["id"]:
            raise api.ApiError("Category ID not set")

        return self.api.call_api(method=METHODS["edit"], params=data.params)

    def delete(self, category_id: int):
        """
        :param category_id: Category's ID to delete
        """
        params = {
            "id": category_id
        }

        return self.api.call_api(method=METHODS["delete"], params=params)

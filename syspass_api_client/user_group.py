from typing import List

from syspass_api_client import api

METHODS = {
    "search": "userGroup/search",
    "view": "userGroup/view",
    "create": "userGroup/create",
    "edit": "userGroup/edit",
    "delete": "userGroup/delete",
}


class UserGroupData:
    """
    Data class for user group's values
    """

    def __init__(self,
                 name: str,
                 description: str = None,
                 users_id: List[int] = None,
                 user_group_id: int = None):
        self.params = {
            "id": user_group_id,
            "name": name,
            "description": description,
            "usersId": users_id
        }


class UserGroup(api.ApiBase):
    def search(self,
               text: str = None,
               count: int = None) -> dict:
        """
        Search for user groups
        :param text: Text string for filtering results
        :param count:  Number of results to return
        :return: a list of dictionaries containing the user groups' values
        """
        params = {}

        if text:
            params["text"] = text

        if count:
            params["count"] = count

        data = self.api.call_api(method=METHODS["search"], params=params)

        return data["result"]["result"]

    def view(self, user_group_id: int) -> dict:
        """
        :param user_group_id: User group's ID
        :return: a dictionary with the user group's data
        """
        params = {
            "id": user_group_id
        }

        data = self.api.call_api(method=METHODS["view"], params=params)

        return data["result"]["result"]

    def create(self, data: UserGroupData) -> dict:
        """
        :param data: UserGroupData object with the user group's values
        :return: a dictionary with the user group's ID and data
        """
        return self.api.call_api(method=METHODS["create"], params=data.params)

    def edit(self, data: UserGroupData) -> dict:
        """
        :param data: UserGroupData object with the user group's values. The user group's ID must be set
        :return: a dictionary with the user group's ID and data
        """
        if not data.params["id"]:
            raise api.ApiError("User group ID not set")

        return self.api.call_api(method=METHODS["edit"], params=data.params)

    def delete(self, user_group_id: int):
        """
        :param user_group_id: User group's ID to delete
        """
        params = {
            "id": user_group_id
        }

        return self.api.call_api(method=METHODS["delete"], params=params)

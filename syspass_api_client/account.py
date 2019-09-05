import os
from typing import List

from syspass_api_client import api

METHODS = {
    "search": "account/search",
    "view": "account/view",
    "view_pass": "account/viewPass",
    "edit_pass": "account/editPass",
    "create": "account/create",
    "edit": "account/edit",
    "delete": "account/delete",
}


class AccountData:
    """
    Data class for account's values
    """

    def __init__(self,
                 name: str,
                 category_id: int,
                 client_id: int,
                 password: str,
                 account_id: int = None,
                 tags_id: List[int] = None,
                 user_group_id: int = None,
                 parent_id: int = None,
                 login: str = None,
                 url: str = None,
                 notes: str = None,
                 private: int = None,
                 private_group: int = None,
                 expire_date: int = None):
        self.params = {
            "id": account_id,
            "name": name,
            "categoryId": category_id,
            "clientId": client_id,
            "pass": password,
            "tagsId": tags_id,
            "userGroupId": user_group_id,
            "parentId": parent_id,
            "login": login,
            "url": url,
            "notes": notes,
            "private": private,
            "privateGroup": private_group,
            "expireDate": expire_date,
        }


class Account(api.ApiBase):
    def __init__(self, o_api: api.JsonRpcApi, token_pass=None):
        """
        :param api: The Api object
        :param token_pass: sysPass API token pass for decrypting data
        """
        super().__init__(o_api)

        if token_pass:
            self.token_pass = token_pass
        else:
            self.token_pass = os.environ.get("SYSPASS_API_TOKEN_PASS")

    def search(self,
               text: str = None,
               count: int = None,
               category_id: int = None,
               client_id: int = None,
               tags_id: list = None,
               operator: str = None) -> list:
        """
        Search for accounts
        :param text: Text string for filtering results
        :param count:  Number of results to return
        :param category_id:  Account's category ID for filtering
        :param client_id: Account's client ID for filtering
        :param tags_id:  List of account's tags for filtering
        :param operator: Operator use to build the filter
        :return: a list of dictionaries containing the accounts' values
        """
        params = {}

        if text:
            params["text"] = text

        if count:
            params["count"] = count

        if category_id:
            params["categoryId"] = category_id

        if client_id:
            params["clientId"] = client_id

        if tags_id:
            params["tagsId"] = tags_id

        if operator:
            params["op"] = operator

        data = self.api.call_api(method=METHODS["search"], params=params)

        return data["result"]["result"]

    def view(self, account_id: int) -> dict:
        """
        :param account_id: Account's ID
        :return: a dictionary with the account's data
        """
        params = {
            "id": account_id
        }

        data = self.api.call_api(method=METHODS["view"], params=params)

        return data["result"]["result"]

    def view_pass(self, account_id: int) -> dict:
        """
        :param account_id: Account's ID
        :return: a dictionary with the account's password
        """
        params = {
            "tokenPass": self.token_pass,
            "id": account_id
        }

        data = self.api.call_api(method=METHODS["view_pass"], params=params)

        return data["result"]["result"]

    def create(self, data: AccountData) -> dict:
        """
        :param data: AccountData object with the account's values
        :return: a dictionary with the account's ID and data
        """
        params = {
            "tokenPass": self.token_pass
        }

        params.update(data.params)

        data = self.api.call_api(method=METHODS["create"], params=params)

        return data["result"]

    def edit(self, data: AccountData) -> dict:
        """
        :param data: AccountData object with the account's values. The account's ID must be set
        :return: a dictionary with the account's ID and data
        """
        if not data.params["id"]:
            raise api.ApiError("Account ID not set")

        params = {
            "tokenPass": self.token_pass
        }

        params.update(data.params)

        data = self.api.call_api(method=METHODS["edit"], params=params)

        return data["result"]

    def delete(self, account_id: int):
        """
        :param account_id: Account's ID to delete
        """
        params = {
            "id": account_id
        }

        return self.api.call_api(method=METHODS["delete"], params=params)

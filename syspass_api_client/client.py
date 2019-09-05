from syspass_api_client import api

METHODS = {
    "search": "client/search",
    "view": "client/view",
    "create": "client/create",
    "edit": "client/edit",
    "delete": "client/delete",
}


class ClientData:
    """
    Data class for client's values
    """

    def __init__(self,
                 name: str,
                 description: str = None,
                 is_global: bool = None,
                 client_id: int = None):
        self.params = {
            "id": client_id,
            "name": name,
            "description": description,
            "global": is_global
        }


class Client(api.ApiBase):
    def search(self,
               text: str = None,
               count: int = None) -> list:
        """
        Search for clients
        :param text: Text string for filtering results
        :param count:  Number of results to return
        :return: a list of dictionaries containing the clients' values
        """
        params = {}

        if text:
            params["text"] = text

        if count:
            params["count"] = count

        data = self.api.call_api(method=METHODS["search"], params=params)

        return data["result"]["result"]

    def view(self, client_id: int) -> dict:
        """
        :param client_id: Client's ID
        :return: a dictionary with the client's data
        """
        params = {
            "id": client_id
        }

        data = self.api.call_api(method=METHODS["view"], params=params)

        return data["result"]["result"]

    def create(self, data: ClientData) -> dict:
        """
        :param data: ClientData object with the client's values
        :return: a dictionary with the client's ID and data
        """
        return self.api.call_api(method=METHODS["create"], params=data.params)

    def edit(self, data: ClientData) -> dict:
        """
        :param data: ClientData object with the client's values. The client's ID must be set
        :return: a dictionary with the client's ID and data
        """
        if not data.params["id"]:
            raise api.ApiError("Client ID not set")

        return self.api.call_api(method=METHODS["edit"], params=data.params)

    def delete(self, client_id: int):
        """
        :param client_id: Client's ID to delete
        """
        params = {
            "id": client_id
        }

        return self.api.call_api(method=METHODS["delete"], params=params)

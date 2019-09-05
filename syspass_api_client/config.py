from syspass_api_client import api

METHODS = {
    "backup": "config/backup",
    "export": "config/export"
}


class Config(api.ApiBase):
    def backup(self, path: str) -> dict:
        """
        Perform a sysPass backup
        :param path: path where store the backup in
        :return:
        """
        params = {
            "path": path
        }

        data = self.api.call_api(method=METHODS["backup"], params=params)

        return data["result"]["result"]

    def export(self, path: str, password: str = None) -> dict:
        """
        Export sysPass data in XML  format
        :param path: path where store the xml in
        :param password: password used for encrypting the XML data (passwords are always encrypted)
        :return:
        """
        params = {
            "path": path,
            "password": password
        }

        data = self.api.call_api(method=METHODS["export"], params=params)

        return data["result"]["result"]

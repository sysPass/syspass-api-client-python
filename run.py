from syspass_api_client import account, category, client, tag, user_group
from syspass_api_client.api import JsonRpcApi

if __name__ == "__main__":
    api = JsonRpcApi()
    account = account.Account(api)
    category = category.Category(api)
    client = client.Client(api)
    tag = tag.Tag(api)
    user_group = user_group.UserGroup(api)

    for account_data in account.search():
        print(account_data)

    for category_data in category.search():
        print(category_data)

    for client_data in client.search():
        print(client_data)

    for tag_data in tag.search():
        print(tag_data)

    for user_group_data in user_group.search():
        print(user_group_data)

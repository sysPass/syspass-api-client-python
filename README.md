## sysPass API Client for Python

[![Build Status](https://travis-ci.org/sysPass/syspass-api-client-python.svg?branch=master)](https://travis-ci.org/sysPass/syspass-api-client-python)

This API client aims to be a core library for those projects based on Python.

It has all the methods currently implemented (as of sysPass v3.1) and can be easily extended to future extensions.

### Installation

```$ pipenv install syspass_api_client```

### Usage

The following environment variables could be used:

* SYSPASS_API_URL
* SYSPASS_API_TOKEN
* SYSPASS_API_TOKEN_PASS
* SYSPASS_TLS_VERIFY

```python
from syspass_api_client import api, account

o_api = api.JsonRpcApi()
o_account = account.Account(o_api)

for account_data in o_account.search():
    print(account_data)
```
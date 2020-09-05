# Arcapi

A third-party API for [ARC Prober](https://redive.estertion.win/arcaea/probe/) in Python.

Language: English/[中文](docs/README-CN.md)/[日本語](docs/README-JP.md)

## Quick Start

### Install

To use Arcapi, you can install it by [pypi](https://pypi.org/).
```shell script
$pip install Arc-api
```

### Usage
This api support synchronized and asynchronized methods to connect the websocket provide by Prober. To run in a synchronized way:

```python
from Arcapi import SyncApi

# Initialize an API with user code
api_ = SyncApi(user_code='000000000') 

# You can assign the constant range here, or just leave it in a default
print("userinfo: ", api_.userinfo(start=8, end=12)) 
```

Otherwise, you can run in an asynchronized way. If you deploy your service with a bot, I strongly recommend you to do in this way:

```python
import asyncio
from Arcapi import AsyncApi

# Initialize an API with user code
api_ = AsyncApi(user_code='000000000')

# You can assign the constant range here, or just leave it in a default
asyncio.get_event_loop().run_until_complete(api_.userinfo(start=8, end=12))
``` 

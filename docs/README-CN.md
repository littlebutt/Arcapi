# Arcapi

为 [ARC Prober](https://redive.estertion.win/arcaea/probe/) 搭建的第三方Python库。

语言: [English](../README.md)/中文/[日本語](./README-JP.md)

## 快速开始

### 安装

首先，你可以通过 [pypi](https://pypi.org/)安装本Python库
```shell script
$pip install Arc-api
```

### 使用方法
本API支持同步和异步连接ARC Prober，若需同步调用可以这样使用：

```python
from Arcapi import SyncApi

# Initialize an API with user code
api_ = SyncApi(user_code='000000000') 

# You can assign the constant range here, or just leave it in a default
print("userinfo: ", api_.userinfo(start=8, end=12)) 
```

或者，你可以这样调用异步方法。如果你需要安装在聊天机器人内，本教程强烈建议使用此方法： 

```python
import asyncio
from Arcapi import AsyncApi

# Initialize an API with user code
api_ = AsyncApi(user_code='000000000')

# You can assign the constant range here, or just leave it in a default
asyncio.get_event_loop().run_until_complete(api_.userinfo(start=8, end=12))
``` 
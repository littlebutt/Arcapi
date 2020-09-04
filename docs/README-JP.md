# Arcapi

これは[ARC Prober](https://redive.estertion.win/arcaea/probe/)のサードパーティーのPythonライブラリである。

語言: [English](../README.md)/[中文](./README-CN.md)/日本語

## スタート

### インストール

当該APIを使いのために、[pypi](https://pypi.org/)をご利用してインストールできます。
```shell script
$pip install Arcapi
```

### 使い方
本APIは非同期と同期両方をサポートしてます。まず、同期に実行させることは、このような書けます：
```python
from Arcapi import SyncApi

# Initialize an API with user code
api_ = SyncApi(user_code='000000000') 

# You can assign the constant range here, or just leave it in a default
print("userinfo: ", api_.userinfo(start=8, end=12)) 
```

一方、非同期させることもできます。MSNロボットを作るの場合は、この方法はおすすめです：

```python
import asyncio
from Arcapi import AsyncApi

# Initialize an API with user code
api_ = AsyncApi(user_code='000000000')

# You can assign the constant range here, or just leave it in a default
asyncio.get_event_loop().run_until_complete(api_.userinfo(start=8, end=12))
``` 
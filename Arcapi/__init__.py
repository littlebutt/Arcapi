from .async_api import AsyncApi
from .sync_api import SyncApi

__all__ = [
    'AsyncApi', 'SyncApi', 'Arcapi'
]


class Arcapi:
    _async_api: AsyncApi
    _sync_api: SyncApi

    def __init__(self, user_code: str):
        self._async_api = AsyncApi(user_code=user_code)
        self._sync_api = SyncApi(user_code=user_code)

    @property
    def asyncapi(self):
        return self._async_api

    @property
    def syncapi(self):
        return self._sync_api

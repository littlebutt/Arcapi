from Arcapi import Arcapi, AsyncApi, SyncApi
import asyncio


def test_async():
    api_ = AsyncApi('000000001')

    async def _():
        data = await api_.userinfo()
        print("user info :", data)
    asyncio.get_event_loop().run_until_complete(_())


def test_sync():
    api_ = SyncApi('000000002')
    print("constants :", api_.constants())



def test():
    api_ = Arcapi(user_code='000000001')
    _async = api_.asyncapi
    _sync = api_.syncapi


if __name__ == '__main__':
    test_async()
    test_sync()
    test()


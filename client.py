import httpx, aiohttp


async def test_httpx(api: str):
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            api,
            files={
                "file": (None, b"test", "text/plain"),
            }
        )
        print("-" * 20)
        print("httpx", resp)
        print("httpx", resp.json())
        print("-" * 20)


async def test_httpx_default(api: str):
    """httpx set default filename to 'upload'"""
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            api,
            files={
                "file": b"test",
            }
        )
        print("-" * 20)
        print("httpx_default", resp)
        print("httpx_default", resp.json())
        print("-" * 20)


async def test_aiohttp(api: str):
    async with aiohttp.ClientSession() as client:
        resp = await client.post(
            api,
            data={
                "file": (None, b"test", "text/plain"),
            }
        )
        print("-" * 20)
        print("aiohttp", resp)
        print("aiohttp", await resp.json())
        print("-" * 20)


async def test_aiohttp_default(api: str):
    """aiohttp set default filename to 'file' ({key: file}, default filename = key)"""
    async with aiohttp.ClientSession() as client:
        resp = await client.post(
            api,
            data={
                "file": b"test",
            }
        )
        print("-" * 20)
        print("aiohttp_default", resp)
        print("aiohttp_default", await resp.json())
        print("-" * 20)


if __name__ == '__main__':
    from asyncio import run

    _api = "http://127.0.0.1:8000/uploadfile"
    run(test_httpx(_api))
    run(test_httpx_default(_api))
    run(test_aiohttp(_api))
    run(test_aiohttp_default(_api))

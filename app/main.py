import asyncio
import os
from typing import Awaitable, Callable, Coroutine, Optional

Server = Callable[
    [list[asyncio.Server]],
    Callable[[asyncio.StreamReader, asyncio.StreamWriter], Awaitable[None]],
]


async def mkserver(port: int, callback: Server) -> None:
    global _server
    server = list[asyncio.Server]()
    server.append(await asyncio.start_server(callback(server), "127.0.0.1", port))

    try:
        async with server[0]:
            await server[0].serve_forever()
    except asyncio.CancelledError:
        pass


def test(
    client: Callable[[], Callable[[int, float], Coroutine[None, None, bool]]],
    server: Callable[[], Server],
) -> None:
    print(f"Testing {client.__name__} <=> {server.__name__}")
    print("=" * 100, flush=True)

    if pid1 := os.fork():
        if pid2 := os.fork():
            # I'm the parent of two children
            os.waitpid(pid1, 0)
            os.waitpid(pid2, 0)
        else:
            result = asyncio.run(client()(9999, 1))
            print("=" * 100)
            print(f"Roundtrip equality: {result}", end="\n\n\n")
            exit()
    else:
        asyncio.run(mkserver(9999, server()))
        exit()


def v1_client():
    from . import v1

    return v1.v1_client


def v2_client():
    from . import v2

    return v2.v2_client


def v1_server():
    from . import v1

    return v1.v1_server


def v2_server():
    from . import v2

    return v2.v2_server


test(v1_client, v2_server)
test(v2_client, v1_server)

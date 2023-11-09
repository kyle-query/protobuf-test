import asyncio

from proto.output.v1 import example_v1_pb2 as v1


def v1_copy_exs(val: v1.Examples) -> v1.Examples:
    send = v1.Examples()
    if val.HasField("count"):
        send.count = val.count
    for ex in val.items:
        send.items.append(v1_copy_ex(ex))
    return send


def v1_copy_ex(val: v1.Example) -> v1.Example:
    send = v1.Example()
    if val.HasField("a"):
        send.a = val.a
    if val.HasField("b"):
        send.b = val.b
    if val.HasField("d"):
        send.d = val.d
    if val.HasField("e"):
        send.e = val.e
    if val.HasField("option"):
        send.option = val.option
    return send


def v1_print_exs(val: v1.Examples) -> str:
    items = ",\n    ".join(v1_print_ex(ex) for ex in val.items)
    return f"v1.Examples(count={val.count!r}, items=[\n    {items}])"


def v1_print_ex(val: v1.Example) -> str:
    return f"v1.Example(a={val.a!r}, b={val.b!r}, d={val.d!r}, e={val.e!r}, option={val.option!r})"


def v1_server(server: list[asyncio.Server]):
    async def worker(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        recv = v1.Examples()
        recv.ParseFromString(await reader.read(1024**3))
        print(f"server_v1 recv: {v1_print_exs(recv)}", end="\n\n", flush=True)

        writer.write(v1_copy_exs(recv).SerializeToString())
        await writer.drain()

        assert server
        server[0].close()
        await server[0].wait_closed()

    return worker


async def v1_client(port: int, wait: float) -> bool:
    await asyncio.sleep(wait)

    reader, writer = await asyncio.open_connection("127.0.0.1", port)

    send = v1.Examples(
        count=100,
        items=[
            v1.Example(a="hello", b=111, d=911.9, option=v1.A),
            v1.Example(a="hello", b=222, e=228.8, option=v1.B),
            v1.Example(a="hello", b=300, d=933.9, option=v1.C),
        ],
    )

    print(f"client_v1 send: {v1_print_exs(send)}", end="\n\n", flush=True)
    writer.write(send.SerializeToString())
    await writer.drain()

    recv = v1.Examples()
    recv.ParseFromString(await reader.read(1024**3))
    print(f"client_v1 recv: {v1_print_exs(recv)}", flush=True)

    return recv == send

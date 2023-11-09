import asyncio

from proto.output.v2 import example_v2_pb2 as v2


def v2_copy_exs(recv: v2.Examples) -> v2.Examples:
    send = v2.Examples()
    if recv.HasField("count_old"):
        send.count_old = recv.count_old
    if recv.HasField("count_new"):
        send.count_new = recv.count_new
    for ex in recv.items:
        send.items.append(v2_copy_ex(ex))
    return send


def v2_copy_ex(recv: v2.Example) -> v2.Example:
    send = v2.Example()
    if recv.HasField("a_old"):
        send.a_old = recv.a_old
    if recv.HasField("b"):
        send.b = recv.b
    if recv.HasField("c_new"):
        send.c_new = recv.c_new
    if recv.HasField("d"):
        send.d = recv.d
    if recv.HasField("e"):
        send.e = recv.e
    if recv.HasField("f_new"):
        send.f_new = recv.f_new
    if recv.HasField("option"):
        send.option = recv.option
    return send


def v2_print_exs(val: v2.Examples) -> str:
    items = ",\n    ".join(v2_print_ex(ex) for ex in val.items)
    return f"v2.Examples(count_old={val.count_old!r}, count_new={val.count_new!r}, items=[\n    {items}])"


def v2_print_ex(val: v2.Example) -> str:
    return f"v2.Example(a_old={val.a_old!r}, b={val.b!r}, c_new={val.c_new!r}, d={val.d!r}, e={val.e!r}, f_new={val.f_new!r}, option={val.option!r})"


def v2_server(server: list[asyncio.Server]):
    async def worker(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        recv = v2.Examples()
        recv.ParseFromString(await reader.read(1024**3))
        print(f"server_v2 recv: {v2_print_exs(recv)}", end="\n\n", flush=True)

        writer.write(v2_copy_exs(recv).SerializeToString())
        await writer.drain()

        assert server
        server[0].close()
        await server[0].wait_closed()

    return worker


async def v2_client(port: int, wait: float) -> bool:
    await asyncio.sleep(wait)

    reader, writer = await asyncio.open_connection("127.0.0.1", port)

    send = v2.Examples(
        count_old=100,
        count_new=3295,
        items=[
            v2.Example(a_old="hello", b=111, c_new="abc", d=999.9, option=v2.Example.B),
            v2.Example(
                a_old="hello", b=220, c_new="defff", e=7.888, option=v2.Example.C
            ),
            v2.Example(
                a_old="hello",
                b=300,
                c_new="ghi",
                f_new=33339.9,
                option=v2.Example.D_NEW,
            ),
        ],
    )

    print(f"client_v2 send: {v2_print_exs(send)}", end="\n\n", flush=True)
    writer.write(send.SerializeToString())
    await writer.drain()

    recv = v2.Examples()
    recv.ParseFromString(await reader.read(1024**3))
    print(f"client_v2 recv: {v2_print_exs(recv)}", flush=True)

    return recv == send

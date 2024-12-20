This project demonstrates Protobuf backward compatibility. You can run the demo like this:

```sh
$ asdf install
$ poetry run python -m app.main
```

The output should look like:

```
» poetry run python -m app.main
Testing v1_client <=> v2_server
====================================================================================================
client_v1 send: v1.Examples(count=100, items=[
    v1.Example(a='hello', b=111, d=911.9, e=0.0, option=1),
    v1.Example(a='hello', b=222, d=0.0, e=228.8, option=2),
    v1.Example(a='hello', b=300, d=933.9, e=0.0, option=3)])

server_v2 recv: v2.Examples(count_old=100, count_new=9999999, items=[
    v2.Example(a_old='hello', b=111, c_new='', d=911.9, e=0.0, f_new=0.0, option=1),
    v2.Example(a_old='hello', b=222, c_new='', d=0.0, e=228.8, f_new=0.0, option=2),
    v2.Example(a_old='hello', b=300, c_new='', d=933.9, e=0.0, f_new=0.0, option=3)])

client_v1 recv: v1.Examples(count=100, items=[
    v1.Example(a='hello', b=111, d=911.9, e=0.0, option=1),
    v1.Example(a='hello', b=222, d=0.0, e=228.8, option=2),
    v1.Example(a='hello', b=300, d=933.9, e=0.0, option=3)])
====================================================================================================
Roundtrip equality: True


Testing v2_client <=> v1_server
====================================================================================================
client_v2 send: v2.Examples(count_old=100, count_new=3295, items=[
    v2.Example(a_old='hello', b=111, c_new='abc', d=999.9, e=0.0, f_new=0.0, option=2),
    v2.Example(a_old='hello', b=220, c_new='defff', d=0.0, e=7.888, f_new=0.0, option=3),
    v2.Example(a_old='hello', b=300, c_new='ghi', d=0.0, e=0.0, f_new=33339.9, option=4)])

server_v1 recv: v1.Examples(count=100, items=[
    v1.Example(a='hello', b=111, d=999.9, e=0.0, option=2),
    v1.Example(a='hello', b=220, d=0.0, e=7.888, option=3),
    v1.Example(a='hello', b=300, d=0.0, e=0.0, option=1)])

client_v2 recv: v2.Examples(count_old=100, count_new=9999999, items=[
    v2.Example(a_old='hello', b=111, c_new='', d=999.9, e=0.0, f_new=0.0, option=2),
    v2.Example(a_old='hello', b=220, c_new='', d=0.0, e=7.888, f_new=0.0, option=3),
    v2.Example(a_old='hello', b=300, c_new='', d=0.0, e=0.0, f_new=0.0, option=1)])
====================================================================================================
Roundtrip equality: False
```

This uses two versions of a protobuf spec: v1, which is the older version, and v2 which has additive
changes. The demo simulates these conditions:

* The client sends a message using v1 definitions. The server interprets it using the v2
    definitions. The server responds with the same message using v2 definitions and the client
    interprets it using the v1 definitions.

* The client sends a message using v2 definitions. The server interprets it using the v1
    definitions. The server responds with the same message using v1 definitions and the client
    interprets it using the v2 definitions.

In both cases the client compares the message it sent to the message it received.

In the first case, the server reads default values for all the new fields which weren't present on
the wire from the v1 message. When it sends a v2 message back over the wire, the client is unaware
of the new elements from v2.

In the second case, the server is unaware of the new elements from v2 which were present on the
wire. The server responds with a v1 message that contains only fields they have in common. When the
client reads the v1 message on the wire using v2 definitions, the new elements have default values.

### Field Presence

Protobuf does not have a `null` value. This means all fields have a non-`null` value. However, it
does *not* mean all fields must be set. We can use this fact to encode `null` as a field which isn't
set.

However, this also means we cannot distinguish if a field was explicitly set to `null` or if it
simply wasn't set at all, because both cases result in the same binary message. When a client reads
a field which wasn't set (or was set to `null`), it will read the default value declared by the
client's protobuf definitions.

We can check whether a field is present on the wire or not using the `HasField` method. With this we
can tell if we are reading a default value because the field wasn't sent, or because the sender sent
a value that happened to be the default.

We cannot track field presence on repeated elements and maps (dictionaries). This means `HasField`
can't be used to distinguish an empty list from a list field that wasn't set.

You can read more about field presence [here](https://protobuf.dev/programming-guides/field_presence/)

### Default Values

We can specify default values in `.proto` files like this `optional integer foo = 1; [default =
10]`. If the field is not set by client code, it will also not be written on the wire. When it's
read from the wire, the definitions used by the reader will specify the default value that will be
read. To restate this, the default values are not used by writers.

In our protobuf encoder and decoder functions, we copy fields from a domain object to a Protobuf
object and vice-versa. Here is an example:

```python
# Domain object
from dataclasses import dataclass
from typing import Optional
from queryai_ocsf.data.json import JsonVal
from queryai_ocsf.codec.helper import decode_pb_jsonval, encode_pb_jsonval
from queryai_ocsf.google.objects.object_pb2 import Object as pb_Object


@dataclass
class dc_Object:
    """..."""

    raw_data: Optional[JsonVal] = None
    """Raw Data: The event data as received from the event source."""

    record_id: Optional[str] = None
    """Record ID: Unique idenifier for the object"""

# This file was generated by queryai_ocsf_codegen/main.py, at line 187
from typing import Optional


def encode_pb_object(src: dc_Object, dst: Optional[pb_Object] = None) -> pb_Object:
    if dst is None:
        dst = pb_Object()
    if src.raw_data is not None:
        dst.raw_data.CopyFrom(encode_pb_jsonval(src.raw_data))
    if src.record_id is not None:
        dst.record_id = src.record_id
    return dst


def decode_pb_object(src: pb_Object, dst: Optional[dc_Object] = None) -> dc_Object:
    if dst is None:
        dst = dc_Object()
    if src.HasField("raw_data"):
        dst.raw_data = decode_pb_jsonval(src.raw_data)
    if src.HasField("record_id"):
        dst.record_id = src.record_id
    return dst
```

Default values declared by protobuf specificaitons are not used by the reader or writer. We're using
protobuf v2, but note that v3 removes the ability to set default values anyway.

The reader first checks presence using `HasField`. If the field is not present, the default
value declared in the Python domain object (`dc_Object`) remains. Without the `HasField` check, we
could not communicate `None` values because `dst.record_id = src.record_id` would implicitly read
the non-`None` default value declared by the protobuf specification.

## Read more

You can read about recommended practices [here](https://protobuf.dev/programming-guides/dos-donts/)

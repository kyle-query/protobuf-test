from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

A: Option
B: Option
C: Option
DESCRIPTOR: _descriptor.FileDescriptor

class Example(_message.Message):
    __slots__ = ["a", "b", "d", "e", "option"]
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    D_FIELD_NUMBER: _ClassVar[int]
    E_FIELD_NUMBER: _ClassVar[int]
    OPTION_FIELD_NUMBER: _ClassVar[int]
    a: str
    b: int
    d: float
    e: float
    option: Option
    def __init__(self, a: _Optional[str] = ..., b: _Optional[int] = ..., d: _Optional[float] = ..., e: _Optional[float] = ..., option: _Optional[_Union[Option, str]] = ...) -> None: ...

class Examples(_message.Message):
    __slots__ = ["count", "items"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    count: int
    items: _containers.RepeatedCompositeFieldContainer[Example]
    def __init__(self, count: _Optional[int] = ..., items: _Optional[_Iterable[_Union[Example, _Mapping]]] = ...) -> None: ...

class Option(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

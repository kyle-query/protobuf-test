from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Example(_message.Message):
    __slots__ = ["a_old", "b", "c_new", "d", "e", "f_new", "option"]
    class Option(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    A: Example.Option
    A_OLD_FIELD_NUMBER: _ClassVar[int]
    B: Example.Option
    B_FIELD_NUMBER: _ClassVar[int]
    C: Example.Option
    C_NEW_FIELD_NUMBER: _ClassVar[int]
    D_FIELD_NUMBER: _ClassVar[int]
    D_NEW: Example.Option
    E_FIELD_NUMBER: _ClassVar[int]
    F_NEW_FIELD_NUMBER: _ClassVar[int]
    OPTION_FIELD_NUMBER: _ClassVar[int]
    a_old: str
    b: int
    c_new: str
    d: float
    e: float
    f_new: float
    option: Example.Option
    def __init__(self, a_old: _Optional[str] = ..., b: _Optional[int] = ..., c_new: _Optional[str] = ..., d: _Optional[float] = ..., e: _Optional[float] = ..., f_new: _Optional[float] = ..., option: _Optional[_Union[Example.Option, str]] = ...) -> None: ...

class Examples(_message.Message):
    __slots__ = ["count_new", "count_old", "items"]
    COUNT_NEW_FIELD_NUMBER: _ClassVar[int]
    COUNT_OLD_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    count_new: int
    count_old: int
    items: _containers.RepeatedCompositeFieldContainer[Example]
    def __init__(self, count_old: _Optional[int] = ..., count_new: _Optional[int] = ..., items: _Optional[_Iterable[_Union[Example, _Mapping]]] = ...) -> None: ...

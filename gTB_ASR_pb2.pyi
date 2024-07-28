from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FilenameRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ASRReply(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class WavRequest(_message.Message):
    __slots__ = ("wav",)
    WAV_FIELD_NUMBER: _ClassVar[int]
    wav: bytes
    def __init__(self, wav: _Optional[bytes] = ...) -> None: ...

class AgentsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentsReply(_message.Message):
    __slots__ = ("agents",)
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    agents: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, agents: _Optional[_Iterable[str]] = ...) -> None: ...

class AddAgentRequest(_message.Message):
    __slots__ = ("agent_ip",)
    AGENT_IP_FIELD_NUMBER: _ClassVar[int]
    agent_ip: str
    def __init__(self, agent_ip: _Optional[str] = ...) -> None: ...

class AddAgentReply(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: bool = ...) -> None: ...

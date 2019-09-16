from enum import Enum

from thriftpy2.protocol import TBinaryProtocol
from typing import List
from typing import Optional


CLIENT_ADDR: str
SERVER_ADDR: str


class Endpoint(object):
    ipv4: int
    port: int
    service_name: str
    ipv6: Optional[bytes]


class Annotation(object):
    timestamp: int
    value: str
    host: Endpoint


class AnnotationType(Enum):
    BOOL=0
    BYTES=1
    I16=2
    I32=3
    I64=4
    DOUBLE=5
    STRING=6


class BinaryAnnotation(object):
    key: str
    value: bytes
    annotation_type: AnnotationType
    host: Endpoint


class Span(object):
    trace_id: int
    name: str
    id: int
    parent_id: Optional[int]
    annotations: List[Annotation]
    binary_annotations: List[BinaryAnnotation]
    debug: Optional[bool]
    timestamp: Optional[int]
    duration: Optional[int]
    trace_id_high: Optional[int]

    def read(self, protocol): # type: (TBinaryProtocol) -> None
        pass

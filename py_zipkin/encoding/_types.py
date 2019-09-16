# -*- coding: utf-8 -*-
from enum import Enum
from typing import Dict


class Encoding(Enum):
    """Supported output encodings."""
    V1_THRIFT = 'V1_THRIFT'
    V1_JSON = 'V1_JSON'
    V2_JSON = 'V2_JSON'
    V2_PROTO3 = 'V2_PROTO3'


class Kind(Enum):
    """Type of Span."""
    CLIENT = 'CLIENT'
    SERVER = 'SERVER'
    PRODUCER = 'PRODUCER'
    CONSUMER = 'CONSUMER'
    LOCAL = None


# Convenience typedefs for tags and annotations
Tags = Dict[str, str]
Annotations = Dict[str, float]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time

import mock
import pytest
import requests

from py_zipkin import Encoding
from py_zipkin import Kind
from py_zipkin import zipkin
from py_zipkin.storage import get_default_tracer
from py_zipkin.transport.http import HTTPTransportHandler
from py_zipkin.util import generate_random_64bit_string
from py_zipkin.zipkin import ZipkinAttrs


def us(seconds):
    return int(seconds * 1000 * 1000)


@pytest.mark.parametrize('encoding', [
    Encoding.V1_THRIFT,
    Encoding.V1_JSON,
    Encoding.V2_JSON,
    Encoding.V2_PROTO3,
])
def test_encoding(encoding):
    zipkin_attrs = ZipkinAttrs(
        trace_id=generate_random_64bit_string(),
        span_id=generate_random_64bit_string(),
        parent_span_id=generate_random_64bit_string(),
        is_sampled=True,
        flags=None,
    )
    inner_span_id = generate_random_64bit_string()
    transport_handler = HTTPTransportHandler(encoding)
    ts = round(time.time(), 3)
    tracer = get_default_tracer()

    with tracer.zipkin_span(
        service_name='test_service_name',
        span_name='test_span_name',
        transport_handler=transport_handler,
        binary_annotations={'some_key': 'some_value'},
        encoding=encoding,
        zipkin_attrs=zipkin_attrs,
        host='10.0.0.0',
        port=8080,
        kind=Kind.CLIENT,
    ) as span:
        with mock.patch.object(
            zipkin,
            'generate_random_64bit_string',
            return_value=inner_span_id,
        ):
            with tracer.zipkin_span(
                service_name='test_service_name',
                span_name='inner_span',
                timestamp=ts,
                duration=5,
                annotations={'ws': ts},
            ):
                span.add_sa_binary_annotation(
                    8888,
                    'sa_service',
                    '2001:0db8:85a3:0000:0000:8a2e:0370:7334',
                )

    resp = requests.get('http://127.0.0.1:9411/api/v2/trace/{}'.format(
        zipkin_attrs.trace_id,
    ))
    assert resp.status_code == 200

    output = resp.json()
    assert len(output) == 2

    inner_span, root_span = output

    assert root_span == {
        'traceId': zipkin_attrs.trace_id,
        'name': 'test_span_name',
        'parentId': zipkin_attrs.parent_span_id,
        'id': zipkin_attrs.span_id,
        'kind': 'CLIENT',
        'timestamp': mock.ANY,
        'duration': mock.ANY,
        'localEndpoint': {
            'ipv4': '10.0.0.0',
            'port': 8080,
            'serviceName': 'test_service_name',
        },
        'remoteEndpoint': {
            'ipv6': '2001:db8:85a3::8a2e:370:7334',
            'port': 8888,
            'serviceName': 'sa_service',
        },
        'tags': {'some_key': 'some_value'},
    }

    assert inner_span == {
        'traceId': zipkin_attrs.trace_id,
        'name': 'inner_span',
        'parentId': zipkin_attrs.span_id,
        'id': inner_span_id,
        'timestamp': us(ts),
        'duration': us(5),
        'localEndpoint': {
            'ipv4': '10.0.0.0',
            'port': 8080,
            'serviceName': 'test_service_name',
        },
        'annotations': [{'timestamp': us(ts), 'value': 'ws'}],
    }


@pytest.mark.parametrize('encoding', [
    Encoding.V1_THRIFT,
    Encoding.V1_JSON,
    Encoding.V2_JSON,
    Encoding.V2_PROTO3,
])
def test_encoding_server_span(encoding):
    zipkin_attrs = ZipkinAttrs(
        trace_id=generate_random_64bit_string(),
        span_id=generate_random_64bit_string(),
        parent_span_id=generate_random_64bit_string(),
        is_sampled=True,
        flags=None,
    )
    transport_handler = HTTPTransportHandler(encoding)
    tracer = get_default_tracer()

    with tracer.zipkin_span(
        service_name='test_service_name',
        span_name='test_span_name',
        transport_handler=transport_handler,
        binary_annotations={'some_key': 'some_value'},
        encoding=encoding,
        zipkin_attrs=zipkin_attrs,
        host='10.0.0.0',
        port=8080,
        kind=Kind.SERVER,
    ):
        pass

    resp = requests.get('http://127.0.0.1:9411/api/v2/trace/{}'.format(
        zipkin_attrs.trace_id,
    ))
    assert resp.status_code == 200

    output = resp.json()
    assert len(output) == 1

    assert output[0] == {
        'traceId': zipkin_attrs.trace_id,
        'name': 'test_span_name',
        'parentId': zipkin_attrs.parent_span_id,
        'id': zipkin_attrs.span_id,
        'kind': 'SERVER',
        'timestamp': mock.ANY,
        'duration': mock.ANY,
        'shared': True,
        'localEndpoint': {
            'ipv4': '10.0.0.0',
            'port': 8080,
            'serviceName': 'test_service_name',
        },
        'tags': {'some_key': 'some_value'},
    }

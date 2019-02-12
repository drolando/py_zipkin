import json
import time

import pytest

from py_zipkin import Tracer
from py_zipkin.encoding import Encoding
from py_zipkin.encoding._encoders import get_encoder
from tests.test_helpers import MockTransportHandler

ITER = 10000


def test_zipkin_span_not_traced():
    tracer = Tracer()

    start = time.time()
    for _ in range(ITER):
        with tracer.zipkin_span(
            service_name='foo',
            span_name='bar',
        ):
            pass

    end = time.time()
    print(end - start)
    print('{}us'.format(round((end - start) / ITER * 1000 * 1000, 2)))
    assert False


def test_zipkin_span_traced():
    tracer = Tracer()
    transport = MockTransportHandler()

    with tracer.zipkin_span(
        service_name='foo',
        span_name='bar',
        sample_rate=100.0,
        transport_handler=transport,
        encoding=Encoding.V2_JSON,
    ):
        start = time.time()
        for _ in range(ITER):
            with tracer.zipkin_span(
                service_name='foo',
                span_name='bar',
            ):
                pass

        end = time.time()
    print(end - start)
    print('{}us'.format(round((end - start) / ITER * 1000 * 1000, 2)))
    assert len(transport.get_payloads()) == 101
    assert len(json.loads(transport.get_payloads()[0])) == 100
    assert False


def test_zipkin_span_traced_not_sampled():
    tracer = Tracer()
    transport = MockTransportHandler()

    with tracer.zipkin_span(
        service_name='foo',
        span_name='bar',
        sample_rate=0.0,
        transport_handler=transport,
        encoding=Encoding.V2_JSON,
    ):
        start = time.time()
        for _ in range(ITER):
            with tracer.zipkin_span(
                service_name='foo',
                span_name='bar',
            ):
                pass

        end = time.time()
    print(end - start)
    print('{}us'.format(round((end - start) / ITER * 1000 * 1000, 2)))
    assert len(transport.get_payloads()) == 0
    assert False


@pytest.mark.parametrize(['encoding', 'exp_time'], [
    (Encoding.V1_THRIFT, 110.0),
    (Encoding.V1_JSON, 22.0),
    (Encoding.V2_JSON, 8.0),
])
def test_zipkin_encoding(encoding, exp_time):
    tracer = Tracer()
    transport = MockTransportHandler()

    with tracer.zipkin_span(
        service_name='foo',
        span_name='bar',
        sample_rate=100.0,
        transport_handler=transport,
        encoding=encoding,
    ):
        for _ in range(ITER):
            with tracer.zipkin_span(
                service_name='foo',
                span_name='bar',
            ):
                pass
        spans = list(tracer.get_spans())

    encoder = get_encoder(encoding)
    # spans = tracer.get_spans()
    assert len(spans) == ITER
    enc_spans = []

    start = time.time()
    for span in spans:
        enc_spans.append(encoder.encode_span(span))
    encoder.encode_queue(enc_spans)
    end = time.time()

    duration = end - start
    per_span = round(duration / ITER * 1000 * 1000, 1)
    # assert len(output) == 101
    assert abs(per_span - exp_time) / exp_time < 0.1

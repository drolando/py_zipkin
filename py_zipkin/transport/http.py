import logging

import six
from six.moves import urllib

from py_zipkin.encoding import Encoding
from py_zipkin.transport.base import BaseTransportHandler

log = logging.getLogger(__file__)


class HTTPTransportHandler(BaseTransportHandler):

    def __init__(self, encoding):
        super(HTTPTransportHandler, self).__init__()
        if encoding == Encoding.V1_THRIFT:
            self.url = 'http://127.0.0.1:9411/api/v1/spans'
            self.content_type = 'application/x-thrift'
        elif encoding == Encoding.V1_JSON:
            self.url = 'http://127.0.0.1:9411/api/v1/spans'
            self.content_type = 'application/json'
        elif encoding == Encoding.V2_JSON:
            self.url = 'http://127.0.0.1:9411/api/v2/spans'
            self.content_type = 'application/json'
        elif encoding == Encoding.V2_PROTO3:
            self.url = 'http://127.0.0.1:9411/api/v2/spans'
            self.content_type = 'application/x-protobuf'

    def send(self, payload):
        # In case payload is sent in as non-bytearray format,
        # safeguard convert to bytearray before handling
        if isinstance(payload, six.string_types):
            # Even six.b is not enough to handle the py2/3 difference since
            # it uses latin-1 as default encoding and not utf-8.
            if six.PY2:
                payload = six.b(payload)  # pragma: no cover
            else:
                payload = payload.encode('utf-8')  # pragma: no cover

        headers = {'Content-Type': self.content_type}
        request = urllib.request.Request(self.url, payload, headers)
        try:
            urllib.request.urlopen(request)
        except urllib.error.HTTPError as e:
            log.error('Failed to send trace to zipkin. Error: {} - {}'.format(
                repr(e),
                e.read(),
            ))

    def get_max_payload_bytes(self):
        return None

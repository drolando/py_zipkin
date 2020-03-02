Transports
==========

Zipkin supports multiple transport options, the most common being HTTP, Kafka and
RabbitMQ. All of them accept both V1 and V2 spans, with both thrift, json and
protobuf encoding.

py_zipkin has a pluggable transport layer, which allows you to use your own
transport implementation. py_zipkin provides some examples, however they're not
production ready so you're advised to write your own.

HTTP transport example
~~~~~~~~~~~~~~~~~~~~~~

The simplest way to get spans to the collector is via HTTP POST.
py_zipkin includes a simple HTTP transport that you can use for testing or when
trying out zipkin. However it's not production ready, so we suggest you to write
your own transport.

.. autoclass:: py_zipkin.transport.SimpleHTTPTransport

Implement a new transport
-------------------------

The recommended way to implement a new transport handler is to subclass
`BaseTransportHandler <#py_zipkin.transport.BaseTransportHandler>`_ and implement
the `send` and `get_max_payload_bytes` methods.

`send` receives an already encoded span list as bytearray. You can send this this
list directly to Zipkin, write it to Kafka or use your preferred transport. It's
already properly encoded, so any Zipkin collector will accept it as-is.

`get_max_payload_bytes` should return the maximum payload size supported by your
transport, or `None` if you can send arbitrarily big messages. Most transport will
have a maximum payload size, for example by default Kafka will reject messages
bigger than 1MB.

.. note::
    Older versions of py_zipkin suggested implementing the transport handler as a
    function with a single argument. That should still work with the current
    py_zipkin version, but it's deprecated and will be removed in 1.0.

.. autoclass:: py_zipkin.transport.BaseTransportHandler
   :members:

Kafka transport example
~~~~~~~~~~~~~~~~~~~~~~~

If you have the ability to send spans over Kafka (more like what you might do in
production), you'd do something like the following, using the kafka-python package:

.. code-block:: python

   from kafka import SimpleProducer, KafkaClient

   from py_zipkin.transport import BaseTransportHandler


   class KafkaTransport(BaseTransportHandler):

      def get_max_payload_bytes(self):
         # By default Kafka rejects messages bigger than 1000012 bytes.
         return 1000012

      def send(self, message):
         kafka_client = KafkaClient('{}:{}'.format('localhost', 9092))
         producer = SimpleProducer(kafka_client)
         producer.send_messages('kafka_topic_name', message)

Sampling and firehose mode
--------------------------

py_zipkin accepts up to two transport handlers: `transport_handler` and
`firehose_handler`.

`transport_handler`'s `send` function will only be called if the current trace is
being sampled and you actually need to send those spans. If the trace is not
sampled it won't be called at all. So there's no need for you to implement any
sampling in the transport.

If defined, `firehose_handler` instead will be called for every trace, even if it's
not sampled. Having 2 different transports for firehose mode and "sampled" mode
allows you to send the 2 kinds of traces to different clusters and even to use a
different transport mechanism for each if you want.

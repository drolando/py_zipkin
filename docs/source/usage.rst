How to use py_zipkin
====================

test test tes

Start a trace with a given sampling rate
----------------------------------------

This example shows how to start a new trace. We pass in a ``sample_rate`` but no
existing zipkin ids, so py_zipkin will assume this is the beginning of a new trace and
generate new random ids.

Since this is our root context manager, the other required argument is the
``transport_handler`` which will take care of emitting the generated spans to the zipkin
backend.

Passing an explicit ``encoding`` is optional, but if you want to use a different
encoding than the default (``V1 thrift`` at the moment) you can specify it here.

.. code-block:: python

    from py_zipkin import zipkin_span
    from py_zipkin import Encoding
    from py_zipkin import Kind

    # Start a trace
    def my_batch_job(*argv, **kwargs):
        with zipkin_span(
            service_name='my_service',
            span_name='my_batch_job',
            transport_handler=SimpleHTTPTransport("localhost", 9411),
            sample_rate=100.0,
            encoding=Encoding.V2_JSON,
        ):
            do_stuff()


Continue an existing trace started by another service
-----------------------------------------------------

This example shows what you'd typically do when instrumenting a framework like Pyramid
or Django. The incoming request headers carry the zipkin ids for the current trace, so
instead of generating new random ones we want to reuse those.

``extract_zipkin_attrs_from_headers`` will extract the ids from the headers and return
them as ZipkinAttrs. If the incoming headers did not contain zipkin ids it'll simply
generate new ones.

The ``sample_rate`` is used in case the incoming X-B3-Sampled header is set to 0
(trace is not being sampled). If sample_rate is set to a value greater than 0, we'll
re-roll the dice and take again a decision on whether to sample the trace from now on.

.. note::
    py_zipkin will never stop sampling a trace, so if the incoming X-B3-Sampled header
    is set to 1, sample_rate is ignored.

.. note::
    You generally don't want every service in your chain to decide yet again whether to
    sample a trace of not. That leads to a lot of incomplete traces being saved, as
    only the services after the current one will emit spans but not the ones before.

    What works best is to set ``sample_rate`` only in the services at the edge of your
    infrastructure (the first ones to be hit by a user request) and leave all the other
    services with a rate of 0.

.. code-block:: python

    from py_zipkin import zipkin_span
    from py_zipkin import Encoding
    from py_zipkin import Kind
    from py_zipkin.request_helpers import extract_zipkin_attrs_from_headers

    # Start a trace
    def handle_request(request):
        zipkin_attrs = extract_zipkin_attrs_from_headers(
            headers=request.headers,
            sample_rate=1.0,
        )
        with zipkin_span(
            service_name='my_service',
            span_name='GET',
            transport_handler=SimpleHTTPTransport("localhost", 9411),
            zipkin_attrs=zipkin_attrs,
            encoding=Encoding.V2_JSON,
            kind=Kind.SERVER,
        ):
            do_stuff()

.. autofunction:: py_zipkin.request_helpers.extract_zipkin_attrs_from_headers

Log a span within the context of a zipkin trace
-----------------------------------------------

If you're already in a zipkin trace, you can use this to log a span inside. The
only required param is service_name. If you're not in a zipkin trace (e.g. you forgot
to add a root context), this won't do anything to prevent memory leaks.

.. code-block:: python

   # As a decorator
   @zipkin_span(service_name='my_service', span_name='my_function')
   def my_function():
      do_stuff()

.. code-block:: python

   # As a context manager
   def my_function():
      with zipkin_span(service_name='my_service', span_name='do_stuff'):
         do_stuff()



Trace a service call
--------------------

Client side
~~~~~~~~~~~

.. code-block:: python

    from py_zipkin.request_helpers import create_http_headers
    from py_zipkin.zipkin import zipkin_client_span

    def make_request(url, headers):
        with zipkin_client_span('my_service', 'GET'):
            headers.update(create_http_headers())
            return requests.get(url, headers=headers)

.. autofunction:: py_zipkin.request_helpers.create_http_headers

.. autoclass:: py_zipkin.zipkin.zipkin_span

.. autoclass:: py_zipkin.Kind

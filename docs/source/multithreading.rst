Multithreading
==============

py_zipkin stores its tracer object and context stack in a thread-local variable.
If your project makes use of multithreading, the code running in the new thread
won't have access to the Tracer created in the original thread and so will be
unable to emit spans.

Threading autoinstrumentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you use ``threading.Thread`` to create and run your threads, then py_zipkin provides
an helper to automatically propagate the trace context to the new Threads.

.. code-block:: python

    from py_zipkin.instrumentations import python_threads

    # Call this before creating or starting any thread
    python_threads.patch_threading()

Manual propagation
~~~~~~~~~~~~~~~~~~

If you use another library to create new threads, you'll have to propagate the tracer
manually.

.. code-block:: python

    from py_zipkin.storage import get_default_tracer
    from py_zipkin.storage import set_default_tracer

    # Before launching the new thread / greenlet get a copy of the current Tracer
    tracer = get_default_tracer().copy()

    # Pass `tracer` as argument to whatever function you're going to run in the new
    # thread / greenlet and as first thing set it as current tracer.
    def my_async_fn(tracer, *argv, **kwargs):
        set_default_tracer(tracer)
        # Do stuff

    gevent.spawn(my_async_fn, tracer)

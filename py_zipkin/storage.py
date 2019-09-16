# -*- coding: utf-8 -*-
import logging
import threading
from collections import deque
from collections import namedtuple

from typing import List
from typing import Optional
from typing import TypeVar

import py_zipkin
from py_zipkin.encoding._helpers import Span

try:  # pragma: no cover
    # Since python 3.7 threadlocal is deprecated in favor of contextvars
    # which also work in asyncio.
    import contextvars
    _contextvars_tracer = contextvars.ContextVar('py_zipkin.Tracer object')
except ImportError:  # pragma: no cover
    # The contextvars module was added in python 3.7
    _contextvars_tracer = None
_thread_local_tracer = threading.local()

"""
Holds the basic attributes needed to log a zipkin trace

:param trace_id: Unique trace id
:param span_id: Span Id of the current request span
:param parent_span_id: Parent span Id of the current request span
:param flags: stores flags header. Currently unused
:param is_sampled: pre-computed boolean whether the trace should be logged
"""
ZipkinAttrs = namedtuple(
    'ZipkinAttrs',
    ['trace_id', 'span_id', 'parent_span_id', 'flags', 'is_sampled'],
)


log = logging.getLogger('py_zipkin.storage')


ZST = TypeVar('ZST', bound=py_zipkin.zipkin.zipkin_span)


def _get_thread_local_tracer():  # type: () -> Tracer
    """Returns the current tracer from thread-local.

    If there's no current tracer it'll create a new one.
    :returns: current tracer.
    :rtype: Tracer
    """
    if not hasattr(_thread_local_tracer, 'tracer'):
        _thread_local_tracer.tracer = Tracer()
    return _thread_local_tracer.tracer


def _set_thread_local_tracer(tracer):  # type: (Tracer) -> None
    """Sets the current tracer in thread-local.

    :param tracer: current tracer.
    :type tracer: Tracer
    """
    _thread_local_tracer.tracer = tracer


def _get_contextvars_tracer():  # pragma: no cover
    # type: () -> Tracer
    """Returns the current tracer from contextvars.

    If there's no current tracer it'll create a new one.
    :returns: current tracer.
    :rtype: Tracer
    """
    try:
        return _contextvars_tracer.get()
    except LookupError:
        _contextvars_tracer.set(Tracer())
        return _contextvars_tracer.get()


def _set_contextvars_tracer(tracer):  # pragma: no cover
    # type: (Tracer) -> None
    """Sets the current tracer in contextvars.

    :param tracer: current tracer.
    :type tracer: Tracer
    """
    _contextvars_tracer.set(tracer)


class Tracer(object):

    def __init__(self):  # type: () -> None
        self._is_transport_configured = False
        self._span_storage = SpanStorage()
        self._context_stack = Stack()

    def get_zipkin_attrs(self):  # type: () -> Optional[ZipkinAttrs]
        return self._context_stack.get()

    def push_zipkin_attrs(self, ctx):  # type: (ZipkinAttrs) -> None
        self._context_stack.push(ctx)

    def pop_zipkin_attrs(self):  # type: () -> Optional[ZipkinAttrs]
        return self._context_stack.pop()

    def add_span(self, span):  # type: (Span) -> None
        self._span_storage.append(span)

    def get_spans(self):  # type: () -> SpanStorage
        return self._span_storage

    def clear(self):  # type: () -> None
        self._span_storage.clear()

    def set_transport_configured(self, configured):  # type: (bool) -> None
        self._is_transport_configured = configured

    def is_transport_configured(self):  # type: () -> bool
        return self._is_transport_configured

    def zipkin_span(self, *argv, **kwargs):
        # type: (ZST) -> py_zipkin.zipkin.zipkin_span
        from py_zipkin.zipkin import zipkin_span
        kwargs['_tracer'] = self
        return zipkin_span(*argv, **kwargs)


class Stack(object):
    """
    Stack is a simple stack class.

    It offers the operations push, pop and get.
    The latter two return None if the stack is empty.

    .. deprecated::
       Use the Tracer interface which offers better multi-threading support.
       Stack will be removed in version 1.0.
    """

    def __init__(self, storage=None):  # type: (List[ZipkinAttrs]) -> None
        if storage is not None:
            log.warning('Passing a storage object to Stack is deprecated.')
            self._storage = storage
        else:
            self._storage = []

    def push(self, item):  # type: (ZipkinAttrs) -> None
        self._storage.append(item)

    def pop(self):  # type: () -> Optional[ZipkinAttrs]
        if self._storage:
            return self._storage.pop()
        return None

    def get(self):  # type: () -> Optional[ZipkinAttrs]
        if self._storage:
            return self._storage[-1]
        return None


class ThreadLocalStack(Stack):
    """ThreadLocalStack is variant of Stack that uses a thread local storage.

    The thread local storage is accessed lazily in every method call,
    so the thread that calls the method matters, not the thread that
    instantiated the class.
    Every instance shares the same thread local data.

    .. deprecated::
       Use the Tracer interface which offers better multi-threading support.
       ThreadLocalStack will be removed in version 1.0.
    """

    def __init__(self):  # type: () -> None
        log.warning('ThreadLocalStack is deprecated. See DEPRECATIONS.rst for'
                    'details on how to migrate to using Tracer.')

    @property
    def _storage(self):  # type: ignore
        return get_default_tracer()._context_stack._storage


class SpanStorage(deque):
    """Stores the list of completed spans ready to be sent.

    .. deprecated::
       Use the Tracer interface which offers better multi-threading support.
       SpanStorage will be removed in version 1.0.
    """
    pass


def default_span_storage():  # type: () -> SpanStorage
    log.warning('default_span_storage is deprecated. See DEPRECATIONS.rst for'
                'details on how to migrate to using Tracer.')
    return get_default_tracer()._span_storage


def get_default_tracer():  # type: () -> Tracer
    """Return the current default Tracer.

    For now it'll get it from thread-local in Python 2.7 to 3.6 and from
    contextvars since Python 3.7.

    :returns: current default tracer.
    :rtype: Tracer
    """
    if _contextvars_tracer:
        return _get_contextvars_tracer()

    return _get_thread_local_tracer()


def set_default_tracer(tracer):  # type: (Tracer) -> None
    """Sets the current default Tracer.

    For now it'll get it from thread-local in Python 2.7 to 3.6 and from
    contextvars since Python 3.7.

    :returns: current default tracer.
    :rtype: Tracer
    """
    if _contextvars_tracer:
        _set_contextvars_tracer(tracer)

    _set_thread_local_tracer(tracer)

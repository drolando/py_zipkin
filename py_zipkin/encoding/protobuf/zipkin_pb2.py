# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: zipkin.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='zipkin.proto',
  package='zipkin.proto3',
  syntax='proto3',
  serialized_options=_b('\n\016zipkin2.proto3P\001'),
  serialized_pb=_b('\n\x0czipkin.proto\x12\rzipkin.proto3\"\xf5\x03\n\x04Span\x12\x10\n\x08trace_id\x18\x01 \x01(\x0c\x12\x11\n\tparent_id\x18\x02 \x01(\x0c\x12\n\n\x02id\x18\x03 \x01(\x0c\x12&\n\x04kind\x18\x04 \x01(\x0e\x32\x18.zipkin.proto3.Span.Kind\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x11\n\ttimestamp\x18\x06 \x01(\x06\x12\x10\n\x08\x64uration\x18\x07 \x01(\x04\x12/\n\x0elocal_endpoint\x18\x08 \x01(\x0b\x32\x17.zipkin.proto3.Endpoint\x12\x30\n\x0fremote_endpoint\x18\t \x01(\x0b\x32\x17.zipkin.proto3.Endpoint\x12.\n\x0b\x61nnotations\x18\n \x03(\x0b\x32\x19.zipkin.proto3.Annotation\x12+\n\x04tags\x18\x0b \x03(\x0b\x32\x1d.zipkin.proto3.Span.TagsEntry\x12\r\n\x05\x64\x65\x62ug\x18\x0c \x01(\x08\x12\x0e\n\x06shared\x18\r \x01(\x08\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"U\n\x04Kind\x12\x19\n\x15SPAN_KIND_UNSPECIFIED\x10\x00\x12\n\n\x06\x43LIENT\x10\x01\x12\n\n\x06SERVER\x10\x02\x12\x0c\n\x08PRODUCER\x10\x03\x12\x0c\n\x08\x43ONSUMER\x10\x04\"J\n\x08\x45ndpoint\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\x0c\n\x04ipv4\x18\x02 \x01(\x0c\x12\x0c\n\x04ipv6\x18\x03 \x01(\x0c\x12\x0c\n\x04port\x18\x04 \x01(\x05\".\n\nAnnotation\x12\x11\n\ttimestamp\x18\x01 \x01(\x06\x12\r\n\x05value\x18\x02 \x01(\t\"1\n\x0bListOfSpans\x12\"\n\x05spans\x18\x01 \x03(\x0b\x32\x13.zipkin.proto3.Span\"\x10\n\x0eReportResponse2T\n\x0bSpanService\x12\x45\n\x06Report\x12\x1a.zipkin.proto3.ListOfSpans\x1a\x1d.zipkin.proto3.ReportResponse\"\x00\x42\x12\n\x0ezipkin2.proto3P\x01\x62\x06proto3')
)



_SPAN_KIND = _descriptor.EnumDescriptor(
  name='Kind',
  full_name='zipkin.proto3.Span.Kind',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SPAN_KIND_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLIENT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERVER', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCER', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONSUMER', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=448,
  serialized_end=533,
)
_sym_db.RegisterEnumDescriptor(_SPAN_KIND)


_SPAN_TAGSENTRY = _descriptor.Descriptor(
  name='TagsEntry',
  full_name='zipkin.proto3.Span.TagsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='zipkin.proto3.Span.TagsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='zipkin.proto3.Span.TagsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=403,
  serialized_end=446,
)

_SPAN = _descriptor.Descriptor(
  name='Span',
  full_name='zipkin.proto3.Span',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trace_id', full_name='zipkin.proto3.Span.trace_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent_id', full_name='zipkin.proto3.Span.parent_id', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='zipkin.proto3.Span.id', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kind', full_name='zipkin.proto3.Span.kind', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='zipkin.proto3.Span.name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='zipkin.proto3.Span.timestamp', index=5,
      number=6, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='zipkin.proto3.Span.duration', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local_endpoint', full_name='zipkin.proto3.Span.local_endpoint', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remote_endpoint', full_name='zipkin.proto3.Span.remote_endpoint', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='annotations', full_name='zipkin.proto3.Span.annotations', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='zipkin.proto3.Span.tags', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='debug', full_name='zipkin.proto3.Span.debug', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shared', full_name='zipkin.proto3.Span.shared', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SPAN_TAGSENTRY, ],
  enum_types=[
    _SPAN_KIND,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=533,
)


_ENDPOINT = _descriptor.Descriptor(
  name='Endpoint',
  full_name='zipkin.proto3.Endpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_name', full_name='zipkin.proto3.Endpoint.service_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipv4', full_name='zipkin.proto3.Endpoint.ipv4', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipv6', full_name='zipkin.proto3.Endpoint.ipv6', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='zipkin.proto3.Endpoint.port', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=535,
  serialized_end=609,
)


_ANNOTATION = _descriptor.Descriptor(
  name='Annotation',
  full_name='zipkin.proto3.Annotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='zipkin.proto3.Annotation.timestamp', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='zipkin.proto3.Annotation.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=611,
  serialized_end=657,
)


_LISTOFSPANS = _descriptor.Descriptor(
  name='ListOfSpans',
  full_name='zipkin.proto3.ListOfSpans',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='spans', full_name='zipkin.proto3.ListOfSpans.spans', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=659,
  serialized_end=708,
)


_REPORTRESPONSE = _descriptor.Descriptor(
  name='ReportResponse',
  full_name='zipkin.proto3.ReportResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=710,
  serialized_end=726,
)

_SPAN_TAGSENTRY.containing_type = _SPAN
_SPAN.fields_by_name['kind'].enum_type = _SPAN_KIND
_SPAN.fields_by_name['local_endpoint'].message_type = _ENDPOINT
_SPAN.fields_by_name['remote_endpoint'].message_type = _ENDPOINT
_SPAN.fields_by_name['annotations'].message_type = _ANNOTATION
_SPAN.fields_by_name['tags'].message_type = _SPAN_TAGSENTRY
_SPAN_KIND.containing_type = _SPAN
_LISTOFSPANS.fields_by_name['spans'].message_type = _SPAN
DESCRIPTOR.message_types_by_name['Span'] = _SPAN
DESCRIPTOR.message_types_by_name['Endpoint'] = _ENDPOINT
DESCRIPTOR.message_types_by_name['Annotation'] = _ANNOTATION
DESCRIPTOR.message_types_by_name['ListOfSpans'] = _LISTOFSPANS
DESCRIPTOR.message_types_by_name['ReportResponse'] = _REPORTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Span = _reflection.GeneratedProtocolMessageType('Span', (_message.Message,), {

  'TagsEntry' : _reflection.GeneratedProtocolMessageType('TagsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SPAN_TAGSENTRY,
    '__module__' : 'zipkin_pb2'
    # @@protoc_insertion_point(class_scope:zipkin.proto3.Span.TagsEntry)
    })
  ,
  'DESCRIPTOR' : _SPAN,
  '__module__' : 'zipkin_pb2'
  # @@protoc_insertion_point(class_scope:zipkin.proto3.Span)
  })
_sym_db.RegisterMessage(Span)
_sym_db.RegisterMessage(Span.TagsEntry)

Endpoint = _reflection.GeneratedProtocolMessageType('Endpoint', (_message.Message,), {
  'DESCRIPTOR' : _ENDPOINT,
  '__module__' : 'zipkin_pb2'
  # @@protoc_insertion_point(class_scope:zipkin.proto3.Endpoint)
  })
_sym_db.RegisterMessage(Endpoint)

Annotation = _reflection.GeneratedProtocolMessageType('Annotation', (_message.Message,), {
  'DESCRIPTOR' : _ANNOTATION,
  '__module__' : 'zipkin_pb2'
  # @@protoc_insertion_point(class_scope:zipkin.proto3.Annotation)
  })
_sym_db.RegisterMessage(Annotation)

ListOfSpans = _reflection.GeneratedProtocolMessageType('ListOfSpans', (_message.Message,), {
  'DESCRIPTOR' : _LISTOFSPANS,
  '__module__' : 'zipkin_pb2'
  # @@protoc_insertion_point(class_scope:zipkin.proto3.ListOfSpans)
  })
_sym_db.RegisterMessage(ListOfSpans)

ReportResponse = _reflection.GeneratedProtocolMessageType('ReportResponse', (_message.Message,), {
  'DESCRIPTOR' : _REPORTRESPONSE,
  '__module__' : 'zipkin_pb2'
  # @@protoc_insertion_point(class_scope:zipkin.proto3.ReportResponse)
  })
_sym_db.RegisterMessage(ReportResponse)


DESCRIPTOR._options = None
_SPAN_TAGSENTRY._options = None

_SPANSERVICE = _descriptor.ServiceDescriptor(
  name='SpanService',
  full_name='zipkin.proto3.SpanService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=728,
  serialized_end=812,
  methods=[
  _descriptor.MethodDescriptor(
    name='Report',
    full_name='zipkin.proto3.SpanService.Report',
    index=0,
    containing_service=None,
    input_type=_LISTOFSPANS,
    output_type=_REPORTRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SPANSERVICE)

DESCRIPTOR.services_by_name['SpanService'] = _SPANSERVICE

# @@protoc_insertion_point(module_scope)

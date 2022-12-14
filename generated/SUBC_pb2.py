# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SUBC.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='SUBC.proto',
  package='VisionDAQ',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nSUBC.proto\x12\tVisionDAQ\"a\n\x07\x46romDAQ\x12\x0b\n\x03yaw\x18\x01 \x02(\x05\x12\r\n\x05pitch\x18\x02 \x02(\x05\x12\x0b\n\x03rpm\x18\x03 \x02(\x05\x12\r\n\x05speed\x18\x04 \x02(\x05\x12\r\n\x05\x64\x65pth\x18\x05 \x02(\x05\x12\x0f\n\x07\x62\x61ttery\x18\x06 \x02(\x08'
)




_FROMDAQ = _descriptor.Descriptor(
  name='FromDAQ',
  full_name='VisionDAQ.FromDAQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='yaw', full_name='VisionDAQ.FromDAQ.yaw', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pitch', full_name='VisionDAQ.FromDAQ.pitch', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rpm', full_name='VisionDAQ.FromDAQ.rpm', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='speed', full_name='VisionDAQ.FromDAQ.speed', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='depth', full_name='VisionDAQ.FromDAQ.depth', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='battery', full_name='VisionDAQ.FromDAQ.battery', index=5,
      number=6, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=122,
)

DESCRIPTOR.message_types_by_name['FromDAQ'] = _FROMDAQ
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FromDAQ = _reflection.GeneratedProtocolMessageType('FromDAQ', (_message.Message,), {
  'DESCRIPTOR' : _FROMDAQ,
  '__module__' : 'SUBC_pb2'
  # @@protoc_insertion_point(class_scope:VisionDAQ.FromDAQ)
  })
_sym_db.RegisterMessage(FromDAQ)


# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example_v2.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x65xample_v2.proto\"\xb5\x01\n\x07\x45xample\x12\x11\n\x05\x61_old\x18\x01 \x01(\tB\x02\x18\x01\x12\t\n\x01\x62\x18\x02 \x01(\x03\x12\r\n\x05\x63_new\x18\x06 \x01(\t\x12\x0b\n\x01\x64\x18\x03 \x01(\x01H\x00\x12\x0b\n\x01\x65\x18\x04 \x01(\x01H\x00\x12\x0f\n\x05\x66_new\x18\x07 \x01(\x01H\x00\x12\x1f\n\x06option\x18\x05 \x01(\x0e\x32\x0f.Example.Option\"(\n\x06Option\x12\x05\n\x01\x41\x10\x01\x12\x05\n\x01\x42\x10\x02\x12\x05\n\x01\x43\x10\x03\x12\t\n\x05\x44_NEW\x10\x04\x42\x07\n\x05union\"V\n\x08\x45xamples\x12\x15\n\tcount_old\x18\x01 \x01(\x03\x42\x02\x18\x01\x12\x1a\n\tcount_new\x18\x03 \x01(\x05:\x07\x39\x39\x39\x39\x39\x39\x39\x12\x17\n\x05items\x18\x02 \x03(\x0b\x32\x08.Example')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'example_v2_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EXAMPLE.fields_by_name['a_old']._options = None
  _EXAMPLE.fields_by_name['a_old']._serialized_options = b'\030\001'
  _EXAMPLES.fields_by_name['count_old']._options = None
  _EXAMPLES.fields_by_name['count_old']._serialized_options = b'\030\001'
  _EXAMPLE._serialized_start=21
  _EXAMPLE._serialized_end=202
  _EXAMPLE_OPTION._serialized_start=153
  _EXAMPLE_OPTION._serialized_end=193
  _EXAMPLES._serialized_start=204
  _EXAMPLES._serialized_end=290
# @@protoc_insertion_point(module_scope)
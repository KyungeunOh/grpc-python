# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: greeting.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0egreeting.proto\x12\x10\x63om.example.grpc\"\"\n\x0fGreetingRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"#\n\x10GreetingResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2f\n\x0fGreetingService\x12S\n\x08greeting\x12!.com.example.grpc.GreetingRequest\x1a\".com.example.grpc.GreetingResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'greeting_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GREETINGREQUEST._serialized_start=36
  _GREETINGREQUEST._serialized_end=70
  _GREETINGRESPONSE._serialized_start=72
  _GREETINGRESPONSE._serialized_end=107
  _GREETINGSERVICE._serialized_start=109
  _GREETINGSERVICE._serialized_end=211
# @@protoc_insertion_point(module_scope)

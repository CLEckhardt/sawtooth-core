# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: python/sawtooth_block_info/protobuf/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from python.sawtooth_block_info.protobuf import batch_pb2 as python_dot_sawtooth__block__info_dot_protobuf_dot_batch__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1python/sawtooth_block_info/protobuf/genesis.proto\x1a/python/sawtooth_block_info/protobuf/batch.proto\"&\n\x0bGenesisData\x12\x17\n\x07\x62\x61tches\x18\x01 \x03(\x0b\x32\x06.BatchB&\n\x15sawtooth.sdk.protobufP\x01Z\x0bgenesis_pb2b\x06proto3')



_GENESISDATA = DESCRIPTOR.message_types_by_name['GenesisData']
GenesisData = _reflection.GeneratedProtocolMessageType('GenesisData', (_message.Message,), {
  'DESCRIPTOR' : _GENESISDATA,
  '__module__' : 'python.sawtooth_block_info.protobuf.genesis_pb2'
  # @@protoc_insertion_point(class_scope:GenesisData)
  })
_sym_db.RegisterMessage(GenesisData)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025sawtooth.sdk.protobufP\001Z\013genesis_pb2'
  _GENESISDATA._serialized_start=102
  _GENESISDATA._serialized_end=140
# @@protoc_insertion_point(module_scope)

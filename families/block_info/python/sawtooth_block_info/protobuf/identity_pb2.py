# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: python/sawtooth_block_info/protobuf/identity.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2python/sawtooth_block_info/protobuf/identity.proto\"\xae\x01\n\x06Policy\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1e\n\x07\x65ntries\x18\x02 \x03(\x0b\x32\r.Policy.Entry\x1a\x35\n\x05\x45ntry\x12\x1f\n\x04type\x18\x01 \x01(\x0e\x32\x11.Policy.EntryType\x12\x0b\n\x03key\x18\x02 \x01(\t\"?\n\tEntryType\x12\x14\n\x10\x45NTRY_TYPE_UNSET\x10\x00\x12\x0e\n\nPERMIT_KEY\x10\x01\x12\x0c\n\x08\x44\x45NY_KEY\x10\x02\"\'\n\nPolicyList\x12\x19\n\x08policies\x18\x01 \x03(\x0b\x32\x07.Policy\")\n\x04Role\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bpolicy_name\x18\x02 \x01(\t\" \n\x08RoleList\x12\x14\n\x05roles\x18\x01 \x03(\x0b\x32\x05.RoleB\x1e\n\x1asawtooth.identity.protobufP\x01\x62\x06proto3')



_POLICY = DESCRIPTOR.message_types_by_name['Policy']
_POLICY_ENTRY = _POLICY.nested_types_by_name['Entry']
_POLICYLIST = DESCRIPTOR.message_types_by_name['PolicyList']
_ROLE = DESCRIPTOR.message_types_by_name['Role']
_ROLELIST = DESCRIPTOR.message_types_by_name['RoleList']
_POLICY_ENTRYTYPE = _POLICY.enum_types_by_name['EntryType']
Policy = _reflection.GeneratedProtocolMessageType('Policy', (_message.Message,), {

  'Entry' : _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), {
    'DESCRIPTOR' : _POLICY_ENTRY,
    '__module__' : 'python.sawtooth_block_info.protobuf.identity_pb2'
    # @@protoc_insertion_point(class_scope:Policy.Entry)
    })
  ,
  'DESCRIPTOR' : _POLICY,
  '__module__' : 'python.sawtooth_block_info.protobuf.identity_pb2'
  # @@protoc_insertion_point(class_scope:Policy)
  })
_sym_db.RegisterMessage(Policy)
_sym_db.RegisterMessage(Policy.Entry)

PolicyList = _reflection.GeneratedProtocolMessageType('PolicyList', (_message.Message,), {
  'DESCRIPTOR' : _POLICYLIST,
  '__module__' : 'python.sawtooth_block_info.protobuf.identity_pb2'
  # @@protoc_insertion_point(class_scope:PolicyList)
  })
_sym_db.RegisterMessage(PolicyList)

Role = _reflection.GeneratedProtocolMessageType('Role', (_message.Message,), {
  'DESCRIPTOR' : _ROLE,
  '__module__' : 'python.sawtooth_block_info.protobuf.identity_pb2'
  # @@protoc_insertion_point(class_scope:Role)
  })
_sym_db.RegisterMessage(Role)

RoleList = _reflection.GeneratedProtocolMessageType('RoleList', (_message.Message,), {
  'DESCRIPTOR' : _ROLELIST,
  '__module__' : 'python.sawtooth_block_info.protobuf.identity_pb2'
  # @@protoc_insertion_point(class_scope:RoleList)
  })
_sym_db.RegisterMessage(RoleList)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032sawtooth.identity.protobufP\001'
  _POLICY._serialized_start=55
  _POLICY._serialized_end=229
  _POLICY_ENTRY._serialized_start=111
  _POLICY_ENTRY._serialized_end=164
  _POLICY_ENTRYTYPE._serialized_start=166
  _POLICY_ENTRYTYPE._serialized_end=229
  _POLICYLIST._serialized_start=231
  _POLICYLIST._serialized_end=270
  _ROLE._serialized_start=272
  _ROLE._serialized_end=313
  _ROLELIST._serialized_start=315
  _ROLELIST._serialized_end=347
# @@protoc_insertion_point(module_scope)

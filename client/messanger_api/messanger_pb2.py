# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messanger.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fmessanger.proto\"<\n\nUpdateData\x12\x1b\n\x06status\x18\x01 \x01(\x0e\x32\x0b.CodeResult\x12\x11\n\tjson_info\x18\x02 \x01(\t\"J\n\x15MessagesUpdateRequest\x12\x13\n\x0b\x63redentials\x18\x01 \x01(\t\x12\x0e\n\x06update\x18\x02 \x01(\t\x12\x0c\n\x04time\x18\x03 \x01(\x05\"6\n\x11RemoveRoomReqeust\x12\x0c\n\x04room\x18\x01 \x01(\t\x12\x13\n\x0b\x63redentials\x18\x02 \x01(\t\"<\n\nClientInfo\x12\x1b\n\x06status\x18\x01 \x01(\x0e\x32\x0b.CodeResult\x12\x11\n\tjson_info\x18\x02 \x01(\t\"4\n\x0fRequestSelfInfo\x12\x13\n\x0b\x63redentials\x18\x01 \x01(\t\x12\x0c\n\x04time\x18\x02 \x01(\x05\"\'\n\x08Response\x12\x1b\n\x06status\x18\x01 \x01(\x0e\x32\x0b.CodeResult\"B\n\x07Message\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x11\n\taddressee\x18\x02 \x01(\t\x12\x13\n\x0b\x63redentials\x18\x03 \x01(\t\"7\n\x10\x41\x64\x64\x46riendRequest\x12\x0e\n\x06\x66riend\x18\x01 \x01(\t\x12\x13\n\x0b\x63redentials\x18\x02 \x01(\t\":\n\x13RemoveFriendRequest\x12\x0e\n\x06\x66riend\x18\x01 \x01(\t\x12\x13\n\x0b\x63redentials\x18\x02 \x01(\t\"6\n\x11\x43reateRoomRequest\x12\x0c\n\x04room\x18\x01 \x01(\t\x12\x13\n\x0b\x63redentials\x18\x02 \x01(\t\"4\n\x0fJoinRoomRequest\x12\x0c\n\x04room\x18\x01 \x01(\t\x12\x13\n\x0b\x63redentials\x18\x02 \x01(\t\"6\n\x11\x45scapeRoomRequest\x12\x0c\n\x04room\x18\x01 \x01(\t\x12\x13\n\x0b\x63redentials\x18\x02 \x01(\t*1\n\nCodeResult\x12\x12\n\x0eunknown_format\x10\x00\x12\x06\n\x02ok\x10\x01\x12\x07\n\x03\x62\x61\x64\x10\x02\x32\xb9\x03\n\tMessanger\x12\x35\n\x12InformationRequest\x12\x10.RequestSelfInfo\x1a\x0b.ClientInfo\"\x00\x12$\n\x0bSendMessage\x12\x08.Message\x1a\t.Response\"\x00\x12+\n\tAddFriend\x12\x11.AddFriendRequest\x1a\t.Response\"\x00\x12\x31\n\x0cRemoveFriend\x12\x14.RemoveFriendRequest\x1a\t.Response\"\x00\x12-\n\nCreateRoom\x12\x12.CreateRoomRequest\x1a\t.Response\"\x00\x12)\n\x08JoinRoom\x12\x10.JoinRoomRequest\x1a\t.Response\"\x00\x12-\n\nRoomEscape\x12\x12.EscapeRoomRequest\x1a\t.Response\"\x00\x12-\n\nRemoveRoom\x12\x12.RemoveRoomReqeust\x1a\t.Response\"\x00\x12\x37\n\x0eMessagesUpdate\x12\x16.MessagesUpdateRequest\x1a\x0b.UpdateData\"\x00\x62\x06proto3')

_CODERESULT = DESCRIPTOR.enum_types_by_name['CodeResult']
CodeResult = enum_type_wrapper.EnumTypeWrapper(_CODERESULT)
unknown_format = 0
ok = 1
bad = 2


_UPDATEDATA = DESCRIPTOR.message_types_by_name['UpdateData']
_MESSAGESUPDATEREQUEST = DESCRIPTOR.message_types_by_name['MessagesUpdateRequest']
_REMOVEROOMREQEUST = DESCRIPTOR.message_types_by_name['RemoveRoomReqeust']
_CLIENTINFO = DESCRIPTOR.message_types_by_name['ClientInfo']
_REQUESTSELFINFO = DESCRIPTOR.message_types_by_name['RequestSelfInfo']
_RESPONSE = DESCRIPTOR.message_types_by_name['Response']
_MESSAGE = DESCRIPTOR.message_types_by_name['Message']
_ADDFRIENDREQUEST = DESCRIPTOR.message_types_by_name['AddFriendRequest']
_REMOVEFRIENDREQUEST = DESCRIPTOR.message_types_by_name['RemoveFriendRequest']
_CREATEROOMREQUEST = DESCRIPTOR.message_types_by_name['CreateRoomRequest']
_JOINROOMREQUEST = DESCRIPTOR.message_types_by_name['JoinRoomRequest']
_ESCAPEROOMREQUEST = DESCRIPTOR.message_types_by_name['EscapeRoomRequest']
UpdateData = _reflection.GeneratedProtocolMessageType('UpdateData', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDATA,
  '__module__' : 'messanger_pb2'
  # @@protoc_insertion_point(class_scope:UpdateData)
  })
_sym_db.RegisterMessage(UpdateData)

MessagesUpdateRequest = _reflection.GeneratedProtocolMessageType('MessagesUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGESUPDATEREQUEST,
  '__module__' : 'messanger_pb2'
  # @@protoc_insertion_point(class_scope:MessagesUpdateRequest)
  })
_sym_db.RegisterMessage(MessagesUpdateRequest)

RemoveRoomReqeust = _reflection.GeneratedProtocolMessageType('RemoveRoomReqeust', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEROOMREQEUST,
  '__module__' : 'messanger_pb2'
  # @@protoc_insertion_point(class_scope:RemoveRoomReqeust)
  })
_sym_db.RegisterMessage(RemoveRoomReqeust)

ClientInfo = _reflection.GeneratedProtocolMessageType('ClientInfo', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTINFO,
  '__module__' : 'messanger_pb2'
  # @@protoc_insertion_point(class_scope:ClientInfo)
  })
_sym_db.RegisterMessage(ClientInfo)

RequestSelfInfo = _reflection.GeneratedProtocolMessageType('RequestSelfInfo', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTSELFINFO,
  '__module__' : 'messanger_pb2'
  # @@protoc_insertion_point(class_scope:RequestSelfInfo)
  })
_sym_db.RegisterMessage(RequestSelfInfo)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'messanger_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  })
_sym_db.RegisterMessage(Response)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'messanger_pb2'
  # @@protoc_insertion_point(class_scope:Message)
  })
_sym_db.RegisterMessage(Message)

AddFriendRequest = _reflection.GeneratedProtocolMessageType('AddFriendRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDFRIENDREQUEST,
  '__module__' : 'messanger_pb2'
  # @@protoc_insertion_point(class_scope:AddFriendRequest)
  })
_sym_db.RegisterMessage(AddFriendRequest)

RemoveFriendRequest = _reflection.GeneratedProtocolMessageType('RemoveFriendRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEFRIENDREQUEST,
  '__module__' : 'messanger_pb2'
  # @@protoc_insertion_point(class_scope:RemoveFriendRequest)
  })
_sym_db.RegisterMessage(RemoveFriendRequest)

CreateRoomRequest = _reflection.GeneratedProtocolMessageType('CreateRoomRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEROOMREQUEST,
  '__module__' : 'messanger_pb2'
  # @@protoc_insertion_point(class_scope:CreateRoomRequest)
  })
_sym_db.RegisterMessage(CreateRoomRequest)

JoinRoomRequest = _reflection.GeneratedProtocolMessageType('JoinRoomRequest', (_message.Message,), {
  'DESCRIPTOR' : _JOINROOMREQUEST,
  '__module__' : 'messanger_pb2'
  # @@protoc_insertion_point(class_scope:JoinRoomRequest)
  })
_sym_db.RegisterMessage(JoinRoomRequest)

EscapeRoomRequest = _reflection.GeneratedProtocolMessageType('EscapeRoomRequest', (_message.Message,), {
  'DESCRIPTOR' : _ESCAPEROOMREQUEST,
  '__module__' : 'messanger_pb2'
  # @@protoc_insertion_point(class_scope:EscapeRoomRequest)
  })
_sym_db.RegisterMessage(EscapeRoomRequest)

_MESSANGER = DESCRIPTOR.services_by_name['Messanger']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CODERESULT._serialized_start=721
  _CODERESULT._serialized_end=770
  _UPDATEDATA._serialized_start=19
  _UPDATEDATA._serialized_end=79
  _MESSAGESUPDATEREQUEST._serialized_start=81
  _MESSAGESUPDATEREQUEST._serialized_end=155
  _REMOVEROOMREQEUST._serialized_start=157
  _REMOVEROOMREQEUST._serialized_end=211
  _CLIENTINFO._serialized_start=213
  _CLIENTINFO._serialized_end=273
  _REQUESTSELFINFO._serialized_start=275
  _REQUESTSELFINFO._serialized_end=327
  _RESPONSE._serialized_start=329
  _RESPONSE._serialized_end=368
  _MESSAGE._serialized_start=370
  _MESSAGE._serialized_end=436
  _ADDFRIENDREQUEST._serialized_start=438
  _ADDFRIENDREQUEST._serialized_end=493
  _REMOVEFRIENDREQUEST._serialized_start=495
  _REMOVEFRIENDREQUEST._serialized_end=553
  _CREATEROOMREQUEST._serialized_start=555
  _CREATEROOMREQUEST._serialized_end=609
  _JOINROOMREQUEST._serialized_start=611
  _JOINROOMREQUEST._serialized_end=663
  _ESCAPEROOMREQUEST._serialized_start=665
  _ESCAPEROOMREQUEST._serialized_end=719
  _MESSANGER._serialized_start=773
  _MESSANGER._serialized_end=1214
# @@protoc_insertion_point(module_scope)

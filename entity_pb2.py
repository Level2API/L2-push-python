# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: entity.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0c\x65ntity.proto\x12\rsa.rpc.entity\x1a\x19google/protobuf/any.proto\"\x06\n\x04Void\"\x15\n\x04\x42ool\x12\r\n\x05value\x18\x01 \x01(\x08\"\x17\n\x06String\x12\r\n\x05value\x18\x01 \x01(\t\"\x1c\n\nStringList\x12\x0e\n\x06values\x18\x01 \x03(\t\"\x16\n\x05\x42ytes\x12\r\n\x05value\x18\x01 \x01(\x0c\"\x16\n\x05Int64\x12\r\n\x05value\x18\x01 \x01(\x03\"\x1b\n\tInt64List\x12\x0e\n\x06values\x18\x01 \x03(\x03\"\x16\n\x05Int32\x12\r\n\x05value\x18\x01 \x01(\x03\"\x1b\n\tInt32List\x12\x0e\n\x06values\x18\x01 \x03(\x05\"\xd9\x01\n\nTickRecord\x12\x16\n\x0estock_exchange\x18\x01 \x01(\r\x12\x12\n\nstock_code\x18\x02 \x01(\t\x12\x12\n\ncreated_at\x18\x03 \x01(\x03\x12\x0c\n\x04\x63ode\x18\x04 \x01(\t\x12\r\n\x05price\x18\x05 \x01(\r\x12\x0e\n\x06volume\x18\x06 \x01(\x04\x12\x0e\n\x06\x61mount\x18\x07 \x01(\x04\x12\x0e\n\x06tx_dir\x18\x08 \x01(\r\x12\x0f\n\x07tx_kind\x18\t \x01(\r\x12\x15\n\rbuy_order_seq\x18\n \x01(\t\x12\x16\n\x0esell_order_seq\x18\x0b \x01(\t\"\xab\x01\n\x0bOrderRecord\x12\x16\n\x0estock_exchange\x18\x01 \x01(\r\x12\x12\n\nstock_code\x18\x02 \x01(\t\x12\x12\n\ncreated_at\x18\x03 \x01(\x03\x12\x0c\n\x04\x63ode\x18\x04 \x01(\t\x12\r\n\x05price\x18\x05 \x01(\r\x12\x0e\n\x06volume\x18\x06 \x01(\x04\x12\x0e\n\x06\x61mount\x18\x07 \x01(\x04\x12\x0e\n\x06tx_dir\x18\x08 \x01(\r\x12\x0f\n\x07tx_kind\x18\t \x01(\r\"\xde\x01\n\x10OrderQueueRecord\x12\x16\n\x0estock_exchange\x18\x01 \x01(\r\x12\x12\n\nstock_code\x18\x02 \x01(\t\x12\x12\n\ncreated_at\x18\x03 \x01(\x03\x12\x12\n\nbid1_price\x18\x04 \x01(\r\x12\x15\n\rbid1_quantity\x18\x05 \x01(\r\x12\x12\n\nask1_price\x18\x06 \x01(\r\x12\x15\n\rask1_quantity\x18\x07 \x01(\r\x12\x19\n\x11\x62id_volume_detail\x18\x08 \x03(\r\x12\x19\n\x11\x61sk_volume_detail\x18\t \x03(\r\"\xef\x03\n\x10StockQuoteRecord\x12\x16\n\x0estock_exchange\x18\x01 \x01(\r\x12\x12\n\nstock_code\x18\x02 \x01(\t\x12\x12\n\ncreated_at\x18\x03 \x01(\x03\x12\x0e\n\x06status\x18\x04 \x01(\r\x12\x18\n\x10prev_close_price\x18\x05 \x01(\r\x12\x12\n\nopen_price\x18\x06 \x01(\r\x12\x14\n\x0clatest_price\x18\x07 \x01(\r\x12\x12\n\nhigh_price\x18\x08 \x01(\r\x12\x11\n\tlow_price\x18\t \x01(\r\x12\x16\n\x0elimit_up_price\x18\n \x01(\r\x12\x18\n\x10limit_down_price\x18\x0b \x01(\r\x12\x16\n\x0eorder_quantity\x18\x0c \x01(\r\x12\x0e\n\x06volume\x18\r \x01(\x04\x12\x0e\n\x06\x61mount\x18\x0e \x01(\x04\x12\x12\n\nbid_volume\x18\x0f \x01(\x04\x12\x11\n\tbid_price\x18\x10 \x01(\r\x12\x12\n\nask_volume\x18\x11 \x01(\x04\x12\x11\n\task_price\x18\x12 \x01(\r\x12\x18\n\x10\x62id_price_detail\x18\x13 \x03(\r\x12\x19\n\x11\x62id_volume_detail\x18\x14 \x03(\r\x12\x18\n\x10\x61sk_price_detail\x18\x15 \x03(\r\x12\x19\n\x11\x61sk_volume_detail\x18\x16 \x03(\r\"\xe7\x02\n\x12StockQuoteSnapshot\x12\x14\n\x0cstock_symbol\x18\x01 \x01(\t\x12\x12\n\ncreated_at\x18\x04 \x01(\x03\x12\x18\n\x10prev_close_price\x18\x05 \x01(\r\x12\x12\n\nopen_price\x18\x06 \x01(\r\x12\x14\n\x0clatest_price\x18\x07 \x01(\r\x12\x12\n\nhigh_price\x18\x08 \x01(\r\x12\x11\n\tlow_price\x18\t \x01(\r\x12\x0e\n\x06volume\x18\r \x01(\x04\x12\x0e\n\x06\x61mount\x18\x0e \x01(\x04\x12\x15\n\rturnover_rate\x18\x0f \x01(\x02\x12\x11\n\tamplitude\x18\x10 \x01(\x02\x12\x1a\n\x12total_stock_volume\x18\x11 \x01(\x04\x12\x1a\n\x12\x66loat_stock_volume\x18\x12 \x01(\x04\x12\x1c\n\x14total_market_capital\x18\x13 \x01(\x04\x12\x1c\n\x14\x66loat_market_capital\x18\x14 \x01(\x04\"K\n\x16StockQuoteSnapshotList\x12\x31\n\x06values\x18\x01 \x03(\x0b\x32!.sa.rpc.entity.StockQuoteSnapshot\"@\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04role\x18\x02 \x01(\x05\x12\x0f\n\x07version\x18\x03 \x01(\x03\x12\r\n\x05\x63omet\x18\x04 \x01(\x05\"B\n\x08\x41uthInfo\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04role\x18\x02 \x01(\x05\x12\r\n\x05token\x18\x03 \x01(\t\x12\r\n\x05\x63omet\x18\x04 \x01(\x05\"\xde\x01\n\nAPIMessage\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03\x61pi\x18\x02 \x01(\x05\x12\x12\n\ncreated_at\x18\x05 \x01(\x03\x12\"\n\x04\x64\x61ta\x18\x06 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0c\n\x04\x63ode\x18\x07 \x01(\x05\x12\x0b\n\x03msg\x18\x08 \x01(\t\x12\x35\n\x06header\x18\t \x03(\x0b\x32%.sa.rpc.entity.APIMessage.HeaderEntry\x1a-\n\x0bHeaderEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x80\x01\n\x0cSubscription\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x15\n\rtopic_pattern\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\x03\x12\x1b\n\x13max_subscribe_count\x18\x04 \x01(\r\x12\x1c\n\x14used_subscribe_count\x18\x05 \x01(\r\"`\n\x18GetStockQuoteSnapShotReq\x12\x14\n\x0cstock_symbol\x18\x01 \x01(\t\x12\x16\n\x0emin_created_at\x18\x02 \x01(\x03\x12\x16\n\x0emax_created_at\x18\x03 \x01(\x03\"\xf1\x05\n\x0cIndMISummary\x12\x14\n\x0cstock_symbol\x18\x01 \x01(\t\x12\x12\n\ncreated_at\x18\x02 \x01(\x03\x12\x1c\n\x14\x61\x63\x65_quantity_summary\x18\x03 \x03(\x04\x12\x1c\n\x14\x64\x64y_quantity_summary\x18\x04 \x03(\x04\x12\x1a\n\x12\x64\x64x_amount_summary\x18\x05 \x03(\x04\x12\x0b\n\x03\x64\x64x\x18\n \x01(\x01\x12\x0b\n\x03\x64\x64y\x18\x0b \x01(\x01\x12\x0c\n\x04\x64\x64z0\x18\x0c \x01(\x01\x12\x0c\n\x04\x64\x64z1\x18\r \x01(\x01\x12\x0c\n\x04\x64\x64z2\x18\x0e \x01(\x01\x12\x0c\n\x04\x64\x64z3\x18\x0f \x01(\x01\x12\x0c\n\x04\x64\x64z4\x18\x10 \x01(\x01\x12\x12\n\nddx_d5_avg\x18\x11 \x01(\x01\x12\x12\n\nddy_d5_avg\x18\x12 \x01(\x01\x12\x13\n\x0b\x64\x64z0_d5_avg\x18\x13 \x01(\x01\x12\x13\n\x0b\x64\x64z1_d5_avg\x18\x14 \x01(\x01\x12\x13\n\x0b\x64\x64z2_d5_avg\x18\x15 \x01(\x01\x12\x13\n\x0b\x64\x64z3_d5_avg\x18\x16 \x01(\x01\x12\x13\n\x0b\x64\x64z4_d5_avg\x18\x17 \x01(\x01\x12\x13\n\x0b\x64\x64x_d20_avg\x18\x18 \x01(\x01\x12\x13\n\x0b\x64\x64y_d20_avg\x18\x19 \x01(\x01\x12\x14\n\x0c\x64\x64z0_d20_avg\x18\x1a \x01(\x01\x12\x14\n\x0c\x64\x64z1_d20_avg\x18\x1b \x01(\x01\x12\x14\n\x0c\x64\x64z2_d20_avg\x18\x1c \x01(\x01\x12\x14\n\x0c\x64\x64z3_d20_avg\x18\x1d \x01(\x01\x12\x14\n\x0c\x64\x64z4_d20_avg\x18\x1e \x01(\x01\x12\x13\n\x0b\x64\x64x_d60_avg\x18\x1f \x01(\x01\x12\x13\n\x0b\x64\x64y_d60_avg\x18  \x01(\x01\x12\x14\n\x0c\x64\x64z0_d60_avg\x18! \x01(\x01\x12\x14\n\x0c\x64\x64z1_d60_avg\x18\" \x01(\x01\x12\x14\n\x0c\x64\x64z2_d60_avg\x18# \x01(\x01\x12\x14\n\x0c\x64\x64z3_d60_avg\x18$ \x01(\x01\x12\x14\n\x0c\x64\x64z4_d60_avg\x18% \x01(\x01\x12\x1e\n\x16\x64\x64x_d10_cont_red_count\x18& \x01(\r\x12\x1e\n\x16\x64\x64x_d10_aggr_red_count\x18\' \x01(\r\"?\n\x10IndMISummaryList\x12+\n\x06values\x18\x01 \x03(\x0b\x32\x1b.sa.rpc.entity.IndMISummary\"\xf1\x05\n\x0cIndDDSummary\x12\x14\n\x0cstock_symbol\x18\x01 \x01(\t\x12\x12\n\ncreated_at\x18\x02 \x01(\x03\x12\x1c\n\x14\x61\x63\x65_quantity_summary\x18\x03 \x03(\x04\x12\x1c\n\x14\x64\x64y_quantity_summary\x18\x04 \x03(\x04\x12\x1a\n\x12\x64\x64x_amount_summary\x18\x05 \x03(\x04\x12\x0b\n\x03\x64\x64x\x18\n \x01(\x01\x12\x0b\n\x03\x64\x64y\x18\x0b \x01(\x01\x12\x0c\n\x04\x64\x64z0\x18\x0c \x01(\x01\x12\x0c\n\x04\x64\x64z1\x18\r \x01(\x01\x12\x0c\n\x04\x64\x64z2\x18\x0e \x01(\x01\x12\x0c\n\x04\x64\x64z3\x18\x0f \x01(\x01\x12\x0c\n\x04\x64\x64z4\x18\x10 \x01(\x01\x12\x12\n\nddx_d5_avg\x18\x11 \x01(\x01\x12\x12\n\nddy_d5_avg\x18\x12 \x01(\x01\x12\x13\n\x0b\x64\x64z0_d5_avg\x18\x13 \x01(\x01\x12\x13\n\x0b\x64\x64z1_d5_avg\x18\x14 \x01(\x01\x12\x13\n\x0b\x64\x64z2_d5_avg\x18\x15 \x01(\x01\x12\x13\n\x0b\x64\x64z3_d5_avg\x18\x16 \x01(\x01\x12\x13\n\x0b\x64\x64z4_d5_avg\x18\x17 \x01(\x01\x12\x13\n\x0b\x64\x64x_d20_avg\x18\x18 \x01(\x01\x12\x13\n\x0b\x64\x64y_d20_avg\x18\x19 \x01(\x01\x12\x14\n\x0c\x64\x64z0_d20_avg\x18\x1a \x01(\x01\x12\x14\n\x0c\x64\x64z1_d20_avg\x18\x1b \x01(\x01\x12\x14\n\x0c\x64\x64z2_d20_avg\x18\x1c \x01(\x01\x12\x14\n\x0c\x64\x64z3_d20_avg\x18\x1d \x01(\x01\x12\x14\n\x0c\x64\x64z4_d20_avg\x18\x1e \x01(\x01\x12\x13\n\x0b\x64\x64x_d60_avg\x18\x1f \x01(\x01\x12\x13\n\x0b\x64\x64y_d60_avg\x18  \x01(\x01\x12\x14\n\x0c\x64\x64z0_d60_avg\x18! \x01(\x01\x12\x14\n\x0c\x64\x64z1_d60_avg\x18\" \x01(\x01\x12\x14\n\x0c\x64\x64z2_d60_avg\x18# \x01(\x01\x12\x14\n\x0c\x64\x64z3_d60_avg\x18$ \x01(\x01\x12\x14\n\x0c\x64\x64z4_d60_avg\x18% \x01(\x01\x12\x1e\n\x16\x64\x64x_d10_cont_red_count\x18& \x01(\r\x12\x1e\n\x16\x64\x64x_d10_aggr_red_count\x18\' \x01(\r\"?\n\x10IndDDSummaryList\x12+\n\x06values\x18\x01 \x03(\x0b\x32\x1b.sa.rpc.entity.IndDDSummary\"^\n\tGetIndReq\x12\x0b\n\x03ind\x18\x01 \x01(\r\x12\x14\n\x0cstock_symbol\x18\x02 \x01(\t\x12\x16\n\x0emin_created_at\x18\x03 \x01(\x03\x12\x16\n\x0emax_created_at\x18\x04 \x01(\x03\x42\x16Z\x14sa-common/rpc/entityb\x06proto3')

_VOID = DESCRIPTOR.message_types_by_name['Void']
_BOOL = DESCRIPTOR.message_types_by_name['Bool']
_STRING = DESCRIPTOR.message_types_by_name['String']
_STRINGLIST = DESCRIPTOR.message_types_by_name['StringList']
_BYTES = DESCRIPTOR.message_types_by_name['Bytes']
_INT64 = DESCRIPTOR.message_types_by_name['Int64']
_INT64LIST = DESCRIPTOR.message_types_by_name['Int64List']
_INT32 = DESCRIPTOR.message_types_by_name['Int32']
_INT32LIST = DESCRIPTOR.message_types_by_name['Int32List']
_TICKRECORD = DESCRIPTOR.message_types_by_name['TickRecord']
_ORDERRECORD = DESCRIPTOR.message_types_by_name['OrderRecord']
_ORDERQUEUERECORD = DESCRIPTOR.message_types_by_name['OrderQueueRecord']
_STOCKQUOTERECORD = DESCRIPTOR.message_types_by_name['StockQuoteRecord']
_STOCKQUOTESNAPSHOT = DESCRIPTOR.message_types_by_name['StockQuoteSnapshot']
_STOCKQUOTESNAPSHOTLIST = DESCRIPTOR.message_types_by_name['StockQuoteSnapshotList']
_USER = DESCRIPTOR.message_types_by_name['User']
_AUTHINFO = DESCRIPTOR.message_types_by_name['AuthInfo']
_APIMESSAGE = DESCRIPTOR.message_types_by_name['APIMessage']
_APIMESSAGE_HEADERENTRY = _APIMESSAGE.nested_types_by_name['HeaderEntry']
_SUBSCRIPTION = DESCRIPTOR.message_types_by_name['Subscription']
_GETSTOCKQUOTESNAPSHOTREQ = DESCRIPTOR.message_types_by_name['GetStockQuoteSnapShotReq']
_INDMISUMMARY = DESCRIPTOR.message_types_by_name['IndMISummary']
_INDMISUMMARYLIST = DESCRIPTOR.message_types_by_name['IndMISummaryList']
_INDDDSUMMARY = DESCRIPTOR.message_types_by_name['IndDDSummary']
_INDDDSUMMARYLIST = DESCRIPTOR.message_types_by_name['IndDDSummaryList']
_GETINDREQ = DESCRIPTOR.message_types_by_name['GetIndReq']
Void = _reflection.GeneratedProtocolMessageType('Void', (_message.Message,), {
    'DESCRIPTOR': _VOID,
    '__module__': 'entity_pb2'
    # @@protoc_insertion_point(class_scope:sa.rpc.entity.Void)
})
_sym_db.RegisterMessage(Void)

Bool = _reflection.GeneratedProtocolMessageType('Bool', (_message.Message,), {
    'DESCRIPTOR': _BOOL,
    '__module__': 'entity_pb2'
    # @@protoc_insertion_point(class_scope:sa.rpc.entity.Bool)
})
_sym_db.RegisterMessage(Bool)

String = _reflection.GeneratedProtocolMessageType('String', (_message.Message,), {
    'DESCRIPTOR': _STRING,
    '__module__': 'entity_pb2'
    # @@protoc_insertion_point(class_scope:sa.rpc.entity.String)
})
_sym_db.RegisterMessage(String)

StringList = _reflection.GeneratedProtocolMessageType('StringList', (_message.Message,), {
    'DESCRIPTOR': _STRINGLIST,
    '__module__': 'entity_pb2'
    # @@protoc_insertion_point(class_scope:sa.rpc.entity.StringList)
})
_sym_db.RegisterMessage(StringList)

Bytes = _reflection.GeneratedProtocolMessageType('Bytes', (_message.Message,), {
    'DESCRIPTOR': _BYTES,
    '__module__': 'entity_pb2'
    # @@protoc_insertion_point(class_scope:sa.rpc.entity.Bytes)
})
_sym_db.RegisterMessage(Bytes)

Int64 = _reflection.GeneratedProtocolMessageType('Int64', (_message.Message,), {
    'DESCRIPTOR': _INT64,
    '__module__': 'entity_pb2'
    # @@protoc_insertion_point(class_scope:sa.rpc.entity.Int64)
})
_sym_db.RegisterMessage(Int64)

Int64List = _reflection.GeneratedProtocolMessageType('Int64List', (_message.Message,), {
    'DESCRIPTOR': _INT64LIST,
    '__module__': 'entity_pb2'
    # @@protoc_insertion_point(class_scope:sa.rpc.entity.Int64List)
})
_sym_db.RegisterMessage(Int64List)

Int32 = _reflection.GeneratedProtocolMessageType('Int32', (_message.Message,), {
    'DESCRIPTOR': _INT32,
    '__module__': 'entity_pb2'
    # @@protoc_insertion_point(class_scope:sa.rpc.entity.Int32)
})
_sym_db.RegisterMessage(Int32)

Int32List = _reflection.GeneratedProtocolMessageType('Int32List', (_message.Message,), {
    'DESCRIPTOR': _INT32LIST,
    '__module__': 'entity_pb2'
    # @@protoc_insertion_point(class_scope:sa.rpc.entity.Int32List)
})
_sym_db.RegisterMessage(Int32List)

TickRecord = _reflection.GeneratedProtocolMessageType('TickRecord', (_message.Message,), {
    'DESCRIPTOR': _TICKRECORD,
    '__module__': 'entity_pb2'
    # @@protoc_insertion_point(class_scope:sa.rpc.entity.TickRecord)
})
_sym_db.RegisterMessage(TickRecord)

OrderRecord = _reflection.GeneratedProtocolMessageType('OrderRecord', (_message.Message,), {
    'DESCRIPTOR': _ORDERRECORD,
    '__module__': 'entity_pb2'
    # @@protoc_insertion_point(class_scope:sa.rpc.entity.OrderRecord)
})
_sym_db.RegisterMessage(OrderRecord)

OrderQueueRecord = _reflection.GeneratedProtocolMessageType('OrderQueueRecord', (_message.Message,), {
    'DESCRIPTOR': _ORDERQUEUERECORD,
    '__module__': 'entity_pb2'
    # @@protoc_insertion_point(class_scope:sa.rpc.entity.OrderQueueRecord)
})
_sym_db.RegisterMessage(OrderQueueRecord)

StockQuoteRecord = _reflection.GeneratedProtocolMessageType('StockQuoteRecord', (_message.Message,), {
    'DESCRIPTOR': _STOCKQUOTERECORD,
    '__module__': 'entity_pb2'
    # @@protoc_insertion_point(class_scope:sa.rpc.entity.StockQuoteRecord)
})
_sym_db.RegisterMessage(StockQuoteRecord)

StockQuoteSnapshot = _reflection.GeneratedProtocolMessageType('StockQuoteSnapshot', (_message.Message,), {
    'DESCRIPTOR': _STOCKQUOTESNAPSHOT,
    '__module__': 'entity_pb2'
    # @@protoc_insertion_point(class_scope:sa.rpc.entity.StockQuoteSnapshot)
})
_sym_db.RegisterMessage(StockQuoteSnapshot)

StockQuoteSnapshotList = _reflection.GeneratedProtocolMessageType('StockQuoteSnapshotList', (_message.Message,), {
    'DESCRIPTOR': _STOCKQUOTESNAPSHOTLIST,
    '__module__': 'entity_pb2'
    # @@protoc_insertion_point(class_scope:sa.rpc.entity.StockQuoteSnapshotList)
})
_sym_db.RegisterMessage(StockQuoteSnapshotList)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
    'DESCRIPTOR': _USER,
    '__module__': 'entity_pb2'
    # @@protoc_insertion_point(class_scope:sa.rpc.entity.User)
})
_sym_db.RegisterMessage(User)

AuthInfo = _reflection.GeneratedProtocolMessageType('AuthInfo', (_message.Message,), {
    'DESCRIPTOR': _AUTHINFO,
    '__module__': 'entity_pb2'
    # @@protoc_insertion_point(class_scope:sa.rpc.entity.AuthInfo)
})
_sym_db.RegisterMessage(AuthInfo)

APIMessage = _reflection.GeneratedProtocolMessageType('APIMessage', (_message.Message,), {

    'HeaderEntry': _reflection.GeneratedProtocolMessageType('HeaderEntry', (_message.Message,), {
        'DESCRIPTOR': _APIMESSAGE_HEADERENTRY,
        '__module__': 'entity_pb2'
        # @@protoc_insertion_point(class_scope:sa.rpc.entity.APIMessage.HeaderEntry)
    })
    ,
    'DESCRIPTOR': _APIMESSAGE,
    '__module__': 'entity_pb2'
    # @@protoc_insertion_point(class_scope:sa.rpc.entity.APIMessage)
})
_sym_db.RegisterMessage(APIMessage)
_sym_db.RegisterMessage(APIMessage.HeaderEntry)

Subscription = _reflection.GeneratedProtocolMessageType('Subscription', (_message.Message,), {
    'DESCRIPTOR': _SUBSCRIPTION,
    '__module__': 'entity_pb2'
    # @@protoc_insertion_point(class_scope:sa.rpc.entity.Subscription)
})
_sym_db.RegisterMessage(Subscription)

GetStockQuoteSnapShotReq = _reflection.GeneratedProtocolMessageType('GetStockQuoteSnapShotReq', (_message.Message,), {
    'DESCRIPTOR': _GETSTOCKQUOTESNAPSHOTREQ,
    '__module__': 'entity_pb2'
    # @@protoc_insertion_point(class_scope:sa.rpc.entity.GetStockQuoteSnapShotReq)
})
_sym_db.RegisterMessage(GetStockQuoteSnapShotReq)

IndMISummary = _reflection.GeneratedProtocolMessageType('IndMISummary', (_message.Message,), {
    'DESCRIPTOR': _INDMISUMMARY,
    '__module__': 'entity_pb2'
    # @@protoc_insertion_point(class_scope:sa.rpc.entity.IndMISummary)
})
_sym_db.RegisterMessage(IndMISummary)

IndMISummaryList = _reflection.GeneratedProtocolMessageType('IndMISummaryList', (_message.Message,), {
    'DESCRIPTOR': _INDMISUMMARYLIST,
    '__module__': 'entity_pb2'
    # @@protoc_insertion_point(class_scope:sa.rpc.entity.IndMISummaryList)
})
_sym_db.RegisterMessage(IndMISummaryList)

IndDDSummary = _reflection.GeneratedProtocolMessageType('IndDDSummary', (_message.Message,), {
    'DESCRIPTOR': _INDDDSUMMARY,
    '__module__': 'entity_pb2'
    # @@protoc_insertion_point(class_scope:sa.rpc.entity.IndDDSummary)
})
_sym_db.RegisterMessage(IndDDSummary)

IndDDSummaryList = _reflection.GeneratedProtocolMessageType('IndDDSummaryList', (_message.Message,), {
    'DESCRIPTOR': _INDDDSUMMARYLIST,
    '__module__': 'entity_pb2'
    # @@protoc_insertion_point(class_scope:sa.rpc.entity.IndDDSummaryList)
})
_sym_db.RegisterMessage(IndDDSummaryList)

GetIndReq = _reflection.GeneratedProtocolMessageType('GetIndReq', (_message.Message,), {
    'DESCRIPTOR': _GETINDREQ,
    '__module__': 'entity_pb2'
    # @@protoc_insertion_point(class_scope:sa.rpc.entity.GetIndReq)
})
_sym_db.RegisterMessage(GetIndReq)

if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z\024sa-common/rpc/entity'
    _APIMESSAGE_HEADERENTRY._options = None
    _APIMESSAGE_HEADERENTRY._serialized_options = b'8\001'
    _VOID._serialized_start = 58
    _VOID._serialized_end = 64
    _BOOL._serialized_start = 66
    _BOOL._serialized_end = 87
    _STRING._serialized_start = 89
    _STRING._serialized_end = 112
    _STRINGLIST._serialized_start = 114
    _STRINGLIST._serialized_end = 142
    _BYTES._serialized_start = 144
    _BYTES._serialized_end = 166
    _INT64._serialized_start = 168
    _INT64._serialized_end = 190
    _INT64LIST._serialized_start = 192
    _INT64LIST._serialized_end = 219
    _INT32._serialized_start = 221
    _INT32._serialized_end = 243
    _INT32LIST._serialized_start = 245
    _INT32LIST._serialized_end = 272
    _TICKRECORD._serialized_start = 275
    _TICKRECORD._serialized_end = 492
    _ORDERRECORD._serialized_start = 495
    _ORDERRECORD._serialized_end = 666
    _ORDERQUEUERECORD._serialized_start = 669
    _ORDERQUEUERECORD._serialized_end = 891
    _STOCKQUOTERECORD._serialized_start = 894
    _STOCKQUOTERECORD._serialized_end = 1389
    _STOCKQUOTESNAPSHOT._serialized_start = 1392
    _STOCKQUOTESNAPSHOT._serialized_end = 1751
    _STOCKQUOTESNAPSHOTLIST._serialized_start = 1753
    _STOCKQUOTESNAPSHOTLIST._serialized_end = 1828
    _USER._serialized_start = 1830
    _USER._serialized_end = 1894
    _AUTHINFO._serialized_start = 1896
    _AUTHINFO._serialized_end = 1962
    _APIMESSAGE._serialized_start = 1965
    _APIMESSAGE._serialized_end = 2187
    _APIMESSAGE_HEADERENTRY._serialized_start = 2142
    _APIMESSAGE_HEADERENTRY._serialized_end = 2187
    _SUBSCRIPTION._serialized_start = 2190
    _SUBSCRIPTION._serialized_end = 2318
    _GETSTOCKQUOTESNAPSHOTREQ._serialized_start = 2320
    _GETSTOCKQUOTESNAPSHOTREQ._serialized_end = 2416
    _INDMISUMMARY._serialized_start = 2419
    _INDMISUMMARY._serialized_end = 3172
    _INDMISUMMARYLIST._serialized_start = 3174
    _INDMISUMMARYLIST._serialized_end = 3237
    _INDDDSUMMARY._serialized_start = 3240
    _INDDDSUMMARY._serialized_end = 3993
    _INDDDSUMMARYLIST._serialized_start = 3995
    _INDDDSUMMARYLIST._serialized_end = 4058
    _GETINDREQ._serialized_start = 4060
    _GETINDREQ._serialized_end = 4154
# @@protoc_insertion_point(module_scope)
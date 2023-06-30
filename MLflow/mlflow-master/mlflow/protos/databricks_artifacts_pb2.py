# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: databricks_artifacts.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2
from . import databricks_pb2 as databricks__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x64\x61tabricks_artifacts.proto\x12\x06mlflow\x1a\x15scalapb/scalapb.proto\x1a\x10\x64\x61tabricks.proto\"\xdf\x01\n\x16\x41rtifactCredentialInfo\x12\x0e\n\x06run_id\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x12\n\nsigned_uri\x18\x03 \x01(\t\x12:\n\x07headers\x18\x04 \x03(\x0b\x32).mlflow.ArtifactCredentialInfo.HttpHeader\x12,\n\x04type\x18\x05 \x01(\x0e\x32\x1e.mlflow.ArtifactCredentialType\x1a)\n\nHttpHeader\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x95\x02\n\x15GetCredentialsForRead\x12\x14\n\x06run_id\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x12\x0c\n\x04path\x18\x02 \x03(\t\x12\x12\n\npage_token\x18\x03 \x01(\t\x1a\x63\n\x08Response\x12\x38\n\x10\x63redential_infos\x18\x02 \x03(\x0b\x32\x1e.mlflow.ArtifactCredentialInfo\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\tJ\x04\x08\x01\x10\x02:_\xe2?(\n&com.databricks.rpc.RPC[$this.Response]\xe2?1\n/com.databricks.mlflow.api.MlflowTrackingMessage\"\x96\x02\n\x16GetCredentialsForWrite\x12\x14\n\x06run_id\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x12\x0c\n\x04path\x18\x02 \x03(\t\x12\x12\n\npage_token\x18\x03 \x01(\t\x1a\x63\n\x08Response\x12\x38\n\x10\x63redential_infos\x18\x02 \x03(\x0b\x32\x1e.mlflow.ArtifactCredentialInfo\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\tJ\x04\x08\x01\x10\x02:_\xe2?(\n&com.databricks.rpc.RPC[$this.Response]\xe2?1\n/com.databricks.mlflow.api.MlflowTrackingMessage\"\xd5\x02\n\x15\x43reateMultipartUpload\x12\x14\n\x06run_id\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x17\n\tnum_parts\x18\x03 \x01(\x03\x42\x04\xf8\x86\x19\x01\x1a\x9d\x01\n\x08Response\x12\x11\n\tupload_id\x18\x01 \x01(\t\x12?\n\x17upload_credential_infos\x18\x02 \x03(\x0b\x32\x1e.mlflow.ArtifactCredentialInfo\x12=\n\x15\x61\x62ort_credential_info\x18\x03 \x01(\x0b\x32\x1e.mlflow.ArtifactCredentialInfo:_\xe2?(\n&com.databricks.rpc.RPC[$this.Response]\xe2?1\n/com.databricks.mlflow.api.MlflowTrackingMessage\"-\n\x08PartEtag\x12\x13\n\x0bpart_number\x18\x01 \x01(\x03\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\"\xe9\x01\n\x17\x43ompleteMultipartUpload\x12\x14\n\x06run_id\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x17\n\tupload_id\x18\x03 \x01(\tB\x04\xf8\x86\x19\x01\x12$\n\npart_etags\x18\x04 \x03(\x0b\x32\x10.mlflow.PartEtag\x1a\n\n\x08Response:_\xe2?(\n&com.databricks.rpc.RPC[$this.Response]\xe2?1\n/com.databricks.mlflow.api.MlflowTrackingMessage\"\xa0\x02\n\x19GetPresignedUploadPartUrl\x12\x14\n\x06run_id\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x17\n\tupload_id\x18\x03 \x01(\tB\x04\xf8\x86\x19\x01\x12\x19\n\x0bpart_number\x18\x04 \x01(\x03\x42\x04\xf8\x86\x19\x01\x1aJ\n\x08Response\x12>\n\x16upload_credential_info\x18\x01 \x01(\x0b\x32\x1e.mlflow.ArtifactCredentialInfo:_\xe2?(\n&com.databricks.rpc.RPC[$this.Response]\xe2?1\n/com.databricks.mlflow.api.MlflowTrackingMessage*s\n\x16\x41rtifactCredentialType\x12\x11\n\rAZURE_SAS_URI\x10\x01\x12\x15\n\x11\x41WS_PRESIGNED_URL\x10\x02\x12\x12\n\x0eGCP_SIGNED_URL\x10\x03\x12\x1b\n\x17\x41ZURE_ADLS_GEN2_SAS_URI\x10\x04\x32\xe3\x06\n DatabricksMlflowArtifactsService\x12\x9c\x01\n\x15getCredentialsForRead\x12\x1d.mlflow.GetCredentialsForRead\x1a&.mlflow.GetCredentialsForRead.Response\"<\xf2\x86\x19\x38\n4\n\x04POST\x12&/mlflow/artifacts/credentials-for-read\x1a\x04\x08\x02\x10\x00\x10\x03\x12\xa0\x01\n\x16getCredentialsForWrite\x12\x1e.mlflow.GetCredentialsForWrite\x1a\'.mlflow.GetCredentialsForWrite.Response\"=\xf2\x86\x19\x39\n5\n\x04POST\x12\'/mlflow/artifacts/credentials-for-write\x1a\x04\x08\x02\x10\x00\x10\x03\x12\x9f\x01\n\x15\x63reateMultipartUpload\x12\x1d.mlflow.CreateMultipartUpload\x1a&.mlflow.CreateMultipartUpload.Response\"?\xf2\x86\x19;\n7\n\x04POST\x12)/mlflow/artifacts/create-multipart-upload\x1a\x04\x08\x02\x10\x00\x10\x03\x12\xa7\x01\n\x17\x63ompleteMultipartUpload\x12\x1f.mlflow.CompleteMultipartUpload\x1a(.mlflow.CompleteMultipartUpload.Response\"A\xf2\x86\x19=\n9\n\x04POST\x12+/mlflow/artifacts/complete-multipart-upload\x1a\x04\x08\x02\x10\x00\x10\x03\x12\xb0\x01\n\x19getPresignedUploadPartUrl\x12!.mlflow.GetPresignedUploadPartUrl\x1a*.mlflow.GetPresignedUploadPartUrl.Response\"D\xf2\x86\x19@\n<\n\x03GET\x12//mlflow/artifacts/get-presigned-upload-part-url\x1a\x04\x08\x02\x10\x00\x10\x03\x42,\n\x1f\x63om.databricks.api.proto.mlflow\x90\x01\x01\xa0\x01\x01\xe2?\x02\x10\x01')

_ARTIFACTCREDENTIALTYPE = DESCRIPTOR.enum_types_by_name['ArtifactCredentialType']
ArtifactCredentialType = enum_type_wrapper.EnumTypeWrapper(_ARTIFACTCREDENTIALTYPE)
AZURE_SAS_URI = 1
AWS_PRESIGNED_URL = 2
GCP_SIGNED_URL = 3
AZURE_ADLS_GEN2_SAS_URI = 4


_ARTIFACTCREDENTIALINFO = DESCRIPTOR.message_types_by_name['ArtifactCredentialInfo']
_ARTIFACTCREDENTIALINFO_HTTPHEADER = _ARTIFACTCREDENTIALINFO.nested_types_by_name['HttpHeader']
_GETCREDENTIALSFORREAD = DESCRIPTOR.message_types_by_name['GetCredentialsForRead']
_GETCREDENTIALSFORREAD_RESPONSE = _GETCREDENTIALSFORREAD.nested_types_by_name['Response']
_GETCREDENTIALSFORWRITE = DESCRIPTOR.message_types_by_name['GetCredentialsForWrite']
_GETCREDENTIALSFORWRITE_RESPONSE = _GETCREDENTIALSFORWRITE.nested_types_by_name['Response']
_CREATEMULTIPARTUPLOAD = DESCRIPTOR.message_types_by_name['CreateMultipartUpload']
_CREATEMULTIPARTUPLOAD_RESPONSE = _CREATEMULTIPARTUPLOAD.nested_types_by_name['Response']
_PARTETAG = DESCRIPTOR.message_types_by_name['PartEtag']
_COMPLETEMULTIPARTUPLOAD = DESCRIPTOR.message_types_by_name['CompleteMultipartUpload']
_COMPLETEMULTIPARTUPLOAD_RESPONSE = _COMPLETEMULTIPARTUPLOAD.nested_types_by_name['Response']
_GETPRESIGNEDUPLOADPARTURL = DESCRIPTOR.message_types_by_name['GetPresignedUploadPartUrl']
_GETPRESIGNEDUPLOADPARTURL_RESPONSE = _GETPRESIGNEDUPLOADPARTURL.nested_types_by_name['Response']
ArtifactCredentialInfo = _reflection.GeneratedProtocolMessageType('ArtifactCredentialInfo', (_message.Message,), {

  'HttpHeader' : _reflection.GeneratedProtocolMessageType('HttpHeader', (_message.Message,), {
    'DESCRIPTOR' : _ARTIFACTCREDENTIALINFO_HTTPHEADER,
    '__module__' : 'databricks_artifacts_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.ArtifactCredentialInfo.HttpHeader)
    })
  ,
  'DESCRIPTOR' : _ARTIFACTCREDENTIALINFO,
  '__module__' : 'databricks_artifacts_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ArtifactCredentialInfo)
  })
_sym_db.RegisterMessage(ArtifactCredentialInfo)
_sym_db.RegisterMessage(ArtifactCredentialInfo.HttpHeader)

GetCredentialsForRead = _reflection.GeneratedProtocolMessageType('GetCredentialsForRead', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _GETCREDENTIALSFORREAD_RESPONSE,
    '__module__' : 'databricks_artifacts_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.GetCredentialsForRead.Response)
    })
  ,
  'DESCRIPTOR' : _GETCREDENTIALSFORREAD,
  '__module__' : 'databricks_artifacts_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.GetCredentialsForRead)
  })
_sym_db.RegisterMessage(GetCredentialsForRead)
_sym_db.RegisterMessage(GetCredentialsForRead.Response)

GetCredentialsForWrite = _reflection.GeneratedProtocolMessageType('GetCredentialsForWrite', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _GETCREDENTIALSFORWRITE_RESPONSE,
    '__module__' : 'databricks_artifacts_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.GetCredentialsForWrite.Response)
    })
  ,
  'DESCRIPTOR' : _GETCREDENTIALSFORWRITE,
  '__module__' : 'databricks_artifacts_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.GetCredentialsForWrite)
  })
_sym_db.RegisterMessage(GetCredentialsForWrite)
_sym_db.RegisterMessage(GetCredentialsForWrite.Response)

CreateMultipartUpload = _reflection.GeneratedProtocolMessageType('CreateMultipartUpload', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _CREATEMULTIPARTUPLOAD_RESPONSE,
    '__module__' : 'databricks_artifacts_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.CreateMultipartUpload.Response)
    })
  ,
  'DESCRIPTOR' : _CREATEMULTIPARTUPLOAD,
  '__module__' : 'databricks_artifacts_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.CreateMultipartUpload)
  })
_sym_db.RegisterMessage(CreateMultipartUpload)
_sym_db.RegisterMessage(CreateMultipartUpload.Response)

PartEtag = _reflection.GeneratedProtocolMessageType('PartEtag', (_message.Message,), {
  'DESCRIPTOR' : _PARTETAG,
  '__module__' : 'databricks_artifacts_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.PartEtag)
  })
_sym_db.RegisterMessage(PartEtag)

CompleteMultipartUpload = _reflection.GeneratedProtocolMessageType('CompleteMultipartUpload', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _COMPLETEMULTIPARTUPLOAD_RESPONSE,
    '__module__' : 'databricks_artifacts_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.CompleteMultipartUpload.Response)
    })
  ,
  'DESCRIPTOR' : _COMPLETEMULTIPARTUPLOAD,
  '__module__' : 'databricks_artifacts_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.CompleteMultipartUpload)
  })
_sym_db.RegisterMessage(CompleteMultipartUpload)
_sym_db.RegisterMessage(CompleteMultipartUpload.Response)

GetPresignedUploadPartUrl = _reflection.GeneratedProtocolMessageType('GetPresignedUploadPartUrl', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _GETPRESIGNEDUPLOADPARTURL_RESPONSE,
    '__module__' : 'databricks_artifacts_pb2'
    # @@protoc_insertion_point(class_scope:mlflow.GetPresignedUploadPartUrl.Response)
    })
  ,
  'DESCRIPTOR' : _GETPRESIGNEDUPLOADPARTURL,
  '__module__' : 'databricks_artifacts_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.GetPresignedUploadPartUrl)
  })
_sym_db.RegisterMessage(GetPresignedUploadPartUrl)
_sym_db.RegisterMessage(GetPresignedUploadPartUrl.Response)

_DATABRICKSMLFLOWARTIFACTSSERVICE = DESCRIPTOR.services_by_name['DatabricksMlflowArtifactsService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037com.databricks.api.proto.mlflow\220\001\001\240\001\001\342?\002\020\001'
  _GETCREDENTIALSFORREAD.fields_by_name['run_id']._options = None
  _GETCREDENTIALSFORREAD.fields_by_name['run_id']._serialized_options = b'\370\206\031\001'
  _GETCREDENTIALSFORREAD._options = None
  _GETCREDENTIALSFORREAD._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]\342?1\n/com.databricks.mlflow.api.MlflowTrackingMessage'
  _GETCREDENTIALSFORWRITE.fields_by_name['run_id']._options = None
  _GETCREDENTIALSFORWRITE.fields_by_name['run_id']._serialized_options = b'\370\206\031\001'
  _GETCREDENTIALSFORWRITE._options = None
  _GETCREDENTIALSFORWRITE._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]\342?1\n/com.databricks.mlflow.api.MlflowTrackingMessage'
  _CREATEMULTIPARTUPLOAD.fields_by_name['run_id']._options = None
  _CREATEMULTIPARTUPLOAD.fields_by_name['run_id']._serialized_options = b'\370\206\031\001'
  _CREATEMULTIPARTUPLOAD.fields_by_name['num_parts']._options = None
  _CREATEMULTIPARTUPLOAD.fields_by_name['num_parts']._serialized_options = b'\370\206\031\001'
  _CREATEMULTIPARTUPLOAD._options = None
  _CREATEMULTIPARTUPLOAD._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]\342?1\n/com.databricks.mlflow.api.MlflowTrackingMessage'
  _COMPLETEMULTIPARTUPLOAD.fields_by_name['run_id']._options = None
  _COMPLETEMULTIPARTUPLOAD.fields_by_name['run_id']._serialized_options = b'\370\206\031\001'
  _COMPLETEMULTIPARTUPLOAD.fields_by_name['upload_id']._options = None
  _COMPLETEMULTIPARTUPLOAD.fields_by_name['upload_id']._serialized_options = b'\370\206\031\001'
  _COMPLETEMULTIPARTUPLOAD._options = None
  _COMPLETEMULTIPARTUPLOAD._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]\342?1\n/com.databricks.mlflow.api.MlflowTrackingMessage'
  _GETPRESIGNEDUPLOADPARTURL.fields_by_name['run_id']._options = None
  _GETPRESIGNEDUPLOADPARTURL.fields_by_name['run_id']._serialized_options = b'\370\206\031\001'
  _GETPRESIGNEDUPLOADPARTURL.fields_by_name['upload_id']._options = None
  _GETPRESIGNEDUPLOADPARTURL.fields_by_name['upload_id']._serialized_options = b'\370\206\031\001'
  _GETPRESIGNEDUPLOADPARTURL.fields_by_name['part_number']._options = None
  _GETPRESIGNEDUPLOADPARTURL.fields_by_name['part_number']._serialized_options = b'\370\206\031\001'
  _GETPRESIGNEDUPLOADPARTURL._options = None
  _GETPRESIGNEDUPLOADPARTURL._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]\342?1\n/com.databricks.mlflow.api.MlflowTrackingMessage'
  _DATABRICKSMLFLOWARTIFACTSSERVICE.methods_by_name['getCredentialsForRead']._options = None
  _DATABRICKSMLFLOWARTIFACTSSERVICE.methods_by_name['getCredentialsForRead']._serialized_options = b'\362\206\0318\n4\n\004POST\022&/mlflow/artifacts/credentials-for-read\032\004\010\002\020\000\020\003'
  _DATABRICKSMLFLOWARTIFACTSSERVICE.methods_by_name['getCredentialsForWrite']._options = None
  _DATABRICKSMLFLOWARTIFACTSSERVICE.methods_by_name['getCredentialsForWrite']._serialized_options = b'\362\206\0319\n5\n\004POST\022\'/mlflow/artifacts/credentials-for-write\032\004\010\002\020\000\020\003'
  _DATABRICKSMLFLOWARTIFACTSSERVICE.methods_by_name['createMultipartUpload']._options = None
  _DATABRICKSMLFLOWARTIFACTSSERVICE.methods_by_name['createMultipartUpload']._serialized_options = b'\362\206\031;\n7\n\004POST\022)/mlflow/artifacts/create-multipart-upload\032\004\010\002\020\000\020\003'
  _DATABRICKSMLFLOWARTIFACTSSERVICE.methods_by_name['completeMultipartUpload']._options = None
  _DATABRICKSMLFLOWARTIFACTSSERVICE.methods_by_name['completeMultipartUpload']._serialized_options = b'\362\206\031=\n9\n\004POST\022+/mlflow/artifacts/complete-multipart-upload\032\004\010\002\020\000\020\003'
  _DATABRICKSMLFLOWARTIFACTSSERVICE.methods_by_name['getPresignedUploadPartUrl']._options = None
  _DATABRICKSMLFLOWARTIFACTSSERVICE.methods_by_name['getPresignedUploadPartUrl']._serialized_options = b'\362\206\031@\n<\n\003GET\022//mlflow/artifacts/get-presigned-upload-part-url\032\004\010\002\020\000\020\003'
  _ARTIFACTCREDENTIALTYPE._serialized_start=1784
  _ARTIFACTCREDENTIALTYPE._serialized_end=1899
  _ARTIFACTCREDENTIALINFO._serialized_start=80
  _ARTIFACTCREDENTIALINFO._serialized_end=303
  _ARTIFACTCREDENTIALINFO_HTTPHEADER._serialized_start=262
  _ARTIFACTCREDENTIALINFO_HTTPHEADER._serialized_end=303
  _GETCREDENTIALSFORREAD._serialized_start=306
  _GETCREDENTIALSFORREAD._serialized_end=583
  _GETCREDENTIALSFORREAD_RESPONSE._serialized_start=387
  _GETCREDENTIALSFORREAD_RESPONSE._serialized_end=486
  _GETCREDENTIALSFORWRITE._serialized_start=586
  _GETCREDENTIALSFORWRITE._serialized_end=864
  _GETCREDENTIALSFORWRITE_RESPONSE._serialized_start=387
  _GETCREDENTIALSFORWRITE_RESPONSE._serialized_end=486
  _CREATEMULTIPARTUPLOAD._serialized_start=867
  _CREATEMULTIPARTUPLOAD._serialized_end=1208
  _CREATEMULTIPARTUPLOAD_RESPONSE._serialized_start=954
  _CREATEMULTIPARTUPLOAD_RESPONSE._serialized_end=1111
  _PARTETAG._serialized_start=1210
  _PARTETAG._serialized_end=1255
  _COMPLETEMULTIPARTUPLOAD._serialized_start=1258
  _COMPLETEMULTIPARTUPLOAD._serialized_end=1491
  _COMPLETEMULTIPARTUPLOAD_RESPONSE._serialized_start=387
  _COMPLETEMULTIPARTUPLOAD_RESPONSE._serialized_end=397
  _GETPRESIGNEDUPLOADPARTURL._serialized_start=1494
  _GETPRESIGNEDUPLOADPARTURL._serialized_end=1782
  _GETPRESIGNEDUPLOADPARTURL_RESPONSE._serialized_start=1611
  _GETPRESIGNEDUPLOADPARTURL_RESPONSE._serialized_end=1685
  _DATABRICKSMLFLOWARTIFACTSSERVICE._serialized_start=1902
  _DATABRICKSMLFLOWARTIFACTSSERVICE._serialized_end=2769
DatabricksMlflowArtifactsService = service_reflection.GeneratedServiceType('DatabricksMlflowArtifactsService', (_service.Service,), dict(
  DESCRIPTOR = _DATABRICKSMLFLOWARTIFACTSSERVICE,
  __module__ = 'databricks_artifacts_pb2'
  ))

DatabricksMlflowArtifactsService_Stub = service_reflection.GeneratedServiceStubType('DatabricksMlflowArtifactsService_Stub', (DatabricksMlflowArtifactsService,), dict(
  DESCRIPTOR = _DATABRICKSMLFLOWARTIFACTSSERVICE,
  __module__ = 'databricks_artifacts_pb2'
  ))


# @@protoc_insertion_point(module_scope)

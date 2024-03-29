# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: main.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='main.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nmain.proto\" \n\x10\x46ilePathDownload\x12\x0c\n\x04path\x18\x01 \x01(\t\"\x1f\n\x0e\x46ilePathUpload\x12\r\n\x05\x64path\x18\x01 \x01(\t2<\n\nDownloader\x12.\n\x08\x44ownload\x12\x11.FilePathDownload\x1a\x0f.FilePathUploadb\x06proto3'
)




_FILEPATHDOWNLOAD = _descriptor.Descriptor(
  name='FilePathDownload',
  full_name='FilePathDownload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='FilePathDownload.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=46,
)


_FILEPATHUPLOAD = _descriptor.Descriptor(
  name='FilePathUpload',
  full_name='FilePathUpload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dpath', full_name='FilePathUpload.dpath', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=79,
)

DESCRIPTOR.message_types_by_name['FilePathDownload'] = _FILEPATHDOWNLOAD
DESCRIPTOR.message_types_by_name['FilePathUpload'] = _FILEPATHUPLOAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FilePathDownload = _reflection.GeneratedProtocolMessageType('FilePathDownload', (_message.Message,), {
  'DESCRIPTOR' : _FILEPATHDOWNLOAD,
  '__module__' : 'main_pb2'
  # @@protoc_insertion_point(class_scope:FilePathDownload)
  })
_sym_db.RegisterMessage(FilePathDownload)

FilePathUpload = _reflection.GeneratedProtocolMessageType('FilePathUpload', (_message.Message,), {
  'DESCRIPTOR' : _FILEPATHUPLOAD,
  '__module__' : 'main_pb2'
  # @@protoc_insertion_point(class_scope:FilePathUpload)
  })
_sym_db.RegisterMessage(FilePathUpload)



_DOWNLOADER = _descriptor.ServiceDescriptor(
  name='Downloader',
  full_name='Downloader',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=81,
  serialized_end=141,
  methods=[
  _descriptor.MethodDescriptor(
    name='Download',
    full_name='Downloader.Download',
    index=0,
    containing_service=None,
    input_type=_FILEPATHDOWNLOAD,
    output_type=_FILEPATHUPLOAD,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DOWNLOADER)

DESCRIPTOR.services_by_name['Downloader'] = _DOWNLOADER

# @@protoc_insertion_point(module_scope)

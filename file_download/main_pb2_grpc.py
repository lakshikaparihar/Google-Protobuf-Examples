# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import main_pb2 as main__pb2


class DownloaderStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Download = channel.unary_unary(
                '/Downloader/Download',
                request_serializer=main__pb2.FilePathDownload.SerializeToString,
                response_deserializer=main__pb2.FilePathUpload.FromString,
                )


class DownloaderServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Download(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DownloaderServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Download': grpc.unary_unary_rpc_method_handler(
                    servicer.Download,
                    request_deserializer=main__pb2.FilePathDownload.FromString,
                    response_serializer=main__pb2.FilePathUpload.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Downloader', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Downloader(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Download(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Downloader/Download',
            main__pb2.FilePathDownload.SerializeToString,
            main__pb2.FilePathUpload.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
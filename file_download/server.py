from concurrent import futures
import grpc
import main_pb2
import main_pb2_grpc
import urllib.request
import os



class Downloader(main_pb2_grpc.DownloaderServicer):

    def Download(self, request, context):
        urllib.request.urlretrieve(request.fpath,request.fname)
        self.lpath = os.path.abspath(request.fname)
        return main_pb2.FilePathUpload(dpath=self.lpath)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    main_pb2_grpc.add_DownloaderServicer_to_server(Downloader(), server)
    server.add_insecure_port('[::]:5000')
    print("Starting port .....")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

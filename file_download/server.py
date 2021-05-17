from concurrent import futures
import grpc
import main_pb2
import main_pb2_grpc
import urllib.request
import os
import requests
from urllib.parse import urlparse
class Downloader(main_pb2_grpc.DownloaderServicer):

    def extract_name(self,url):
        p = urlparse(url)
        path = p.path[1:].split('/', 1)
        file_name = path[1] 
        return file_name , os.path.abspath(file_name)

    def Download(self, request, context):
        r = requests.get(request.path, allow_redirects=True)
        self.fname , self.lpath = self.extract_name(request.path)
        open(self.fname, 'wb').write(r.content)
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

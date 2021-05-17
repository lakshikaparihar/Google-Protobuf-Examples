from concurrent import futures
import grpc
import main_pb2
import main_pb2_grpc
import urllib.request
import os
from urllib.parse import urlparse
from google.cloud import storage


class Downloader(main_pb2_grpc.DownloaderServicer):

    def googleCloud(self,url):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "cosmic-envoy-313907-2fc47918d007.json"
        p = urlparse(url)
        path = p.path[1:].split('/', 1)
        bucket, file_path = path[0], path[1] 
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket)
        blob = bucket.blob(file_path)
        blob.download_to_filename(os.path.basename(file_path))
        return os.path.abspath(file_path)


    def Download(self, request, context):
        if request.fpath.startswith("https://storage.googleapis.com"):
            self.lpath=self.googleCloud(request.fpath)
        #urllib.request.urlretrieve(request.fpath,request.fname)
        #self.lpath = os.path.abspath(request.fname)
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

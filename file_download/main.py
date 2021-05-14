import main_pb2
import sys

file = main_pb2.filepathdownload();
file.path = input()
print(main_pb2.filepathupload(downloadpath=file.path))
details = main_pb2.filepathupload()
print(details.downloadpath)

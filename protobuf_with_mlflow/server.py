from concurrent import futures
import grpc
import main_pb2
import main_pb2_grpc
import os
import requests
from urllib.parse import urlparse
import pickle
#import mlflow
import joblib
#import mlflow.sklearn, mlflow.keras
#from mlflow.tracking import MlflowClient
#import keras

class Downloader(main_pb2_grpc.DownloaderServicer):

    def extract_name(self,url):
        p = urlparse(url)
        path = p.path[1:].split('/', 1)
        file_name = path[1] 
        return file_name , os.path.abspath(file_name)

    def load_model(self,url,serialization):
        self.fname,self.lpath  = self.extract_name(url)
        #print(repr(self.lpath).strip("'"))
        #print(self.lpath)
        infile = open(repr(self.lpath).strip("'"),'rb')
        if serialization.lower() == 'pickle':
            self.model = pickle.load(infile)
        elif serialization.lower() == 'joblib':
        	self.model = joblib.load(infile)
        ##elif serialization.lower() == 'h5py':
        ##    self.model = keras.models.load_model('./model.pkl')
        print ('Loaded Model')
        infile.close()
        #self.model="Lakshika"
        return self.model,self.fname
        
    def logModel(self,library, url, serialization,proid,modelName):
        model,modelName=self.load_model(url, serialization)
        '''dbpath = "sqlite:///"+proid+".db"
        mlflow.set_tracking_uri(dbpath)
        if library.lower() == 'sklearn':
            mlflow.sklearn.log_model (model, modelName,registered_model_name=modelName)
        elif library.lower() == 'keras':
            mlflow.keras.log_model (model, modelName,registered_model_name=modelName)
        client = MlflowClient()
        client.transition_model_version_stage(
        name=modelName,
        version=1,
        stage="Production"
        )'''
        print ('Logged model')
        return modelName
        
    def Download(self, request, context):
        r = requests.get(request.url, allow_redirects=True)
        self.lpath= self.logModel(request.variant,request.url,request.serialization,request.providerid,request.api_name)
        #self.fname , self.lpath = self.extract_name(request.path)
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

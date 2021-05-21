from concurrent import futures
import grpc
from requests import api
import main_pb2
import main_pb2_grpc
import os
import requests
from urllib.parse import urlparse
import pickle
import mlflow
import joblib
import mlflow.sklearn, mlflow.keras
from mlflow.tracking import MlflowClient
#import keras

class MlflowModelService(main_pb2_grpc.MlflowModelServiceServicer):

    def __init__(self):
        mlflow.set_tracking_uri("sqlite:///mlruns.db")
        

    DELIMITER = "_#_"

    def extract_name(self,url):

        # url shouldn't end with /
        self._print("Entering extract_name")
        p = urlparse(url)
        path = p.path[1:].split('/', 1)
        file_name = path[1] 
        # need to create a folder and delete after logging...................................
        # file handling in new class...................................download , log and file handling.............................
        return file_name , os.path.abspath(file_name)

    def load_model(self,url,serialization):

        # exception handling.......................................
        self._print("Entering Loadind Model")
        self.fname,self.lpath  = self.extract_name(url)
        infile = open(repr(self.lpath).strip("'"),'rb')

        #add in validation class ()......................................................
        if serialization.lower() == 'pickle':
            self.model = pickle.load(infile)
        elif serialization.lower() == 'joblib':
        	self.model = joblib.load(infile)

        ##elif serialization.lower() == 'h5py':
        ##    self.model = keras.models.load_model('./model.pkl')
        self._print ('Loaded Model')
        infile.close()
        return self.model,self.fname
        
    def _print(self,str):
        print(str)

    
    def logModel(self,variant, url, serialization,provider_id,api_id):
        
        self._print("Entering Loging model")
        model,modelName=self.load_model(url, serialization)

        # can we avoid setting experiment id ?????????
        mlflow.set_experiment(provider_id)
        registered_model_name =provider_id+self.DELIMITER+api_id+self.DELIMITER+variant
        self._print("Registerd Model Name : "+registered_model_name)

        with mlflow.start_run():
            active_run = mlflow.active_run()
            print("Active run_id: {}".format(active_run.info.run_id))
            if variant.lower() == 'sklearn':
                mlflow.sklearn.log_model (model, registered_model_name,registered_model_name=registered_model_name)
            elif variant.lower() == 'keras':
                mlflow.keras.log_model (model, registered_model_name,registered_model_name=registered_model_name)

        return registered_model_name, active_run.info.run_id
        
    def validate(self,variant,variant_version,serialization,serialization_version,model):
        pass

    def DownloadAndStore(self, request, context):

        # add exception handling ..............................................................
        print("Entering the DownloadAndStore function")
        
        #need to test.....................
        r = requests.get(request.download_url, allow_redirects=True)
        self.fname,self.lpath  = self.extract_name(request.download_url)
        open(self.fname, 'wb').write(r.content)

        #validating the data
        self.validate(request.metadata.variant , request.metadata.variant_version,request.metadata.serialization_library,request.metadata.serialization_version,r)

        # logging and storing in mlflow
        self.modelname,self.runid= self.logModel(request.metadata.variant,request.download_url,request.metadata.serialization_library,request.user_id,request.api_id)
        print("Finally returning the value")



        return main_pb2.StoreModelResponse(model_name=self.modelname,run_id=self.runid)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=50))
    main_pb2_grpc.add_MlflowModelServiceServicer_to_server(MlflowModelService(),server)
    server.add_insecure_port('[::]:7000')
    print("Starting port .....")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

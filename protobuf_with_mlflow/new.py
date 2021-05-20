import pickle
import mlflow
import mlflow.sklearn

infile = open('finalized_model.pkl','rb')
model = pickle.load(infile)
print ('Loaded Model')
infile.close()

mlflow.set_tracking_uri("sqlite:///mlruns.db")
Experiment_id = mlflow.set_experiment("abc")
with mlflow.start_run(run_name="abcd",experiment_id=Experiment_id):
    run = mlflow.active_run()
    print("Active run_id: {}".format(run.info.run_id))
    mlflow.sklearn.log_model (model, "another-model")
print ('Logged another model')
#print(mlflow.active_run().info.run_id)

#model_uri = "runs:/{}/sklearn-model".format(run.info.run_id)
#mv = mlflow.register_model(model_uri, "RandomForestRegressionModel")
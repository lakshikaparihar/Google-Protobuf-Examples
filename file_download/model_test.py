import pickle
import pandas as pd
with open(r"finalized_model.pkl", "rb") as input_file:
    model = pickle.load(input_file)
data = {
  "preg": [10, 0],
  "plas": [101, 137],
  "pres": [76, 40],
  "skin": [48, 35],
  "test": [180, 168],
  "mass": [32.9, 43.1],
  "pedi": [0.171, 2.288],
  "age": [63, 33]
}

pandas_df = pd.DataFrame (data)
print(model.predict(pandas_df))
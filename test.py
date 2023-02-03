# %%
import pandas as pd

df = pd.read_csv('./model/fashion-mnist-train-1.csv', nrows=1)

# %%
array = df.drop("label", axis=1).values.reshape(28, 28)
array = array/255
array = array.tolist()

# %%
import requests
import json

im = array

data = {'image': im}
def predict():
    result = requests.post('http://127.0.0.1:5000/predict', json.dumps(data))
    print("Réponse : ", result.text)
if __name__ == '__main__':
    predict()



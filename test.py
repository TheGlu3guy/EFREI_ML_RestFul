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

data = {'image': array}
def classify():
    result = requests.post('http://127.0.0.1:5000/classify', json.dumps(data))
    print(result)
    print("Réponse : ", result.text)
if __name__ == '__main__':
    classify()



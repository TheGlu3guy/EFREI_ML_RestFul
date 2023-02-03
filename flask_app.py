from flask import Flask, request, jsonify
import numpy as np
from tensorflow import keras

app = Flask(__name__)

import os
print(os.listdir("."))

id2class = {0: "T-shirt/top",
                1: "Trouser",
                2: "Pullover",
                3: "Dress",
                4: "Coat",
                5: "Sandal",
                6: "Shirt",
                7: "Sneaker",
                8: "Bag",
                9: "Ankle boot", }
model = keras.models.load_model("./model/fashion_mnist")

@app.route('/classify', methods=['POST'])
def predict():
    img = np.array(request.get_json(force=True)['image']).astype("float32")
    img = np.expand_dims(img, -1)[None]
    return id2class[np.argmax(model.predict(img))]
if __name__ == '__main__':
    app.run(host='0.0.0.0')
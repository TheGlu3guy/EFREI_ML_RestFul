import json
import unittest
from flask_app import app
import pandas as pd

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_classify(self):
        with app.test_client() as client:
            df = pd.read_csv('./model/fashion-mnist-train-1.csv', nrows=1)
            
            array = df.drop("label", axis=1).values.reshape(28, 28)
            array = array/255
            array = array.tolist()

            result = client.post(
                '/classify',
                data={'image': array}
            )
            self.assertEqual(
                type(result.data),
                b'Ankle boot'
            )

if __name__ == '__main__':
    unittest.main()
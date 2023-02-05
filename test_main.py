import json
import unittest
from flask_app import app
import pandas as pd

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_classify(self):
        df = pd.read_csv('./model/fashion-mnist-train-1.csv', nrows=1)
            
        array = df.drop("label", axis=1).values.reshape(28, 28)
        array = array/255
        array = array.tolist()
        
        response = self.app.post('/classify', data = json.dumps({ 'image': array }))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Shirt')

if __name__ == '__main__':
    unittest.main()
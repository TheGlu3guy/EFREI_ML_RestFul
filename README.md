Steps to use the project:

- build the docker : docker build -t fashion_mnist .
- run the docker : docker run -d -p 5000:5000 --name=fmn fashion_mnist
- run the test : python -m unittest

Files : 
- flask_app.py : the flask app
- mo
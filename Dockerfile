FROM python:3.9
WORKDIR /usr/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY flask_app.py .
COPY model/fashion_mnist.h5 ./model/fashion_mnist.h5
EXPOSE 5000
CMD ["python","flask_app.py"]
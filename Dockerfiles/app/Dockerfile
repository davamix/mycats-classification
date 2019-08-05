FROM tensorflow/tensorflow:2.0.0b1-py3

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install -r ./requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]
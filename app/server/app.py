import sys
sys.path.insert(1, './model')

from flask import Flask
from flask_restful import Resource, Api
from flask import request

from tensorflow.keras.models import load_model
from metrics import MCC_binary
import numpy as np

app = Flask(__name__)
api = Api(app)

labels = ['Blacky', 'Niche']

def init():
    global model
    model = load_model('./model/fp16.h5', custom_objects={'MCC_binary': MCC_binary})

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, world!'

@app.route('/predict', methods=['POST'])
def prediction():
    req_data = request.json

    data = np.array(req_data['data'])

    predictions = model.predict_classes(data, batch_size=len(data))
    
    pred = labels[predictions[0]]

    app.logger.info("#### PREDICTION #### ")
    app.logger.info(pred)

    return pred

if __name__ == '__main__':
    init()
    app.run(threaded=True, debug=True, host='0.0.0.0')
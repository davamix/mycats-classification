import sys
sys.path.insert(1, './model')

from flask import Flask
from flask_restful import Resource, Api
from flask import request

from tensorflow.keras.models import load_model
from metrics import MCC_binary

app = Flask(__name__)
api = Api(app)

app.logger.info("Loading model...")
#model = load_model('./model/fp16.h5', custom_objects={'MCC_binary': MCC_binary})
app.logger.info("Model fp16 loaded.")

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, world 2!'

@app.route('/predict', methods=['POST'])
def prediction():
    req_data = request.get_json()

    data = req_data['data']

    app.logger.info(data)

    #predictions = model.predict_classes(data)
    
    return data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
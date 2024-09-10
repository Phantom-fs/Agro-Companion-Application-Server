from flask import Flask, request, jsonify
from flask_cors import CORS

import requests

from files_app.torch_utils import prediction, preprocess

app = Flask(__name__)

# enable CORS
CORS(app) # UPDATE IT TO WEBSITE URL

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return "<p>Soil Classification and Crop Recommendation</p>"

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files.get('file')
        if file is None or file.filename == "":
            return jsonify({'error': 'no file'})
        if not allowed_file(file.filename):
            return jsonify({'error': 'format not supported'})

        try:
            img_bytes = file.read()
            
            # preprocess the image
            tensor = preprocess(img_bytes)
            
            # get the top 3 predictions
            top3_labels, top3 = prediction(tensor)
            data = {'class_labels': top3_labels, 'probabilities': top3}
            
            return jsonify(data)
        except:
            return jsonify({'error': 'error during prediction'})

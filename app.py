from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import os

app = Flask(__name__)
CORS(app)  # <-- IMPORTANT for Android app requests

# Load model
model = pickle.load(open("crop_recommendation_model.pkl", "rb"))

@app.route('/')
def home():
    return "🌾 Crop Recommendation API is Running Successfully!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    N = data['N']
    P = data['P']
    K = data['K']
    temperature = data['temperature']
    humidity = data['humidity']
    ph = data['ph']
    rainfall = data['rainfall']

    prediction = model.predict([[N, P, K, temperature, humidity, ph, rainfall]])
    return jsonify({'recommended_crop': prediction[0]})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # IMPORTANT: debug must be False and host must be 0.0.0.0
    app.run(debug=False, host="0.0.0.0", port=port)

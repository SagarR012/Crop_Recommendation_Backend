from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import os

app = Flask(__name__)
CORS(app)  # Allow Android app to call this API

# Load model
model = pickle.load(open("crop_recommendation_model.pkl", "rb"))

@app.route('/')
def home():
    return "🌾 Crop Recommendation API is Running Successfully!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Read input values
        N = float(data['N'])
        P = float(data['P'])
        K = float(data['K'])
        temperature = float(data['temperature'])
        humidity = float(data['humidity'])
        ph = float(data['ph'])
        rainfall = float(data['rainfall'])

        # 1) Prepare features
        features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

        # 2) Get probabilities for all crops
        probs = model.predict_proba(features)[0]      # e.g. [0.1, 0.7, 0.2, ...]
        crops = model.classes_                        # e.g. ['rice','maize','mothbeans',...]

        # 3) Take top-3 indices (highest probability)
        top3_idx = probs.argsort()[-3:][::-1]        # last 3, reversed (max → min)

        top3 = []
        for idx in top3_idx:
            top3.append({
                "crop": str(crops[idx]),
                "confidence": round(float(probs[idx] * 100), 2)  # percentage
            })

        # Best crop for backward compatibility
        best_crop = top3[0]["crop"]

        return jsonify({
            "recommended_crop": best_crop,   # old key (if Android still uses it)
            "top3_crops": top3               # new detailed info
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # IMPORTANT: debug must be False and host must be 0.0.0.0 for Railway
    app.run(debug=False, host="0.0.0.0", port=port)

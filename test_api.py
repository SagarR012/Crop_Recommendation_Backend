import requests

# 🌐 Your public ngrok URL
url = "https://submaniacally-hypercomposite-aubree.ngrok-free.dev/predict"

# 🧾 Example data (you can change these numbers)
data = {
    "N": 90,
    "P": 42,
    "K": 43,
    "temperature": 25.5,
    "humidity": 80.2,
    "ph": 6.5,
    "rainfall": 200.0
}

# 🚀 Send POST request
response = requests.post(url, json=data)

# 📊 Print the result
print("✅ Status Code:", response.status_code)
print("🌾 Prediction Result:", response.json())

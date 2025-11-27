import requests

url = "https://croprecommendationbackend-production.up.railway.app/predict"

data = {
    "N": 90,
    "P": 42,
    "K": 43,
    "temperature": 20,
    "humidity": 80,
    "ph": 6.5,
    "rainfall": 200
}

try:
    r = requests.post(url, json=data, timeout=20)
    print("Status:", r.status_code)
    print("Response:", r.text)
except Exception as e:
    print("ERROR:", e)

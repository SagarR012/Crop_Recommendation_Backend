@echo off
cd /d "C:\Users\Sagar R\OneDrive\Attachments\Desktop\Crop_Recommendation_Backend"

start "" cmd /k "python app.py"
start "" cmd /k "ngrok http 5000"

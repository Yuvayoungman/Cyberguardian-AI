## 🔗 Live Demo
https://cyberguardian-ai-demo.netlify.app

## 🧠 Gemini Integration
CyberGuardian AI integrates Google Gemini 3 Flash as the AI reasoning layer for phishing detection and explainable security analysis.  
The public demo runs in simulation mode due to Gemini API quota limits, while the Gemini-powered backend is fully implemented and tested locally.

## 🚀 How to Run Locally
### Backend
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload

### Frontend
cd frontend
python -m http.server 5500

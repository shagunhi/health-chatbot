from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import json

app = FastAPI()

# ✅ Allow all CORS (for ngrok / localtunnel)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Load your dataset (replace filename)
try:
    diseases_df = pd.read_csv("diseases.csv")
except Exception:
    diseases_df = pd.DataFrame(columns=["Disease", "Symptoms", "Description"])

@app.post("/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    user_message = data.get("message", "").lower()

    if not user_message:
        return {"response": "Please type something so I can help you."}

    # --- Match disease name ---
    for _, row in diseases_df.iterrows():
        disease_name = str(row.get("Disease", "")).lower()
        if disease_name in user_message:
            desc = str(row.get("Description", "No description available."))
            return {"response": f"Here's what I found about {disease_name.title()}: {desc}"}

    # --- Keyword-based fallback replies ---
    if "fever" in user_message:
        return {"response": "Fever can be due to infection. Stay hydrated, rest, and consult a doctor if it lasts 3+ days."}
    if "cold" in user_message:
        return {"response": "For cold: drink warm fluids, rest, and take steam inhalation."}
    if "headache" in user_message:
        return {"response": "Headache could be from stress or dehydration. Drink water and rest."}
    if "heart" in user_message:
        return {"response": "Heart disease prevention: healthy diet, regular exercise, no smoking, manage stress."}

    return {"response": "I'm not sure about that symptom. Please try another health query!"}

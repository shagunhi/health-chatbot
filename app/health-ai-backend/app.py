from fastapi import FastAPI
import pandas as pd
import os
import json
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# Allow frontend (React, Vue, etc.) to call the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # <-- allows all domains; use specific domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Path to the dataset folder
DATA_PATH = os.path.join(os.path.dirname(__file__), "dataset")
datasets = {}

# Load all CSV and JSON files at startup
for file in os.listdir(DATA_PATH):
    file_path = os.path.join(DATA_PATH, file)

    if file.endswith(".csv"):
        try:
            df = pd.read_csv(file_path, on_bad_lines="skip", engine="python")
            datasets[file.replace(".csv", "")] = df
            print(f"✅ Loaded CSV: {file} ({len(df)} rows)")   
        except Exception as e:
            print(f"❌ Error reading {file}: {e}")

            print(f"✅ Loaded CSV: {file}")

    elif file.endswith(".json"):
        with open(file_path, "r", encoding="utf-8") as f:
            datasets[file.replace(".json", "")] = json.load(f)
        print(f"✅ Loaded JSON: {file}")
        
@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/")
def home():
    return {"message": "Health AI backend running successfully 🚀"}

@app.get("/datasets")
def list_datasets():
    """List all dataset names"""
    return {"available_datasets": list(datasets.keys())}

@app.get("/data/{dataset_name}")
def get_dataset(dataset_name: str):

    """Return first few rows or JSON content"""
    if dataset_name not in datasets:
        return {"error": "Dataset not found"}

    data = datasets[dataset_name]

    if isinstance(data, pd.DataFrame):
        # For CSV: show first 5 rows
        return data.head().to_dict(orient="records")
    else:
        # For JSON: return as-is
        return data

from fastapi import Request

@app.post("/chat")
async def chat_endpoint(request: Request):
    """Chatbot that responds using your symptom/disease CSVs"""
    data = await request.json()
    user_message = data.get("message", "").lower().strip()

    reply = None

    # 1️⃣ Search "symptom_Description[1].csv"
    desc_data = datasets.get("symptom_Description[1]")
    if isinstance(desc_data, pd.DataFrame):
        for _, row in desc_data.iterrows():
            disease = str(row.get("Disease", "")).lower()
            description = str(row.get("Description", "")).strip()
            if disease in user_message:
                reply = f"🩺 {disease.title()}: {description}"
                break

    # 2️⃣ Search "symptom_precaution[1].csv" if no match
    if not reply:
        precaution_data = datasets.get("symptom_precaution[1]")
        if isinstance(precaution_data, pd.DataFrame):
            for _, row in precaution_data.iterrows():
                disease = str(row.get("Disease", "")).lower()
                p1 = str(row.get("Precaution_1", ""))
                p2 = str(row.get("Precaution_2", ""))
                p3 = str(row.get("Precaution_3", ""))
                p4 = str(row.get("Precaution_4", ""))
                if disease in user_message:
                    reply = (
                        f"💡 Precautions for {disease.title()}:\n"
                        f"1️⃣ {p1}\n2️⃣ {p2}\n3️⃣ {p3}\n4️⃣ {p4}"
                    )
                    break

    # 3️⃣ If still not found, try some keywords
    if not reply:
        if "fever" in user_message:
            reply = "Fever can be due to infection. Rest, hydrate, and consult a doctor if it persists."
        elif "cold" in user_message:
            reply = "Common cold: stay warm, hydrated, and take rest."
        elif "cough" in user_message:
            reply = "Cough may be from allergies or infection. Try warm fluids and rest."
        elif "heart" in user_message:
            reply = "To prevent heart disease: eat healthy, exercise, avoid smoking."
        else:
            reply = "I'm not sure I found that disease. Please rephrase or mention a specific symptom."

    return {"response": reply}


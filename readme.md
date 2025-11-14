# 🏥 HealthSaathi – Your AI Health Assistant

> An AI-powered health assistant built with **FastAPI**, **MongoDB**, **HTML**, **CSS**, and **JavaScript** that helps users understand diseases, symptoms, and preventive health measures — all through an intuitive chatbot interface.

---

## 🌟 Overview

**HealthSaathi** is a personal health assistant designed to:
- Help users identify diseases based on symptoms  
- Provide detailed information on **symptoms**, **causes**, and **precautions**
- Offer **daily health tips** for a better lifestyle  
- Serve as a foundation for future integration with **WhatsApp** or **SMS alerts**

This system is lightweight, fast, and scalable — ideal for students, clinics, or hackathon projects.

---

## 🧩 Features

### 💬 Chatbot Page
- Smart chatbot interface where users can ask:
  - “What are the symptoms of diabetes?”
  - “I have fever and headache”
  - “Tell me precautions for flu”
- Responds with detailed, pre-trained information.
- Can connect to real **datasets (CSV/JSON)** or MongoDB for dynamic responses.

### 🧬 Diseases Page
- Displays a chart/list of diseases from a dataset.
- Each entry includes:
  - **Description**
  - **Common Symptoms**
  - **Preventive Measures**
- Easy to extend with new datasets or API connections.

### 💡 Health Tips Page
- Provides curated daily health & lifestyle tips.
- Examples:
  - “Drink 2L of water daily”
  - “Sleep at least 7 hours”
  - “Avoid processed food”

### 🏠 Home Page
- Clean landing page introducing **HealthSaathi** and navigation to all sections.

---

## ⚙️ Tech Stack

| Layer | Technology Used |
|-------|-----------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | FastAPI (Python) |
| **Database** | MongoDB Atlas |
| **Libraries** | `pandas`, `pymongo`, `python-dotenv` |
| **Server Test Tool** | `Uvicorn` |
| **(Optional)** | `Ngrok` for public tunnel access |

---

## 🧠 Project Architecture

Frontend (HTML/CSS/JS)  
↓  
FastAPI Backend (Python)  
↓  
MongoDB Atlas / Local Dataset  


**Flow:**
1. User sends query via chatbot (frontend).
2. FastAPI processes message, matches keywords/symptoms.
3. Returns detailed disease info or health advice.
4. Chatbot displays the response dynamically.

---

## 🚀 Getting Started

### 🔹 Clone the Repository
```bash
git clone https://github.com/your-username/HealthSaathi.git
cd HealthSaathi

cd health-ai-backend
pip install -r requirements.txt

MONGO_URI = your_mongodb_connection_string
DB_NAME = health_ai

uvicorn app:app --reload

Server runs at 👉 `http://127.0.0.1:8000`

---

### 🔹 Frontend Setup
Simply open the `chatbot.html` (or `index.html`) file in your browser.

Make sure your backend is running before using the chatbot.  
If you’re using a local setup:
```js
const API_BASE = "http://127.0.0.1:8000";

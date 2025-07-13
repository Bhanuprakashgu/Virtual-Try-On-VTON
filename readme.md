# 👗 Virtual-Try-On-VTON

A lightweight Flask-based API for virtual try-on, built on top of the [TryOnDiffusion](https://github.com/DeepFashion3D/TryOnDiffusion) model. This project lets users overlay garments on a person image in a realistic, AI-generated manner.

> 👨‍💻 **Credits:** Integrated and adapted by **Bhanu Prakash Guddeti**

---

## 🚀 Features

- 🧍 Upload a **person** and **garment** image to see a virtual try-on result  
- ⚡ Fast and simple **API** for generating **AI-powered outfit previews**
- 💻 Works on **CPU** and **GPU** (GPU recommended for speed)
- 🧼 Built-in **image preprocessing** and **pose generation**

---

## 📦 Project Structure

Virtual-Try-On-VTON/
│
├── tryondiffusion_flask/
│ ├── src/
│ │ ├── main.py # Entry point
│ │ └── routes/
│ │ └── tryon.py # Core API logic
│ └── tryondiffusion/ # Original TryOnDiffusion code (unmodified)
├── static/ # Static assets (if any)
├── templates/ # Optional web frontend
└── README.md

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 📥 1. Clone the Repository

```bash
git clone https://github.com/your-username/Virtual-Try-On-VTON.git
cd Virtual-Try-On-VTON
🛠 2. Create a Virtual Environment
bash
python -m venv ven1
venv\Scripts\activate  # On Windows
📦 3. Install Dependencies
bash
pip install -r requirements.txt
🧪 Run the API Server
bash
cd tryondiffusion_flask/src
python main.py
📡 The Flask server will be available at:
http://127.0.0.1:5000

🧵 Try-On API Usage
📌 Endpoint
bash
POST /api/tryon
🧾 JSON Payload
json
{
  "person_image": "data:image/png;base64,...",
  "garment_image": "data:image/png;base64,..."
}
📤 JSON Response
json
{
  "success": true,
  "result_image": "data:image/png;base64,...",
  "message": "Try-on generated successfully using TryOnDiffusion"
}
✅ Health Check
Ping the server to verify it's running:

bash
GET /api/health
💡 Notes
🎯 Dummy pose estimation is used for simplicity

⚙️ The model is lightweight and works on CPU, but a GPU will significantly boost performance

🧳 The original TryOnDiffusion codebase is bundled as-is to ensure full functionality

👨‍🎓 Author
Bhanu Prakash Guddeti
Developer and integrator of the Virtual-Try-On-VTON API.
Feel free to reach out for queries, feedback, or collaboration.

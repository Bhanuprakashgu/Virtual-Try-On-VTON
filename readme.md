👗 TryOnDiffusion Flask API
A lightweight Flask-based API for virtual try-on, built on top of the TryOnDiffusion model. This project lets users overlay garments on a person image in a realistic, AI-generated manner.

👨‍💻 Credits: Integrated and adapted by Bhanu Prakash Guddeti

🚀 Features
Upload a person and garment image to see a try-on result

Fast and simple API for generating AI-powered outfit previews

Works on CPU and GPU (GPU recommended for speed)

Built-in image preprocessing and pose generation

📦 Project Structure
csharp
Copy
Edit
tryondiffusion_flask_app/
│
├── tryondiffusion_flask/
│   ├── src/
│   │   ├── main.py                # Entry point
│   │   └── routes/
│   │       └── tryon.py           # Core API logic
│   └── tryondiffusion/            # Original TryOnDiffusion code (unmodified)
├── static/                        # Static assets (if any)
├── templates/                     # Optional web frontend
└── README.md
⚙️ Setup Instructions
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/tryondiffusion_flask_app.git
cd tryondiffusion_flask_app
2. Create a virtual environment
bash
Copy
Edit
python -m venv ven1
venv\Scripts\activate  # On Windows
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
🧪 Run the API Server
bash
Copy
Edit
cd tryondiffusion_flask/src
python main.py
The Flask server will start at: http://127.0.0.1:5000

🧵 Try-On API Usage
Endpoint
bash
Copy
Edit
POST /api/tryon
JSON Payload
json
Copy
Edit
{
  "person_image": "data:image/png;base64,...",
  "garment_image": "data:image/png;base64,..."
}
JSON Response
json
Copy
Edit
{
  "success": true,
  "result_image": "data:image/png;base64,...",
  "message": "Try-on generated successfully using TryOnDiffusion"
}
✅ Health Check
Ping the server to check model/device status:

bash
Copy
Edit
GET /api/health
💡 Notes
Dummy pose estimation is used for simplicity.

Model is lightweight and runs on CPU, though GPU will improve performance.

The original TryOnDiffusion codebase is bundled as-is to preserve full functionality.

👨‍🎓 Author
Bhanu Prakash Guddeti
Developer and integrator of this API.
Feel free to reach out for queries, feedback, or collaboration.


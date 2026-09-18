Haan bhai 😭 **sirf README ke liye ye poora block copy-paste karna hai**. `README.md` mein jo bhi hai, **Ctrl+A → delete → ye paste**:

````markdown
# 🩺 Medical Chatbot

A voice and vision based AI medical assistant built using Python, Groq, Gradio, and gTTS.

The application allows users to describe their symptoms using voice and optionally upload a medical image. The system converts the patient's voice into text, analyzes the symptoms and image using an AI model, and generates a concise response that can also be converted back into speech.

## ✨ Features

- Voice-based symptom input
- Speech-to-text using Groq Whisper
- Medical image analysis
- AI-powered response generation
- Text-to-speech using gTTS
- Interactive Gradio web interface
- API keys stored securely using `.env`
- Modular Python code structure

## 🔄 How It Works

```text
Patient Voice
      ↓
Speech-to-Text
      ↓
Patient Symptoms + Medical Image
      ↓
AI Analysis
      ↓
Doctor Response
      ↓
Text-to-Speech
      ↓
Voice Response
````

## 🛠️ Technologies Used

* Python
* Gradio
* Groq API
* Whisper Large V3
* Qwen
* gTTS
* python-dotenv
* FFmpeg

## 📁 Project Structure

```text
MEDICAL CHATBOT/
│
├── app.py
├── brain.py
├── voice_of_patient.py
├── voice_of_doctor.py
├── acne.png
├── requirements.txt
├── .gitignore
└── .env
```

| File                  | Purpose                                                  |
| --------------------- | -------------------------------------------------------- |
| `app.py`              | Main Gradio application                                  |
| `brain.py`            | Image encoding and AI image analysis                     |
| `voice_of_patient.py` | Audio recording and speech-to-text                       |
| `voice_of_doctor.py`  | Text-to-speech functionality                             |
| `requirements.txt`    | Python dependencies                                      |
| `.env`                | API keys and environment variables                       |
| `.gitignore`          | Prevents sensitive/unnecessary files from being uploaded |

# ▶️ How to Run

## 1. Clone the Repository

```bash
git clone https://github.com/divyantks/Medical-Chatbot.git
cd Medical-Chatbot
```

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

## 3. Activate the Virtual Environment

### Windows PowerShell

```powershell
.\venv\Scripts\activate
```

## 4. Install Required Packages

```powershell
pip install -r requirements.txt
```

## 5. Install FFmpeg

FFmpeg is required for audio processing.

On Windows:

```powershell
winget install Gyan.FFmpeg
```

After installation, restart the terminal and verify:

```powershell
ffmpeg -version
```

## 6. Add Your Groq API Key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Do not upload the `.env` file to GitHub.

## 7. Run the Application

Make sure the virtual environment is activated:

```powershell
python app.py
```

The application will start locally.

Open the Gradio URL shown in the terminal, usually:

```text
http://127.0.0.1:7860
```

## 8. Using the Application

1. Allow microphone access.
2. Record your symptoms.
3. Upload a medical image if required.
4. Click **Analyze**.
5. Your voice is converted into text.
6. The AI analyzes the symptoms and image.
7. The response is displayed.
8. The response is converted into speech.

## ⚠️ Disclaimer

This project is developed for educational and learning purposes only.

It is not intended to provide professional medical diagnosis, treatment, or medical advice. AI-generated responses may be inaccurate. Always consult a qualified healthcare professional for medical concerns.

## 🚧 Future Improvements

* Conversation history
* Patient and doctor profiles
* Database integration
* Medical knowledge base / RAG
* Improved medical safety and response validation
* Better UI customization
* Cloud deployment
* Authentication
* Multi-language support

## 👨‍💻 Author

**Divyant**

GitHub: [https://github.com/divyantks](https://github.com/divyantks)

````




AI Video Assistant
An AI-powered video assistant that converts YouTube videos into structured and actionable information.

The application downloads audio from a YouTube video, transcribes it using OpenAI Whisper, and processes the transcript using Mistral AI through LangChain.

It can generate:

Video / meeting title

Concise summary

Action items

Key decisions

Open questions

Features
YouTube URL support

Automatic audio extraction using yt-dlp

Audio chunking using pydub

Local speech-to-text transcription using OpenAI Whisper

AI-powered summarization

Automatic title generation

Action item extraction

Key decision extraction

Open question extraction

Environment variable based API key management

Modular Python architecture

Tech Stack
Python

OpenAI Whisper

Mistral AI

LangChain

yt-dlp

pydub

python-dotenv

Architecture
YouTube URL
     |
     v
+---------------+
|    yt-dlp     |
| Audio Extract |
+-------+-------+
        |
        v
+---------------+
|     pydub     |
|Audio Chunking |
+-------+-------+
        |
        v
+---------------+
|    Whisper    |
| Transcription |
+-------+-------+
        |
        v
    Transcript
        |
        v
+--------------------------+
|        Mistral AI        |
+--------------------------+
| - Title Generation       |
| - Summarization          |
| - Action Items            |
| - Key Decisions           |
| - Open Questions          |
+------------+-------------+
             |
             v
      Structured Output
Project Structure
AI Video Assistant/
│
├── core/
│   ├── summarize.py
│   └── extractor.py
│
├── utils/
│   └── ...
│
├── main.py
├── test.py
├── requirements.txt
├── .gitignore
└── README.md
Installation
1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/AI-Video-Assistant.git
cd AI-Video-Assistant
2. Create a Virtual Environment
python -m venv .venv
Activate it on macOS/Linux:

source .venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
Environment Variables
Create a .env file in the root directory:

MISTRAL_AI_API_KEY=your_mistral_api_key
Replace your_mistral_api_key with your actual Mistral API key.

Never commit your .env file to GitHub.

The .gitignore file should contain:

.env
.venv/
__pycache__/
*.pyc
.DS_Store

*.mp3
*.wav
*.mp4
*.m4a
*.webm

*.pt
*.pth
*.bin

.vscode/
.idea/
*.log
How to Run
Run the main application:

python main.py
For testing:

python test.py
Provide a YouTube URL when prompted.

The application will:

Download the video's audio.

Process and chunk the audio.

Transcribe the audio using Whisper.

Generate a title using Mistral AI.

Generate a concise summary.

Extract action items.

Extract key decisions.

Extract open questions.

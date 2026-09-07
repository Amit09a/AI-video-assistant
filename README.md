# AI Video Assistant

An AI-powered video assistant that converts YouTube videos into structured and actionable information.

The application downloads the audio from a YouTube video, transcribes it using OpenAI Whisper, and processes the transcript using Mistral AI through LangChain.

It can generate:

- Video / meeting title
- Concise summary
- Action items
- Key decisions
- Open questions

---

## Features

- YouTube URL support
- Automatic audio extraction using `yt-dlp`
- Audio chunking using `pydub`
- Local speech-to-text transcription using OpenAI Whisper
- AI-powered summarization
- Automatic title generation
- Action item extraction
- Key decision extraction
- Open question extraction
- Modular Python architecture
- Environment variable based API key management

---

## Tech Stack

- **Python**
- **OpenAI Whisper**
- **Mistral AI**
- **LangChain**
- **yt-dlp**
- **pydub**
- **python-dotenv**

---

## Architecture

```text
                    YouTube URL
                         |
                         v
                  +-------------+
                  |    yt-dlp   |
                  | Audio Extract|
                  +------+------+
                         |
                         v
                  +-------------+
                  |    pydub    |
                  |Audio Chunking|
                  +------+------+
                         |
                         v
                  +-------------+
                  |   Whisper   |
                  |Transcription|
                  +------+------+
                         |
                         v
                    Transcript
                         |
             +-----------+-----------+
             |                       |
             v                       v
       Mistral AI              Mistral AI
       Summarization           Information
       & Title                 Extraction
             |                       |
             v                       v
       Final Summary        +-------------------+
                            | Action Items      |
                            | Key Decisions     |
                            | Open Questions    |
                            +-------------------+

# Project

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

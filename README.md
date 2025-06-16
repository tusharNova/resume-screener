# 🧠 AI-Powered Resume Screener (SaaS)

This project is a smart resume screening API that compares resumes to job descriptions using NLP. It helps recruiters or job-seekers evaluate how well a resume matches a specific role.

## 🚀 Features

- 📄 Upload PDF resumes
- 📃 Accept job descriptions via text
- 🧠 NLP-powered skill matching
- ✅ Match score & missing skill suggestions
- 🔒 FastAPI backend (fully modular)
- 🐳 Docker-ready for deployment

## 🛠 Tech Stack

- **Backend**: FastAPI, Python
- **Resume Parsing**: pdfminer.six
- **NLP**: spaCy, fuzzywuzzy
- **Version Control**: Git + GitHub
- **Deployment**: Docker (Render/Fly.io coming soon)

## 🔧 Running Locally

```bash
git clone https://github.com/tusharNova/resume-screener.git
cd resume-screener
pip install -r requirements.txt
uvicorn app.main:app --reload
Visit http://localhost:8000/docs for API testing.
```
## 📦 Coming Soon
- DOCX support
- Cover letter generator (OpenAI)
- Web UI (React or PyQt)
- PostgreSQL for history tracking
- Hosted demo link

----

#### Built by  Tushar Mankar — aspiring Python backend engineer 🚀


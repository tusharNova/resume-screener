from fastapi.testclient import TestClient
from app.main import app  # ✅ This now works
import os

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_upload_resume():
    resume_path = "data/sample_resume.pdf"
    assert os.path.exists(resume_path), "Sample resume not found"

    files = {"resume": ("sample_resume.pdf", open(resume_path, "rb"), "application/pdf")}
    data = {"job_description": "We are looking for a Python and Django developer..."}
    response = client.post("/upload-resume/", files=files, data=data)

    assert response.status_code == 200
    result = response.json()
    assert "match_score" in result

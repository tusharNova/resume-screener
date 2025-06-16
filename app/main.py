from fastapi import FastAPI ,File , UploadFile ,Form
from fastapi.responses import JSONResponse
from typing import Union
from app.resume_parser import extract_text_from_pdf
from app.match import compare_resume_to_jd

app = FastAPI()


@app.get('/')
def home():
    return {"message": "Resume Screener API is running."}



@app.post("/upload-resume/")
async def upload_resume(resume : UploadFile = File(...) , job_description : str = Form(...)):
    # resume_text = await resume.read()

    file_content = await resume.read()
    if resume.filename.endswith(".pdf"):
        resume_text = extract_text_from_pdf(file_content)
    else:
        resume_text = "Only PDF format supported (for now)."
        
    result = compare_resume_to_jd(resume_text, job_description)

    return JSONResponse(content={
        "filename": resume.filename,
        "match_score": result["match_score"],
        "matched_keywords": result["matched_keywords"],
        "missing_keywords": result["missing_keywords"],
        "suggestions": result["suggestions"]
    })
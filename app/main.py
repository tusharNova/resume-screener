from fastapi import FastAPI ,File , UploadFile ,Form
from fastapi.responses import JSONResponse
from typing import Union
from app.resume_parser import extract_text_from_pdf

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
        
    # TODO: Call parsing + matching logic here


    return JSONResponse(content={
        "filename" : resume.filename,
        "job_description" : job_description[:100] + "...",
        "Message" : "Resume uploaded successfully. Parsing and matching will be added soon."
    })
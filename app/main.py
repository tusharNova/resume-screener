from fastapi import FastAPI ,File , UploadFile ,Form
from fastapi.responses import JSONResponse
from typing import Union
from app.resume_parser import extract_text_from_pdf ,extract_text_from_file
from app.match import compare_resume_to_jd

app = FastAPI()


@app.get('/')
def home():
    return {"message": "Resume Screener API is running."}




@app.post("/upload-resume/")
async def upload_resume(resume: UploadFile = File(...), job_description: str = Form(...)):
    try:
        file_content = await resume.read()
        resume_text = extract_text_from_file(resume.filename, file_content)

        result = compare_resume_to_jd(resume_text, job_description)

        return JSONResponse(content=result)
    
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"error": str(e)})
from fastapi import FastAPI ,File , UploadFile ,Form , Request
from fastapi.responses import JSONResponse , HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Union
from app.resume_parser import extract_text_from_pdf ,extract_text_from_file
from app.match import compare_resume_to_jd
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "..", "templates"))

app = FastAPI()


@app.get('/',response_class=HTMLResponse)
def home(request:Request):
    return templates.TemplateResponse("index.html" , {"request" : request})




@app.post("/upload-resume/")
async def upload_resume(resume: UploadFile = File(...), job_description: str = Form(...)):
    try:
        content = await resume.read()
        resume_text = extract_text_from_file(resume.filename, content)

        result = compare_resume_to_jd(resume_text, job_description)
        result["filename"] = resume.filename

        return result
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
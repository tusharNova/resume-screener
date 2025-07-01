from fastapi import FastAPI ,File , UploadFile ,Form , Request , Body
from fastapi.responses import JSONResponse , HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Union
from app.resume_parser import extract_text_from_pdf ,extract_text_from_file
from app.match import compare_resume_to_jd
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
from fastapi.responses import StreamingResponse

from dotenv import load_dotenv

APP_NAME = os.getenv("APP_NAME")
print(f"Starting {APP_NAME}...")




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
    


@app.post("/export/json")
def export_json(data:dict = Body(...)):
    return JSONResponse(content=data)

@app.post("/export/pdf")
def export_pdf(data : dict = Body(...)):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer , pagesize=letter)
    y = 750

    p.drawString(100, y, f"Resume Analysis Report")
    y -=30
    for k , v in data.items():
        line = f"{k.capitalize()}:{','.join(v) if isinstance(v , list) else v}"
        p.drawString(100 , y ,line)
        y -=30


    p.save()
    buffer.seek(0)
    return StreamingResponse(buffer , media_type="application/json" , headers={"Content-Disposition": "attachment;          filename=resume_report.pdf"
    })

# json ,pyqt5 , fastapi , postman
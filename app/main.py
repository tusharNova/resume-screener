from fastapi import FastAPI ,File , UploadFile ,Form
from fastapi.responses import JSONResponse
from typing import Union

app = FastAPI()


@app.get('/')
def home():
    return {"message": "Resume Screener API is running."}



@app.post("/upload-resume/")
async def upload_resume(resume : UploadFile = File(...) , job_description : str = Form(...)):
    resume_text = await resume.read()

    # TODO: Call parsing + matching logic here


    return JSONResponse(content={
        "filename" : resume.filename,
        "job_description" : job_description[:100] + "...",
        "Message" : "Resume uploaded successfully. Parsing and matching will be added soon."
    })
FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential

COPY . .

RUN pip install --mo-cache-dir -r requirements.txt

RUN python -m spacy download en_core_web_sm

EXPOSE 8000

CMD [ "uvicorn"  , "app.main:app" , "--host" , "0.0.0.0" , "--port" , "8000"]


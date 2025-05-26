
from fastapi import FastAPI, UploadFile, File
from summarize import summarize_book
from tts import generate_tts
from video import generate_video

app = FastAPI()

@app.post("/upload")
async def upload_book(file: UploadFile = File(...)):
    contents = await file.read()
    with open(file.filename, "wb") as f:
        f.write(contents)
    return {"filename": file.filename}

@app.post("/summarize")
def run_summary(payload: dict):
    return summarize_book(payload["s3_key"])

@app.post("/generate-tts")
def run_tts(payload: dict):
    return generate_tts(payload["summary_id"])

@app.post("/generate-video")
def run_video(payload: dict):
    return generate_video(payload["tts_id"])

@app.get("/health")
def health():
    return {"status": "ok"}

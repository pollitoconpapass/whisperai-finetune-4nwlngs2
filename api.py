import io
import uvicorn
import librosa
from transformers import pipeline
from fastapi import FastAPI, File, UploadFile


app = FastAPI()
pipe = pipeline(model="pollitoconpapass/whisper-small-finetuned")  # -> change for the model you created (yourusername/model-name)

@app.post("/transcribe-whisper")
async def transcribe(audio: UploadFile = File(...)):
    contents = await audio.read()
    buffer = io.BytesIO(contents)
    with buffer:
        audio_array, _= librosa.load(buffer, sr=16000)

    text = pipe(audio_array)["text"]
    return {"text": text}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8088, log_level="info")

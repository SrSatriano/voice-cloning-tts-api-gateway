from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="TTS API Gateway", version="0.1.0")


class SynthesizeRequest(BaseModel):
    text: str
    voice_id: str
    language: str = "pt"
    format: str = "wav"
    speed: float = 1.0


class SynthesizeResponse(BaseModel):
    job_id: str | None = None
    audio_url: str | None = None
    status: str


VOICES: dict[str, str] = {}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/v1/tts/synthesize", response_model=SynthesizeResponse)
def synthesize(req: SynthesizeRequest):
    if req.voice_id not in VOICES and req.voice_id != "default":
        raise HTTPException(404, f"voice_id {req.voice_id} not found")
    if len(req.text) > 500:
        return SynthesizeResponse(job_id="batch-001", status="queued")
    return SynthesizeResponse(audio_url="/static/sample.wav", status="completed")


@app.post("/v1/tts/batch")
def batch(items: list[SynthesizeRequest]):
    return {"job_id": "batch-002", "count": len(items), "status": "queued"}

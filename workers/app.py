"""Celery worker — processamento em lote."""

import os

from celery import Celery

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
celery_app = Celery("tts", broker=redis_url, backend=redis_url)


@celery_app.task
def synthesize_batch(job_id: str, texts: list[str], voice_id: str) -> dict:
        return {"job_id": job_id, "completed": len(texts)}

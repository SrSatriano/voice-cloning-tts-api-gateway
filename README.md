# Voice-Cloning & TTS API Gateway

API REST self-hosted para geração rápida de áudio a partir de texto com vozes clonadas. Fila Celery/Redis para requisições em lote.

## Stack

- Python, FastAPI
- XTTSv2 / RVC
- Celery, Redis
- Swagger UI em `/docs`

## Documentação interativa

Após subir o serviço:

```
http://localhost:8000/docs
```

## Exemplo de payload

```json
POST /v1/tts/synthesize
{
  "text": "Olá, este é um teste de síntese.",
  "voice_id": "speaker_01",
  "language": "pt",
  "format": "wav",
  "speed": 1.0
}
```

Resposta assíncrona (batch):

```json
POST /v1/tts/batch
{
  "items": [
    {"text": "Linha 1", "voice_id": "speaker_01"},
    {"text": "Linha 2", "voice_id": "speaker_01"}
  ]
}
```

Retorna `job_id` — consultar em `GET /v1/jobs/{job_id}`.

Mais exemplos: [examples/](examples/) | [docs/API.md](docs/API.md)

## Formatação de áudio de origem (fine-tuning)

| Critério | Recomendação |
|----------|--------------|
| Duração | 30s–3min por amostra, 5–15 min total |
| Formato | WAV 24 kHz mono |
| Ruído | SNR > 25 dB; sem música de fundo |
| Conteúdo | Fala natural, variedade de fonemas |
| Normalização | -3 dB peak, sem clipping |

Detalhes: [docs/AUDIO_GUIDELINES.md](docs/AUDIO_GUIDELINES.md)

## Docker

```bash
docker compose up -d
```

## Estrutura

| Pasta | Função |
|-------|--------|
| `api/` | Rotas FastAPI |
| `workers/` | Tasks Celery |
| `models/` | Checkpoints XTTS/RVC |
| `examples/` | Payloads JSON |

## Ética

Use apenas vozes com consentimento explícito do titular.

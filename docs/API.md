# API Reference

## POST /v1/voices/register

Upload de amostra para clonar voz.

- `multipart/form-data`: `file` (wav), `name` (string)

## GET /v1/voices

Lista vozes registradas.

## POST /v1/tts/synthesize

Síncrono para textos < 500 caracteres.

## POST /v1/tts/batch

Assíncrono via Celery.

## Códigos de erro

| Código | Significado |
|--------|-------------|
| 400 | Payload inválido |
| 404 | voice_id inexistente |
| 503 | Fila saturada |

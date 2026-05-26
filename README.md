<div align="center">

# Gateway de API de clonagem de voz e TTS

**Gateway de API de clonagem de voz e TTS**

<p>
  <a href="https://github.com/SrSatriano/voice-cloning-tts-api-gateway"><img src="https://img.shields.io/badge/GitHub-voice-cloning-tts-api-gateway-24292e?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
</p>

<p>
  <img src="https://img.shields.io/badge/versão-1.0.0-0ea5e9?style=flat-square" alt="versão" />
  <img src="https://img.shields.io/badge/licença-MIT-22c55e?style=flat-square" alt="licença" />
  <img src="https://img.shields.io/badge/idioma-pt--BR-blue?style=flat-square" alt="idioma" />
  <img src="https://img.shields.io/badge/CI-GitHub_Actions-8b5cf6?style=flat-square" alt="ci" />
</p>

<p><strong>Síntese e clonagem de voz self-hosted com filas assíncronas.</strong></p>

<p>
  Autor: <a href="https://github.com/SrSatriano">@SrSatriano</a> ·
  Release <strong>1.0.0</strong> (2026-03-26)
</p>

</div>

---

## Índice

1. [Visão geral](#visão-geral)
2. [Problema e solução](#problema-e-solução)
3. [Para quem é](#para-quem-é)
4. [Casos de uso](#casos-de-uso)
5. [Funcionalidades](#funcionalidades)
6. [Stack tecnológica](#stack-tecnológica)
7. [Arquitetura](#arquitetura)
8. [Estrutura do repositório](#estrutura-do-repositório)
9. [Pré-requisitos](#pré-requisitos)
10. [Instalação e execução](#instalação-e-execução)
11. [Configuração](#configuração)
12. [Testes](#testes)
13. [Performance](#performance)
14. [Deploy e operação](#deploy-e-operação)
15. [Limitações conhecidas](#limitações-conhecidas)
16. [Roadmap](#roadmap)
17. [Documentação complementar](#documentação-complementar)
18. [Segurança e licença](#segurança-e-licença)

---

## Visão geral

Este repositório faz parte do **portfólio de engenharia** mantido por [@SrSatriano](https://github.com/SrSatriano). A versão **1.0.0** entrega implementação do núcleo do produto, testes automatizados, pipeline de integração contínua e documentação operacional em **português brasileiro**.

O objetivo é permitir que você clone, execute e evolua o projeto com clareza — do desenvolvimento local ao deploy em produção.

## Problema e solução

| | |
|---|---|
| **Problema** | APIs comerciais de voz são caras e impedem fine-tuning com dados proprietários. |
| **Solução** | API com workers horizontais, upload de WAV de referência e documentação de qualidade de áudio. |

## Para quem é

Produtoras de conteúdo, apps de acessibilidade e chatbots com voz.

## Casos de uso

- Narração de vídeos
- IVR personalizado

## Funcionalidades

- [x] Swagger UI interativo
- [x] Síntese síncrona e batch assíncrono
- [x] Registro de vozes por upload WAV
- [x] Workers Redis escaláveis
- [x] Guia de fine-tuning

## Stack tecnológica

| Camada | Tecnologias |
|--------|-------------|
| **Principal** | Python, FastAPI, Celery, Redis, XTTS |

## Arquitetura

```mermaid
flowchart LR
  CLI[Cliente / Swagger] --> API[FastAPI]
  API --> Q[Fila Redis / Celery]
  Q --> WR[Workers]
  WR --> ST[(Armazenamento)]
```

Detalhamento de componentes, fluxos de dados e decisões de design: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Estrutura do repositório

| Caminho | Descrição |
|---------|-----------|
| `src/api/` | FastAPI |
| `workers/` | Celery tasks |

## Pré-requisitos

Python 3.11+, Redis, GPU recomendada para XTTS.

## Instalação e execução

```bash
git clone https://github.com/SrSatriano/voice-cloning-tts-api-gateway.git
cd voice-cloning-tts-api-gateway
```

```bash
docker compose up -d
Acesse http://localhost:8000/docs
```

## Configuração

| Variável | Descrição | Exemplo |
|----------|-----------|--------|
| `REDIS_URL` | Broker Celery | `redis://localhost:6379/0` |

> **Importante:** nunca faça commit de arquivos `.env` com segredos reais. Use `.env.example` como referência.

## Testes

Execute a suíte de testes antes de abrir pull requests:

```bash
pytest tests/ -q
```

A pipeline [`.github/workflows/ci.yml`](.github/workflows/ci.yml) repete build e testes em cada push para `main`.

## Performance

| Modo | Latência (200 caracteres) |
|------|---------------------------|
| Síncrono | ~1,2 s |

Metodologia, hardware de referência e flags de compilação: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Deploy e operação

| Guia | Conteúdo |
|------|----------|
| [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) | Homologação, produção e rollback |
| [docs/OPERATIONS.md](docs/OPERATIONS.md) | Monitoramento, alertas e incidentes |

## Limitações conhecidas

- Clonagem exige amostra de voz limpa ≥ 6 s

## Roadmap

- Streaming de áudio via WebSocket

## Documentação complementar

| Documento | Descrição |
|-----------|-----------|
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Arquitetura e decisões técnicas |
| [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) | Deploy passo a passo |
| [docs/OPERATIONS.md](docs/OPERATIONS.md) | Runbook operacional |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Como contribuir |
| [CHANGELOG.md](CHANGELOG.md) | Histórico de versões |
| [SECURITY.md](SECURITY.md) | Política de segurança |
| [AUTHORS.md](AUTHORS.md) | Créditos |

## Segurança e licença

- Dependências revisadas na release **1.0.0**
- Vulnerabilidades: siga [SECURITY.md](SECURITY.md)
- Licença: [MIT](LICENSE) © SrSatriano 2026

---

<p align="center">Desenvolvido com foco em clareza e engenharia de produção · <a href="https://github.com/SrSatriano/voice-cloning-tts-api-gateway">Ver no GitHub</a></p>

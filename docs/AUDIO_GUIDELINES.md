# Diretrizes de áudio de origem

## Pré-processamento

1. Remover silêncio inicial/final (threshold -40 dB).
2. Aplicar high-pass 80 Hz.
3. Exportar WAV PCM 16-bit, 24000 Hz mono.

## Evitar

- Compressão MP3 com artefatos.
- Eco de sala (use close-mic).
- Múltiplos falantes na mesma faixa.

## RVC vs XTTS

- **XTTS**: poucas amostras, multilíngue.
- **RVC**: melhor similaridade timbral com mais dados limpos.

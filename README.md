# hermes-omnivoice-tts

**Engine TTS (OmniVoice HTTP + sub-sentence streaming) para hermes-agent v0.16+.**

## Install

```bash
pip install hermes-omnivoice-tts
```

## Uso

```python
from omnivoice_tts.client import OmniVoiceClient

client = OmniVoiceClient(
    base_url="http://127.0.0.1:8202/v1/audio/speech",
    voice="jarvis-clone-trimmed",
)

# Síntese completa
audio = await client.synthesize("Bom dia, Senhor.")

# Streaming sub-sentence
async for chunk in client.stream_synthesize(
    "Bom dia, Senhor. São 14:32, hora de começar o trabalho.",
    sub_sentence_words=12,
):
    play(chunk)
```

## Como funciona

1. Quebra texto em chunks de 8-15 palavras
2. Sintetiza cada chunk via OmniVoice HTTP API
3. Retorna bytes (Opus ou WAV)
4. First chunk latency: <500ms

## Compatibilidade

- Python 3.11+
- Bind 127.0.0.1 only (OmniVoice local)
- Sub-sentence streaming 8-15 palavras
- 11 voice models supported (jarvis-clone-trimmed default)

## License

MIT

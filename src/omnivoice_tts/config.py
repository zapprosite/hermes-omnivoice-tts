"""OmniVoice TTS config."""
from pydantic import BaseSettings, HttpUrl


class OmniVoiceConfig(BaseSettings):
    base_url: HttpUrl = "http://127.0.0.1:8202/v1/audio/speech"
    voice: str = "jarvis-clone-trimmed"
    model: str = "omnivoice"
    speed: float = 1.0
    streaming: bool = True
    sub_sentence_words: int = 12  # 8-15 words
    first_chunk_timeout_ms: int = 500

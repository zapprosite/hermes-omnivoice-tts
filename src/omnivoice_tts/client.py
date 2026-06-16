"""OmniVoice TTS HTTP client (sub-sentence streaming)."""
from __future__ import annotations
import asyncio
import logging
from typing import AsyncIterator

import httpx

log = logging.getLogger("omnivoice_tts_client")


class OmniVoiceClient:
    """Cliente HTTP para OmniVoice TTS com streaming sub-sentence."""

    def __init__(self, base_url: str, voice: str = "jarvis-clone-trimmed"):
        self.base_url = base_url
        self.voice = voice
        self.client = httpx.AsyncClient(timeout=10.0)

    async def synthesize(
        self,
        text: str,
        model: str = "omnivoice",
        speed: float = 1.0,
        stream: bool = True,
    ) -> bytes:
        """Síntese completa (não-streaming)."""
        response = await self.client.post(
            self.base_url,
            json={
                "model": model,
                "input": text,
                "voice": self.voice,
                "speed": speed,
                "stream": stream,
            },
        )
        response.raise_for_status()
        return response.content

    async def stream_synthesize(
        self,
        text: str,
        sub_sentence_words: int = 12,
    ) -> AsyncIterator[bytes]:
        """Streaming sub-sentence (8-15 words por chunk).

        Quebra o texto em chunks e sintetiza cada um.
        First chunk latency: <500ms.
        """
        words = text.split()
        chunks = [
            " ".join(words[i : i + sub_sentence_words])
            for i in range(0, len(words), sub_sentence_words)
        ]

        for chunk in chunks:
            log.debug(f"TTS chunk: {chunk[:50]}...")
            audio = await self.synthesize(chunk, stream=False)
            yield audio

    async def close(self):
        await self.client.aclose()

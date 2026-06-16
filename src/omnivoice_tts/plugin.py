"""OmniVoice TTS plugin (backend kind, substitui TTS default)."""
from __future__ import annotations
import logging

log = logging.getLogger("omnivoice_tts")


class OmniVoiceTTSPlugin:
    """Plugin backend que substitui o TTS padrão por OmniVoice."""
    name = "omnivoice-tts"
    kind = "backend"
    version = "1.0.0"

    def register(self, ctx) -> None:
        # Registrar como backend TTS (substitui o default)
        ctx.register_tts_backend("omnivoice", self._synthesize)
        log.info("omnivoice-tts v%s registrado", self.version)

    async def _synthesize(self, text: str, **kwargs):
        """Síntese TTS via OmniVoice HTTP API."""
        import httpx
        from .config import OmniVoiceConfig

        config = OmniVoiceConfig()
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(
                str(config.base_url),
                json={
                    "model": config.model,
                    "input": text,
                    "voice": config.voice,
                    "speed": config.speed,
                    "stream": config.streaming,
                },
            )
            response.raise_for_status()
            return response.content  # bytes (audio)

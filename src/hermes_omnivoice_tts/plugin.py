"""OmnivoiceTtsPlugin: hermes-omnivoice-tts para hermes-agent."""
from __future__ import annotations

import logging
from pathlib import Path

log = logging.getLogger("hermes-omnivoice-tts")


class OmnivoiceTtsPlugin:
    """Plugin backend."""
    name = "hermes-omnivoice-tts"
    kind = "backend"
    version = "1.0.0"

    def register(self, ctx) -> None:
        """Hook de registro."""
        # Tools
        ctx.register_tool("hermes_omnivoice_tts_status", self._tool_status)

        # Skills
        skill_path = self._skill_path()
        if skill_path.exists():
            ctx.register_skill("hermes-omnivoice-tts", skill_path)

        log.info("hermes-omnivoice-tts v%s registrado", self.version)

    def _skill_path(self) -> Path:
        return Path(__file__).parent.parent.parent / "skills" / "omnivoice-tts"

    def _tool_status(self, **_):
        return {"status": "ready", "version": self.version}

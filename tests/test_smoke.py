"""Smoke tests para hermes-omnivoice-tts."""
import pytest
import httpx


def test_omnivoice_endpoint_reachable():
    """OmniVoice deve estar em :8202 (se rodando)."""
    try:
        with httpx.Client(timeout=2.0) as c:
            r = c.get("http://127.0.0.1:8202/v1/audio/voices")
            # 200 ou 401/404 sao ok (significa que tem algo ouvindo)
            assert r.status_code in (200, 401, 404, 405)
    except httpx.ConnectError:
        pytest.skip("OmniVoice nao esta rodando (esperado em CI)")

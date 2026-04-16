"""Application configuration."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Basic settings for the diagnostic tool."""

    app_name: str = "System Diagnostic Tool"
    version: str = "0.1.0"
    debug: bool = False


settings = Settings()

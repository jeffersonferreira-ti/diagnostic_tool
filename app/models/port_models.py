"""Data models for port connectivity checks."""

from dataclasses import dataclass


@dataclass
class PortCheckResult:
    """Represents the outcome of a TCP port connectivity check."""

    target: str
    port: int
    success: bool
    error_message: str = ""

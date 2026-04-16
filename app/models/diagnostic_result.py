"""Basic models used by the application."""

from dataclasses import dataclass, field


@dataclass
class DiagnosticResult:
    """Minimal container for future diagnostic results."""

    name: str
    status: str = "pending"
    details: dict = field(default_factory=dict)

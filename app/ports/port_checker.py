"""Run predefined TCP port connectivity checks."""

import socket

from app.models.port_models import PortCheckResult

DEFAULT_TIMEOUT = 3
PORT_CHECK_TARGETS = [
    ("google.com", 80),
    ("google.com", 443),
    ("localhost", 3389),
    ("localhost", 22),
]


def _run_port_check(target: str, port: int) -> PortCheckResult:
    """Attempt a TCP connection to a single predefined target."""
    try:
        with socket.create_connection((target, port), timeout=DEFAULT_TIMEOUT):
            return PortCheckResult(
                target=target,
                port=port,
                success=True,
            )
    except OSError as exc:
        return PortCheckResult(
            target=target,
            port=port,
            success=False,
            error_message=str(exc),
        )


def run_port_checks() -> list[PortCheckResult]:
    """Run the predefined port connectivity checks."""
    return [
        _run_port_check(target, port)
        for target, port in PORT_CHECK_TARGETS
    ]

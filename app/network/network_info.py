"""Collect network diagnostic information."""

import socket

from app.models.network_models import (
    ConnectivityTestResult,
    DnsTestResult,
    NetworkInfo,
)

DEFAULT_TIMEOUT = 3
DNS_TEST_DOMAIN = "google.com"
CONNECTIVITY_TARGETS = [
    ("8.8.8.8", 53),
    ("google.com", 443),
]


def _get_hostname() -> str:
    """Return the local hostname with a safe fallback."""
    try:
        return socket.gethostname()
    except OSError:
        return "Unavailable"


def _get_local_ip() -> str:
    """Determine the primary local IP without requiring external traffic."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.connect(("8.8.8.8", 80))
            return sock.getsockname()[0]
    except OSError:
        try:
            return socket.gethostbyname(socket.gethostname())
        except OSError:
            return "Unavailable"


def _run_dns_test(domain: str) -> DnsTestResult:
    """Attempt to resolve a known domain."""
    try:
        resolved_ip = socket.gethostbyname(domain)
        return DnsTestResult(
            domain=domain,
            resolved_ip=resolved_ip,
            success=True,
        )
    except OSError as exc:
        return DnsTestResult(
            domain=domain,
            resolved_ip="Unavailable",
            success=False,
            error_message=str(exc),
        )


def _run_connectivity_test(target: str, port: int) -> ConnectivityTestResult:
    """Attempt a TCP connection to the target within a short timeout."""
    try:
        with socket.create_connection((target, port), timeout=DEFAULT_TIMEOUT):
            return ConnectivityTestResult(
                target=target,
                port=port,
                success=True,
            )
    except OSError as exc:
        return ConnectivityTestResult(
            target=target,
            port=port,
            success=False,
            error_message=str(exc),
        )


def get_network_info() -> NetworkInfo:
    """Collect basic network information and connectivity diagnostics."""
    hostname = _get_hostname()
    local_ip = _get_local_ip()
    dns_test = _run_dns_test(DNS_TEST_DOMAIN)
    connectivity_tests = [
        _run_connectivity_test(target, port)
        for target, port in CONNECTIVITY_TARGETS
    ]

    return NetworkInfo(
        hostname=hostname,
        local_ip=local_ip,
        dns_test=dns_test,
        connectivity_tests=connectivity_tests,
    )

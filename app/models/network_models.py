"""Data models for network diagnostics."""

from dataclasses import dataclass, field


@dataclass
class DnsTestResult:
    """Represents the outcome of a DNS resolution test."""

    domain: str
    resolved_ip: str
    success: bool
    error_message: str = ""


@dataclass
class ConnectivityTestResult:
    """Represents the outcome of a TCP connectivity test."""

    target: str
    port: int
    success: bool
    error_message: str = ""


@dataclass
class NetworkInfo:
    """Represents the network diagnostics summary."""

    hostname: str
    local_ip: str
    dns_test: DnsTestResult
    connectivity_tests: list[ConnectivityTestResult] = field(default_factory=list)

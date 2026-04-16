"""Data models for system diagnostics."""

from dataclasses import dataclass


@dataclass
class SystemInfo:
    """Represents key system metrics for diagnostics."""

    hostname: str
    os_name: str
    os_version: str
    architecture: str
    processor: str
    cpu_usage: float
    total_memory: float
    used_memory: float
    memory_percent: float
    total_disk: float
    free_disk: float
    disk_percent: float

"""Collect system diagnostic information."""

import platform
import socket
import sys

import psutil

from app.models.system_models import SystemInfo


def _bytes_to_gb(value: int) -> float:
    """Convert bytes to gigabytes with readable rounding."""
    return round(value / (1024 ** 3), 2)


def _get_os_details() -> tuple[str, str]:
    """Return a user-friendly operating system name and version."""
    os_name = platform.system() or "Unknown"

    if os_name != "Windows":
        os_version = platform.release() or platform.version() or "Unknown"
        return os_name, os_version

    try:
        build_number = sys.getwindowsversion().build
        friendly_name = "Windows 11" if build_number >= 22000 else "Windows 10"
        return friendly_name, f"build {build_number}"
    except AttributeError:
        pass

    raw_version = platform.version() or "Unknown"
    build_number = raw_version.split(".")[-1] if "." in raw_version else raw_version

    if build_number.isdigit():
        friendly_name = "Windows 11" if int(build_number) >= 22000 else "Windows 10"
        return friendly_name, f"build {build_number}"

    return "Windows", raw_version


def get_system_info() -> SystemInfo:
    """Collect core system information used for diagnostics."""
    try:
        hostname = socket.gethostname()
        os_name, os_version = _get_os_details()
        architecture = platform.machine() or "Unknown"
        processor = platform.processor() or "Unknown"

        cpu_usage = round(psutil.cpu_percent(interval=1), 2)

        memory = psutil.virtual_memory()
        disk = psutil.disk_usage("/")

        return SystemInfo(
            hostname=hostname,
            os_name=os_name,
            os_version=os_version,
            architecture=architecture,
            processor=processor,
            cpu_usage=cpu_usage,
            total_memory=_bytes_to_gb(memory.total),
            used_memory=_bytes_to_gb(memory.used),
            memory_percent=round(memory.percent, 2),
            total_disk=_bytes_to_gb(disk.total),
            free_disk=_bytes_to_gb(disk.free),
            disk_percent=round(disk.percent, 2),
        )
    except Exception:
        return SystemInfo(
            hostname="Unavailable",
            os_name="Unavailable",
            os_version="Unavailable",
            architecture="Unavailable",
            processor="Unavailable",
            cpu_usage=0.0,
            total_memory=0.0,
            used_memory=0.0,
            memory_percent=0.0,
            total_disk=0.0,
            free_disk=0.0,
            disk_percent=0.0,
        )

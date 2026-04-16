"""Application entry point for the diagnostic report."""

from app.network.network_info import get_network_info
from app.system.system_info import get_system_info
from config import settings


def _get_resource_status(value: float) -> str:
    """Return a status label for CPU, memory, and disk usage."""
    if value >= 90:
        return "CRITICAL"
    if value >= 80:
        return "WARNING"
    return "OK"


def _get_check_status(success: bool) -> str:
    """Return a status label for binary network checks."""
    return "OK" if success else "FAILED"


def _format_os_line(name: str, version: str) -> str:
    """Format the operating system for display."""
    if version and version != "Unknown":
        return f"{name} ({version})"
    return name


def main() -> None:
    """Run the system and network diagnostics summary."""
    system_info = get_system_info()
    network_info = get_network_info()
    cpu_status = _get_resource_status(system_info.cpu_usage)
    memory_status = _get_resource_status(system_info.memory_percent)
    disk_status = _get_resource_status(system_info.disk_percent)
    dns_status = _get_check_status(network_info.dns_test.success)

    print(f"{settings.app_name} v{settings.version}")
    print()
    print(f"Hostname: {system_info.hostname}")
    print()
    print("## System Information")
    print()
    print(f"OS: {_format_os_line(system_info.os_name, system_info.os_version)}")
    print(f"Architecture: {system_info.architecture}")
    print(f"Processor: {system_info.processor}")
    print()
    print(f"CPU Usage: {system_info.cpu_usage:.0f}% [{cpu_status}]")
    print(
        f"Memory: {system_info.used_memory:.2f}GB / "
        f"{system_info.total_memory:.2f}GB "
        f"({system_info.memory_percent:.0f}%) "
        f"[{memory_status}]"
    )
    print(
        f"Disk: {system_info.free_disk:.2f}GB free / "
        f"{system_info.total_disk:.2f}GB "
        f"({system_info.disk_percent:.0f}%) "
        f"[{disk_status}]"
    )
    print()
    print("## Network Diagnostics")
    print()
    print(f"Local IP: {network_info.local_ip}")

    if network_info.dns_test.success:
        print(
            "DNS Resolution: "
            f"OK ({network_info.dns_test.domain} -> "
            f"{network_info.dns_test.resolved_ip}) "
            f"[{dns_status}]"
        )
    else:
        print(
            "DNS Resolution: "
            f"FAILED ({network_info.dns_test.domain}) "
            f"[{dns_status}]"
        )
        if network_info.dns_test.error_message:
            print(f"DNS Error: {network_info.dns_test.error_message}")

    for test in network_info.connectivity_tests:
        status = _get_check_status(test.success)
        message = f"Connectivity: {test.target}:{test.port} -> {status}"
        if not test.success and test.error_message:
            message = f"{message} ({test.error_message})"
        print(f"{message} [{status}]")


if __name__ == "__main__":
    main()

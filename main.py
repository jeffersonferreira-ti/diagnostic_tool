"""Application entry point for the diagnostic report."""

import os

from app.network.network_info import get_network_info
from app.ports.port_checker import run_port_checks
from app.reporting.report_generator import save_json_report
from app.system.system_info import get_system_info
from config import settings

STATUS_COLORS = {
    "OK": "\033[32m",
    "WARNING": "\033[33m",
    "CRITICAL": "\033[31m",
    "FAILED": "\033[31m",
}
RESET_COLOR = "\033[0m"


def _supports_color() -> bool:
    """Return True when ANSI color output is likely supported."""
    return os.getenv("TERM") is not None or os.name != "nt"


def _format_status_label(status: str) -> str:
    """Format a status label, using color when supported."""
    label = f"[{status}]"
    if not _supports_color():
        return label

    color = STATUS_COLORS.get(status, "")
    if not color:
        return label

    return f"{color}{label}{RESET_COLOR}"


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


def _build_key_findings(
    memory_status: str,
    disk_status: str,
    dns_status: str,
    port_checks: list,
) -> list[str]:
    """Build a concise list of relevant issues for the summary."""
    findings = []

    if memory_status in {"WARNING", "CRITICAL"}:
        findings.append("High memory usage")
    if disk_status in {"WARNING", "CRITICAL"}:
        findings.append("High disk usage")
    if dns_status == "FAILED":
        findings.append("DNS resolution failed")

    local_port_labels = {
        ("localhost", 3389): "RDP port unavailable",
        ("localhost", 22): "SSH port unavailable",
    }

    for check in port_checks:
        if not check.success:
            findings.append(
                local_port_labels.get(
                    (check.target, check.port),
                    f"{check.target}:{check.port} unavailable",
                )
            )

    return findings


def _get_overall_status(
    cpu_status: str,
    memory_status: str,
    disk_status: str,
    dns_status: str,
    connectivity_statuses: list[str],
    port_statuses: list[str],
) -> str:
    """Determine the overall report status."""
    all_statuses = [
        cpu_status,
        memory_status,
        disk_status,
        dns_status,
        *connectivity_statuses,
        *port_statuses,
    ]

    if "CRITICAL" in all_statuses:
        return "CRITICAL"
    if "WARNING" in all_statuses or "FAILED" in all_statuses:
        return "WARNING"
    return "OK"


def _print_connectivity_line(target: str, port: int, status: str) -> None:
    """Print a concise connectivity result line."""
    print(f"{target}:{port} -> {status} {_format_status_label(status)}")


def main() -> None:
    """Run the system, network, and port diagnostics summary."""
    report_path = "data/output/diagnostic_report.json"
    system_info = get_system_info()
    network_info = get_network_info()
    port_checks = run_port_checks()
    cpu_status = _get_resource_status(system_info.cpu_usage)
    memory_status = _get_resource_status(system_info.memory_percent)
    disk_status = _get_resource_status(system_info.disk_percent)
    dns_status = _get_check_status(network_info.dns_test.success)
    connectivity_statuses = [
        _get_check_status(test.success)
        for test in network_info.connectivity_tests
    ]
    port_statuses = [
        _get_check_status(check.success)
        for check in port_checks
    ]
    external_port_checks = [
        check for check in port_checks if check.target != "localhost"
    ]
    local_port_checks = [
        check for check in port_checks if check.target == "localhost"
    ]
    overall_status = _get_overall_status(
        cpu_status,
        memory_status,
        disk_status,
        dns_status,
        connectivity_statuses,
        port_statuses,
    )
    key_findings = _build_key_findings(
        memory_status,
        disk_status,
        dns_status,
        port_checks,
    )

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
    print(
        f"CPU Usage: {system_info.cpu_usage:.0f}% "
        f"{_format_status_label(cpu_status)}"
    )
    print(
        f"Memory: {system_info.used_memory:.2f}GB / "
        f"{system_info.total_memory:.2f}GB "
        f"({system_info.memory_percent:.0f}%) "
        f"{_format_status_label(memory_status)}"
    )
    print(
        f"Disk: {system_info.free_disk:.2f}GB free / "
        f"{system_info.total_disk:.2f}GB "
        f"({system_info.disk_percent:.0f}%) "
        f"{_format_status_label(disk_status)}"
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
            f"{_format_status_label(dns_status)}"
        )
    else:
        print(
            "DNS Resolution: "
            f"FAILED ({network_info.dns_test.domain}) "
            f"{_format_status_label(dns_status)}"
        )

    for test in network_info.connectivity_tests:
        status = _get_check_status(test.success)
        print(
            "Connectivity: "
            f"{test.target}:{test.port} -> {status} "
            f"{_format_status_label(status)}"
        )

    print()
    print("## External Service Checks")
    print()
    for check in external_port_checks:
        status = _get_check_status(check.success)
        _print_connectivity_line(check.target, check.port, status)

    print()
    print("## Local Service Checks")
    print()
    for check in local_port_checks:
        status = _get_check_status(check.success)
        _print_connectivity_line(check.target, check.port, status)

    print()
    print("## Summary")
    print()
    print(f"Overall Status: {overall_status}")
    print()
    print("Key Findings:")
    print()

    if key_findings:
        for finding in key_findings:
            print(f"* {finding}")
    else:
        print("* No issues detected")

    saved_report_path = save_json_report(
        output_path=report_path,
        system_info=system_info,
        network_info=network_info,
        external_port_checks=external_port_checks,
        local_port_checks=local_port_checks,
        cpu_status=cpu_status,
        memory_status=memory_status,
        disk_status=disk_status,
        overall_status=overall_status,
        key_findings=key_findings,
        get_status=_get_check_status,
    )
    print()
    print(f"Report path: {saved_report_path}")


if __name__ == "__main__":
    main()

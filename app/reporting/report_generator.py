"""Generate and save diagnostic reports."""

import json
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path


def _serialize_port_checks(port_checks: list, get_status) -> list[dict]:
    """Serialize port checks for JSON output."""
    return [
        {
            "target": check.target,
            "port": check.port,
            "success": check.success,
            "status": get_status(check.success),
            "error_message": check.error_message,
        }
        for check in port_checks
    ]


def save_json_report(
    output_path: str,
    system_info,
    network_info,
    external_port_checks: list,
    local_port_checks: list,
    cpu_status: str,
    memory_status: str,
    disk_status: str,
    overall_status: str,
    key_findings: list[str],
    get_status,
) -> str:
    """Save the diagnostic results as a formatted JSON report."""
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "hostname": system_info.hostname,
        "system_information": {
            "os_name": system_info.os_name,
            "os_version": system_info.os_version,
            "architecture": system_info.architecture,
            "processor": system_info.processor,
            "cpu_usage": system_info.cpu_usage,
            "cpu_status": cpu_status,
            "total_memory": system_info.total_memory,
            "used_memory": system_info.used_memory,
            "memory_percent": system_info.memory_percent,
            "memory_status": memory_status,
            "total_disk": system_info.total_disk,
            "free_disk": system_info.free_disk,
            "disk_percent": system_info.disk_percent,
            "disk_status": disk_status,
        },
        "network_diagnostics": {
            "local_ip": network_info.local_ip,
            "dns_test": {
                **asdict(network_info.dns_test),
                "status": get_status(network_info.dns_test.success),
            },
            "connectivity_tests": [
                {
                    **asdict(test),
                    "status": get_status(test.success),
                }
                for test in network_info.connectivity_tests
            ],
        },
        "external_service_checks": _serialize_port_checks(
            external_port_checks,
            get_status,
        ),
        "local_service_checks": _serialize_port_checks(
            local_port_checks,
            get_status,
        ),
        "summary": {
            "overall_status": overall_status,
            "key_findings": key_findings,
        },
    }

    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(
        json.dumps(report, indent=2),
        encoding="utf-8",
    )
    return output_file.as_posix()

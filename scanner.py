#!/usr/bin/env python3
import argparse

from core.cve_checker import check_cve
from core.analyzer import analyze
from ai.ai_module import ai_analyze



print("""
=========================================
   Confluence Vulnerability Scanner
     CVE-2023-22515 Detection Tool
=========================================
""")



def main():
    parser = argparse.ArgumentParser(
        description="Confluence CVE-2023-22515 Scanner"
    )

    parser.add_argument(
        "-u", "--url",
        required=True,
        help="Target Confluence URL (e.g., https://example.com)"
    )

    args = parser.parse_args()
    target = args.url

    print(f"\n[+] Scanning: {target}")

    # Phase 3
    findings = check_cve(target)

    print("\n=== Endpoint Analysis ===")
    for f in findings:
        print(f"[+] {f['endpoint']} → {f['status']}")

    # Phase 4
    result = analyze(findings)
    print(f"\n[!] Basic Status: {result}")

    # Phase 5
    ai_result = ai_analyze(findings)

    print("\n=== AI ANALYSIS ===")
    print(f"[+] Risk: {ai_result['risk']}")
    print(f"[+] Confidence: {ai_result['confidence']}%")
    print("\n[+] Explanation:")
    print(ai_result["explanation"])


if __name__ == "__main__":
    main()

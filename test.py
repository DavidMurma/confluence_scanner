from utils.http import fetch
from core.detector import detect_confluence
from core.cve_checker import check_cve
from core.analyzer import analyze
from ai.ai_module import ai_analyze


r = fetch("https://httpbin.org/get")
# r = fetch("https://confluence.org/get")

if r:
    print("Status:", r.status_code)
else:
    print("Request failed")
    

# --------------------------- Confluence detector checker ---------------------------


# target = "https://example.com"

# if detect_confluence(target):
#     print("Confluence detected ✅")
# else:
#     print("Not Confluence ❌")


# target = "https://example.com"

# --------------------------- Endpoint CVE checker ---------------------------


target = "https://httpbin.org/status"
findings = check_cve(target)

print("\n=== Endpoint Analysis ===")

for f in findings:
    print(f"[+] {f['endpoint']} → {f['status']}")

# --------------------------- Analyzer checker ---------------------------

# target = "https://example.com"

findings = check_cve(target)

print("\n=== Endpoint Analysis ===")
for f in findings:
    print(f"[+] {f['endpoint']} → {f['status']}")

result = analyze(findings)

print("\n=== FINAL RESULT ===")
print("Status:", result)


#/--------------------------- AI Module checker ---------------------------

# target = "https://httpbin.org"

print(f"\nScanning: {target}")

# Phase 3
findings = check_cve(target)

print("\n=== Endpoint Analysis ===")
for f in findings:
    print(f"[+] {f['endpoint']} → {f['status']}")

# Phase 4
result = analyze(findings)
print("\n=== BASIC RESULT ===")
print("Status:", result)

# ✅ NEW (Phase 5)
ai_result = ai_analyze(findings)

print("\n=== AI ANALYSIS ===")
print("Risk:", ai_result["risk"])
print("Confidence:", ai_result["confidence"])
print("\nExplanation:")
print(ai_result["explanation"])



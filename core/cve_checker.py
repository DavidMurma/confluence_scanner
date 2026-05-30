import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from utils.http import fetch
# from utils.http import fetch





def check_cve(target):
    endpoints = [
        "/server-info.action",
        "/setup/setupadministrator.action",
        "/setup/setupstart.action"
    ]

    findings = []

    for ep in endpoints:
        url = target.rstrip("/") + ep
        r = fetch(url)
        # print("first print",url, r)

        if r:
            findings.append({
                "endpoint": ep,
                "status": r.status_code
            })
        else:
            findings.append({
                "endpoint": ep,
                "status": "error"
            })

    return findings


# check_cve("https://example.com")



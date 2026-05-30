
def analyze(findings):
    accessible = 0
    protected = 0
    unknown = 0

    for f in findings:
        status = f["status"]

        if status == 200:
            accessible += 1
        elif status in [301, 302, 403]:
            protected += 1
        else:
            unknown += 1

    # Decision logic
    if accessible > 0:
        return "POSSIBLY VULNERABLE"
    elif protected > 0:
        return "LIKELY SAFE"
    else:
        return "UNKNOWN"

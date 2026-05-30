def ai_analyze(findings):
    score = 0
    total = len(findings)

    for f in findings:
        status = f["status"]

        if status == 200:
            score += 50
        elif status in [301, 302]:
            score += 10
        elif status == 403:
            score += 5
        else:
            score += 0

    # Normalize score
    confidence = min(score, 100)

    # Determine risk level
    if confidence >= 70:
        risk = "HIGH RISK"
    elif confidence >= 30:
        risk = "MEDIUM RISK"
    else:
        risk = "LOW RISK"

    # Generate explanation
    explanation = f"""
The scanner analyzed {total} important Confluence endpoints.

Accessible endpoints (HTTP 200) suggest possible improper access control.
This is related to CVE-2023-22515, where setup or admin functions may be exposed.

Higher accessibility increases the likelihood of vulnerability.
    """

    return {
        "risk": risk,
        "confidence": confidence,
        "explanation": explanation.strip()
    }

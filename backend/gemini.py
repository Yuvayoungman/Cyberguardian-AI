import re
from urllib.parse import urlparse

def analyze_text(text: str):
    text_l = text.lower()
    score = 0
    reasons = []

    # 🔹 Urgency & social engineering
    if any(w in text_l for w in ["urgent", "immediately", "asap", "action required"]):
        score += 25
        reasons.append("Uses urgency to pressure the user.")

    # 🔹 Credential harvesting keywords
    if any(w in text_l for w in ["login", "verify", "password", "otp"]):
        score += 30
        reasons.append("Requests sensitive authentication information.")

    # 🔹 Link detection
    urls = re.findall(r"(https?://[^\s]+)", text_l)
    if urls:
        score += 15
        reasons.append("Contains clickable link.")

        for url in urls:
            parsed = urlparse(url)

            # 🔸 IP-based URLs
            if re.match(r"\d+\.\d+\.\d+\.\d+", parsed.netloc):
                score += 25
                reasons.append("Uses IP address instead of domain name.")

            # 🔸 Suspicious TLDs
            if parsed.netloc.endswith((".xyz", ".top", ".ru", ".tk")):
                score += 20
                reasons.append("Uses high-risk top-level domain.")

            # 🔸 Too many subdomains
            if parsed.netloc.count(".") >= 3:
                score += 15
                reasons.append("Uses excessive subdomains to mimic trusted brands.")

    score = min(score, 100)

    verdict = "Phishing" if score >= 60 else "Suspicious" if score >= 30 else "Likely Safe"

    return f"""
⚠️ Threat Analysis Result

Verdict: {verdict}
Risk Score: {score}/100

Reasons:
- """ + "\n- ".join(reasons) + """

(Note: Demo mode using heuristic + URL intelligence. Gemini reasoning enabled in production.)
"""

import re

def extract_url(message):

    urls = re.findall(r'https?://\S+', message)

    if urls:
        return urls[0]

    return None


def calculate_threat_score(url):

    score = 0

    suspicious_words = [
        "login",
        "verify",
        "update",
        "bank",
        "secure",
        "account"
    ]

    if "https" not in url:
        score += 40

    if len(url) > 50:
        score += 30

    for word in suspicious_words:
        if word in url.lower():
            score += 20

    if "@" in url or "-" in url:
        score += 10

    if score > 100:
        score = 100

    return score


def check_url(message):

    url = extract_url(message)

    if not url:
        return "❌ No URL Found in Message"

    threat_score = calculate_threat_score(url)

    if threat_score >= 70:
        status = "🚨 HIGH RISK PHISHING URL"

    elif threat_score >= 40:
        status = "⚠ SUSPICIOUS URL"

    else:
        status = "✅ SAFE URL"

    return f"""
{status}

🔗 URL:
{url}

📊 Threat Score:
{threat_score}%
"""
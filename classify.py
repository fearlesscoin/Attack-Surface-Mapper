def classify_surface(endpoints, ports):
    high, medium, low = [], [], []

    for ep in endpoints:
        if "admin" in ep or "upload" in ep:
            high.append(ep)
        elif "login" in ep or "api" in ep:
            medium.append(ep)
        else:
            low.append(ep)

    for p in ports:
        if p in [22, 21]:
            medium.append(f"Port {p}")

    return {
        "high_risk": high,
        "medium_risk": medium,
        "low_risk": low
    }

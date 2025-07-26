import whois

def perform_whois(domain):
    try:
        w = whois.whois(domain)
        return str(w)
    except Exception as e:
        return f"WHOIS lookup failed: {e}"

import requests

def subdomains_crtsh(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        resp = requests.get(url, timeout=10)
        data = resp.json()
        subdomains = set()
        for entry in data:
            name = entry['name_value']
            for sub in name.split('\n'):
                if domain in sub:
                    subdomains.add(sub.strip())
        return list(subdomains)
    except Exception as e:
        return [f"Error: {e}"]

import requests

def detect_tech(domain):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        resp = requests.get("http://" + domain, headers=headers)
        server = resp.headers.get("Server", "Unknown")
        powered = resp.headers.get("X-Powered-By", "Unknown")
        return {
            "Server": server,
            "X-Powered-By": powered
        }
    except Exception as e:
        return {"Error": str(e)}

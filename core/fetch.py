# core/fetch.py
import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 FacultyResearchBot"
}


session = requests.Session()


def fetch(url, timeout=15):
    try:
        r = session.get(url, timeout=timeout, headers=HEADERS)
        if r.status_code != 200:
            return None, "error"
        return r.text, "static"
    except Exception:
        return None, "error"

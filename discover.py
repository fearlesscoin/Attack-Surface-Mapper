import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Common attacker-interest paths (for owned / lab targets only)
COMMON_PATHS = [
    "login",
    "login.php",
    "admin",
    "admin/login",
    "upload",
    "api",
    "dashboard"
]

def discover_endpoints(base_url, enable_guessing=True):
    endpoints = set()

    try:
        response = requests.get(base_url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract links from visible HTML
        for tag in soup.find_all("a", href=True):
            endpoints.add(urljoin(base_url, tag["href"]))

        for form in soup.find_all("form", action=True):
            endpoints.add(urljoin(base_url, form["action"]))

    except requests.RequestException:
        pass

    # Optional attacker-style path guessing (LAB / AUTHORIZED USE ONLY)
    if enable_guessing:
        for path in COMMON_PATHS:
            endpoints.add(urljoin(base_url, path))

    return list(endpoints)

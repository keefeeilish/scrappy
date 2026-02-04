# parsers/directory_parser.py

from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def extract_profile_links(html, base_url):
    soup = BeautifulSoup(html, "lxml")
    links = set()

    base_netloc = urlparse(base_url).netloc

    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if not href:
            continue

        full_url = urljoin(base_url, href)
        parsed = urlparse(full_url)

        # Must stay on same site
        if parsed.netloc != base_netloc:
            continue

        # Purdue faculty profiles live here
        if parsed.path.startswith("/people/faculty/"):
            # Ignore directory index pages
            if parsed.path.rstrip("/").endswith("faculty"):
                continue
            if parsed.path.endswith("index.html"):
                continue

            links.add(full_url)

    return sorted(links)

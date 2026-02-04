from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

from core.fetch import fetch
from extractors import contact, research

def extract_internal_links(html, base_url):
    soup = BeautifulSoup(html, "lxml")
    base_domain = urlparse(base_url).netloc
    links = set()

    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        full = urljoin(base_url, href)

        if urlparse(full).netloc == base_domain:
            links.add(full)

    return links


def crawl_personal_site(start_url, max_depth=2):
    visited = set()
    extracted = {}

    def dfs(url, depth):
        if depth > max_depth or url in visited:
            return

        visited.add(url)
        html, _ = fetch(url)
        if not html:
            return

        extracted.update(contact.extract(html))
        extracted.update(research.extract(html))

        for link in extract_internal_links(html, start_url):
            dfs(link, depth + 1)

    dfs(start_url, 0)
    return extracted

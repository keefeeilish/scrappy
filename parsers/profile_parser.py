# parsers/profile_parser.py
from extractors import contact, identity, research, links

def parse_profile(html, url):
    data = {}
    data.update(identity.extract(html))
    data.update(contact.extract(html))
    data.update(research.extract(html))
    data.update(links.extract(html))
    data["profile_page_url"] = url
    return data

import re
from utils.email_deobfuscator import extract_emails

def extract(html):
    emails = extract_emails(html)

    if not emails:
        return {}

    # Take the first email found (safe default)
    return {
        "email": emails[0]
    }

# utils/email_deobfuscator.py
import re

REPLACEMENTS = {
    r"\s*\[at\]\s*": "@",
    r"\s*\(at\)\s*": "@",
    r"\s+at\s+": "@",
    r"\s*\[dot\]\s*": ".",
    r"\s*\(dot\)\s*": ".",
    r"\s+dot\s+": "."
}

def deobfuscate(text):
    t = text.lower()
    for pat, rep in REPLACEMENTS.items():
        t = re.sub(pat, rep, t)
    return t

EMAIL_REGEX = r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}"

def extract_emails(text):
    clean = deobfuscate(text)
    return re.findall(EMAIL_REGEX, clean)

# core/renderer.py
def needs_js(html: str) -> bool:
    signals = [
        "enable javascript",
        "react-root",
        "__NEXT_DATA__",
        "data-reactroot",
        "ng-app"
    ]
    return any(s in html.lower() for s in signals)

def looks_js_heavy(html: str) -> bool:
    if not html:
        return True

    signals = [
        "enable javascript",
        "__NEXT_DATA__",
        "react-root",
        "data-reactroot",
        "ng-app"
    ]
    return any(s in html.lower() for s in signals)

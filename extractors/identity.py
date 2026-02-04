from bs4 import BeautifulSoup

def extract(html):
    soup = BeautifulSoup(html, "lxml")

    name = None
    title = None
    department = None

    h1 = soup.find("h1")
    if h1:
        name = h1.get_text(strip=True)

    text = soup.get_text(" ", strip=True).lower()

    for t in ["assistant professor", "associate professor", "professor"]:
        if t in text:
            title = t.title()
            break

    return {
        "full_name": name,
        "academic_title": title,
        "department": department
    }

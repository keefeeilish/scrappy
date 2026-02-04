# 🎓 University Faculty Scraper

A robust and extensible web scraper for extracting **publicly available university faculty information** from heterogeneous academic websites.  
Built to support **AI-driven personalized research outreach**, faculty profiling, and academic analytics.

---

## ✨ Features

- Scrapes faculty data from public university directories
- Handles **heterogeneous website layouts**
- Designed for **partial and noisy data**
- Schema-first design for downstream ML / NLP pipelines
- Modular, extensible architecture
- Outputs clean, structured JSON

---

## 📌 Data Collected

Depending on availability, the scraper can extract:

- Name  
- Academic title / designation  
- Department  
- Research interests  
- Email address (if publicly listed)  
- Personal / lab website  
- Academic links (Google Scholar, DBLP, etc.)  
- Source profile URL  
- University name  

> Missing fields are expected and handled gracefully.

---

## 🏗️ Project Structure

```
faculty-scraper/
│── scraper/
│   ├── fetch.py        # HTTP requests / page loading
│   ├── parse.py        # HTML parsing logic
│   ├── normalize.py   # Canonical schema mapping
│   └── utils.py       # Shared helpers
│
│── schemas/
│   └── faculty.json   # Canonical data schema
│
│── output/
│   └── sample.json    # Example scraped output
│
│── requirements.txt
│── .gitignore
│── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/faculty-scraper.git
cd faculty-scraper
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the scraper
```bash
python scraper/main.py
```

Scraped data will be saved in structured JSON format.

---

## 🧠 Design Philosophy

- **Resilience over perfection**  
  Academic websites change often — the scraper is built to survive layout drift.

- **Schema-first extraction**  
  Ensures consistent output across universities.

- **Ethical scraping**  
  Only publicly accessible information is collected, respecting `robots.txt`.

---

## 📄 Example Output

```json
{
  "name": "Dr. Jane Doe",
  "designation": "Associate Professor",
  "department": "Computer Science",
  "research_interests": [
    "Machine Learning",
    "Natural Language Processing"
  ],
  "email": "jane.doe@university.edu",
  "profile_url": "https://university.edu/faculty/jane-doe",
  "university": "Example University"
}
```

---

## 🛠️ Extending the Scraper

To add a new university:

1. Implement a parser in `parse.py`
2. Map extracted fields to the canonical schema
3. Register the parser in the dispatcher logic

The architecture is intentionally modular for easy expansion.

---

## ⚠️ Disclaimer

This project is intended **strictly for academic and research purposes**.

- Only public data is scraped  
- No authentication, paywalls, or private systems are bypassed  
- Users are responsible for complying with website policies and applicable laws  

---

## 📚 Use Cases

- Research internship outreach  
- Faculty profiling and academic collaboration  
- Dataset creation for personalization models  
- University-level academic analytics  

---

## 🤝 Contributions

Contributions are welcome.

Feel free to open an issue or submit a pull request to:
- Add support for new universities
- Improve parsing logic
- Enhance schema design
- Optimize performance

---

## ⭐ Motivation

Generic cold emails don’t work.  
This project exists to enable **meaningful, personalized academic outreach at scale**.

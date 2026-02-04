import argparse
import os
import re

from core.fetch import fetch
from parsers.directory_parser import extract_profile_links
from parsers.profile_parser import parse_profile
# Crawl Personal Site function was not being used, so I have temporarily removed it. Feel free to add it back later. 
# from parsers.personal_site_parser import crawl_personal_site
from output.writer import write_jsonl, write_csv


def slugify(name: str) -> str:
    name = name.lower()
    name = re.sub(r"[^a-z0-9]+", "_", name)
    return name.strip("_")


def run(university_directory_urls, university_name, fast=False):
    mode = "FAST" if fast else "FULL"
    print(f"[MODE] Running in {mode} mode")

    all_faculty = []

    university_slug = slugify(university_name)
    output_dir = os.path.join("output", university_slug, run_id)
    os.makedirs(output_dir, exist_ok=True)

    for directory_url in university_directory_urls:
        print(f"[DIR] Scraping directory: {directory_url}")

        html, _ = fetch(directory_url)

        profile_urls = extract_profile_links(html, directory_url)

        print(f"[INFO] Found {len(profile_urls)} profile URLs")

        if not html:
            print("[WARN] Failed to fetch directory")
            continue
        
        total = len(profile_urls)
        for idx, item in enumerate(profile_urls, start=1):
            # Normalize item (string vs dict)
            if isinstance(item, str):
                profile_url = item
                name_hint = None
            elif isinstance(item, dict):
                profile_url = item.get("profile_url")
                name_hint = item.get("full_name") or item.get("name")
            else:
                continue

            label = profile_url or name_hint or "UNKNOWN"

            print(f"[PROFILE {idx}/{total}] {label}")

            # CASE 1: Faculty has profile page
            if profile_url:
                profile_html, _ = fetch(profile_url)
                if not profile_html:
                    print("[WARN] Failed to fetch profile")
                    continue

                data = parse_profile(profile_html, profile_url)

                if name_hint and not data.get("full_name"):
                    data["full_name"] = name_hint

            # CASE 2: Directory-only faculty
            else:
                data = {
                    "full_name": name_hint,
                    "profile_page_url": None
                }

            # Shared metadata
            data["university_name"] = university_name
            data["source_directory_url"] = directory_url

            all_faculty.append(data)

            print(f"[OK] {data.get('full_name')}")



    write_jsonl(
        all_faculty,
        os.path.join(output_dir, "faculty.jsonl")
    )

    write_csv(
        all_faculty,
        os.path.join(output_dir, "faculty.csv")
    )


import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Scrape university faculty directory pages"
    )

    parser.add_argument(
        "--university",
        required=True,
        help="Name of the university being scraped"
    )

    parser.add_argument(
        "--fast",
        action="store_true",
        help="Enable fast mode (skip deep crawling, maximize speed)"
    )


    parser.add_argument(
        "urls",
        nargs="+",
        help="One or more faculty directory URLs"
    )

    args = parser.parse_args()

    run(args.urls, args.university)



if __name__ == "__main__":
    main()

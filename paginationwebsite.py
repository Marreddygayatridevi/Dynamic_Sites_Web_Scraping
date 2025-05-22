from playwright.sync_api import sync_playwright
import time
from rich import print
import html2text
import os
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def is_scrollable(page):
    prev_height = page.evaluate("() => document.body.scrollHeight")
    page.keyboard.press("End")
    time.sleep(2)
    new_height = page.evaluate("() => document.body.scrollHeight")
    return new_height > prev_height

def extract_pagination_urls_from_page(page, base_url):
    anchors = page.query_selector_all("a[href]")
    urls = set()
    for a in anchors:
        href = a.get_attribute("href")
        if href and ("page=" in href or "start=" in href):
            full_url = urljoin(base_url, href)
            urls.add(full_url)
    return urls

def close_popups(page):
    selectors = ["button[aria-label='Close']", ".close", ".popup-close", "[data-dismiss='modal']"]
    for selector in selectors:
        try:
            popup = page.query_selector(selector)
            if popup and popup.is_visible():
                popup.click()
                print(f" Closed popup: {selector}")
                time.sleep(1)
        except:
            pass

def save_combined_html(content):
    with open("final_combined.html", "w", encoding="utf-8") as f:
        f.write(content)

def convert_html_to_markdown(html_file="final_combined.html"):
    with open(html_file, "r", encoding="utf-8") as f:
        html = f.read()
    markdown = html2text.html2text(html)
    with open("final_combined.md", "w", encoding="utf-8") as f:
        f.write(markdown)
    print(" Markdown conversion complete.")

def combine_html_pages(html_list):
    soup = BeautifulSoup("<html><head><meta charset='utf-8'></head><body></body></html>", "html.parser")
    body = soup.body
    for html in html_list:
        page_soup = BeautifulSoup(html, "html.parser")
        page_body = page_soup.body
        if page_body:
            for child in page_body.contents:
                body.append(child)
    return str(soup)

def handle_paginated(page, base_url):
    print(" Handling paginated navigation...")
    visited = set()
    to_visit = [base_url]
    all_html_parts = []

    while to_visit:
        current_url = to_visit.pop(0)
        if current_url in visited:
            continue

        print(f"Scraping: {current_url}")
        try:
            page.goto(current_url, timeout=60000)
            time.sleep(3)
            close_popups(page)
            html = page.evaluate("() => document.documentElement.outerHTML")
            all_html_parts.append(html)
            visited.add(current_url)

            new_urls = extract_pagination_urls_from_page(page, base_url)
            for u in new_urls:
                if u not in visited and u not in to_visit:
                    to_visit.append(u)

        except Exception as e:
            print(f" Failed to load {current_url}: {e}")

    combined_html = combine_html_pages(all_html_parts)
    save_combined_html(combined_html)
    convert_html_to_markdown()

def detect_and_scrape(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.set_viewport_size({"width": 1280, "height": 1080})
        page.goto(url, timeout=60000)
        time.sleep(3)
        close_popups(page)

        print(f" Detecting page type: {url}")
        if is_scrollable(page):
            print(" Infinite scroll detected.")
            # TODO: Implement handle_scroll(page) if you want to support infinite scroll pages.
            print(" Infinite scroll handling is not implemented yet.")
        else:
            print("Pagination detected.")
            handle_paginated(page, url)

        browser.close()

if __name__ == "__main__":
    detect_and_scrape("https://www.adidas.co.in/women-shoes")
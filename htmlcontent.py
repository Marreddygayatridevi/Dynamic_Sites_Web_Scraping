from playwright.sync_api import sync_playwright
import time
from rich import print
import html2text

def scroll_me():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.set_viewport_size({"width": 1280, "height": 1080})

        # Navigate to target URL
        page.goto("https://salty.co.in/collections/sunglasses", timeout=60000)
        time.sleep(5)

        # Wait for content to load
        time.sleep(5)

        # Scroll down using End key
        for x in range(1, 15):
            page.keyboard.press("End")
            print(f"Scrolling key press {x}")
            time.sleep(1)

        # Save final HTML
        html = page.evaluate("() => document.documentElement.outerHTML")
        with open("final_page.html", "w", encoding="utf-8") as f:
            f.write(html)
        print(" HTML content saved to final_page.html")

        # Convert HTML to Markdown
        markdown_text = html2text.html2text(html)
        with open("final_page.md", "w", encoding="utf-8") as md_file:
            md_file.write(markdown_text)
        print(" Markdown content saved to final_page.md")

        browser.close()

if __name__ == "__main__":
    scroll_me()
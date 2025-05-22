# Playwright Web Scraper for Infinite Scroll Pages 
This script uses Playwright to automate scrolling through a webpage with infinite scroll behavior, capture the full page HTML, and convert it into Markdown.

# 📂 Project Structure (htmlcontent.py)

```
bash
.
├── htmlcontent.py          # Main script for scrolling and saving content
├── final_page.html         # Saved HTML after full scroll (auto-generated)
├── final_page.md           # Converted Markdown from HTML (auto-generated)
└── README.md
```

# 🚀 Features

- Opens the target URL using Chromium.

- Simulates scrolling by pressing the End key repeatedly.

- Waits between scrolls to let content load.

- Saves the full page HTML after scrolling.

- Converts HTML to Markdown using html2text.

# 🔧 Requirements

Install the following packages to run this script:

```
bash
pip install playwright rich html2text
```
```
bash
playwright install
```

# 📌 Notes

- The script uses time.sleep() to ensure the page has time to load after each scroll. You can adjust the sleep duration for different websites.

- Running in headless mode is turned off (headless=False) for debugging. Set it to True if you want to run without opening a browser window.

# ✍️ Author

Made with ❤ by Marreddy Gayatri Devi

# 📜 License
Free to use for personal and educational purposes.

#  E-commerce Web Scraper with Playwright (Pagination + Infinite Scroll Support)
This project provides two Python scripts that scrape dynamic e-commerce product pages using Playwright. It includes support for both pagination-based and infinite scroll-based websites and saves the final output as HTML and Markdown.

# 📂 Project Structure (htmlcontent.py)

```
bash
.
├── htmlcontent.py          # Main script for scrolling and saving content
├── final_page.html         # Saved HTML after full scroll (auto-generated)
├── final_page.md           # Converted Markdown from HTML (auto-generated)
└── README.md
```

# # 📂 Project Structure (paginationwebsite.py)

```
bash
.
├── paginationwebsite.py          # Main script for scrolling and saving content
├── final_page.html               # Saved HTML after full scroll (auto-generated)
├── final_page.md                 # Converted Markdown from HTML (auto-generated)
└── README.md
```

# 🚀 Features (htmlcontent.py )

- Opens the target URL using Chromium.

- Simulates scrolling by pressing the End key repeatedly.

- Waits between scrolls to let content load.

- Saves the full page HTML after scrolling.

- Converts HTML to Markdown using html2text.

# 📌 Features (paginationwebsite.py)

- Detects whether a page uses pagination or infinite scroll.

- Navigates through paginated pages by extracting page= or start= links.

- Closes popups automatically (supports common selectors).

- Combines HTML content from all visited pages.

- Converts combined HTML into Markdown format using html2text.



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

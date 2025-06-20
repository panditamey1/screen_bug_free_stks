# Screener HTML Parser

This repository contains a simple parser for extracting tables from screener.in HTML pages.

## Usage

1. Install dependencies:
   ```bash
   pip install beautifulsoup4
   ```

2. Run the parser on an HTML file:
   ```bash
   python parse_screener.py path/to/page.html
   ```

This will produce three CSV files in the current directory:

- `bulk_deals.csv`
- `block_deals.csv`
- `shareholdings.csv`

Sample HTML is provided in `data/sample.html` for testing.




























## Chrome extension: Save Screener HTML

A simple Chrome extension is provided in the `extension` folder. It saves the
current screener.in page's HTML to your Downloads folder using the page title
as the filename.

### Install
1. Open `chrome://extensions` in your browser.
2. Enable **Developer mode**.
3. Click **Load unpacked** and select the `extension` directory from this repo.

### Use
Navigate to a page on screener.in and click the extension icon. The page source
will be downloaded as an HTML file named after the page title.
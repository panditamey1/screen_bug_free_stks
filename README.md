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

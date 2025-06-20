import csv
from bs4 import BeautifulSoup
import sys


def parse_bulk_block_table(table):
    rows = []
    for tr in table.select('tbody tr'):
        cols = tr.find_all('td')
        if not cols:
            continue
        company = cols[0].get_text(strip=True, separator=' ')
        # extract date from span inside first td
        date_span = cols[0].find('span')
        date = date_span.get_text(strip=True) if date_span else ''
        # remove date from company text
        if date:
            company = company.replace(date, '').strip()
        txn_type = cols[1].get_text(strip=True)
        quantity = cols[2].get_text(strip=True)
        price = cols[3].get_text(strip=True)
        rows.append({
            'Company': company,
            'Date': date,
            'Type': txn_type,
            'Quantity': quantity,
            'Price': price,
        })
    return rows


def parse_shareholding_table(table):
    header_cells = table.select_one('thead tr').find_all('th')
    headers = ['Company'] + [th.get_text(strip=True) for th in header_cells[1:]]
    data = []
    for tr in table.select('tbody tr'):
        cells = tr.find_all('td')
        if not cells:
            continue
        row = [cells[0].get_text(strip=True)]
        for td in cells[1:]:
            row.append(td.get_text(strip=True))
        # ensure row has same length as headers
        while len(row) < len(headers):
            row.append('')
        data.append(dict(zip(headers, row)))
    return headers, data


def main(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # Bulk deals
    bulk_div = soup.find('div', id='bulk-deals')
    if bulk_div:
        bulk_table = bulk_div.find('table')
        bulk_rows = parse_bulk_block_table(bulk_table)
        with open('bulk_deals.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['Company', 'Date', 'Type', 'Quantity', 'Price'])
            writer.writeheader()
            writer.writerows(bulk_rows)

    # Block deals
    block_div = soup.find('div', id='block-deals')
    if block_div:
        block_table = block_div.find('table')
        block_rows = parse_bulk_block_table(block_table)
        with open('block_deals.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['Company', 'Date', 'Type', 'Quantity', 'Price'])
            writer.writeheader()
            writer.writerows(block_rows)

    # Shareholding
    share_div = soup.find('div', id='shareholdings')
    if share_div:
        share_table = share_div.find('table')
        headers, share_rows = parse_shareholding_table(share_table)
        with open('shareholdings.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(share_rows)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python parse_screener.py <html_file>')
        sys.exit(1)
    main(sys.argv[1])

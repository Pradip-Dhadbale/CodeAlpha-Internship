
"""Example: scrape Wikipedia 'List of countries and dependencies by population' table.
Save result to output/wikipedia_countries.csv
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time

URL = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
OUT_DIR = 'output'
os.makedirs(OUT_DIR, exist_ok=True)

headers = {'User-Agent': 'web-scraping-task1 (+https://example.com)'}  # replace with your contact or app info

def scrape():
    r = requests.get(URL, headers=headers, timeout=15)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'lxml')
    # The main table usually has class 'wikitable' and contains 'Country(or dependent territory)'
    table = soup.find('table', class_='wikitable')
    rows = []
    if not table:
        raise SystemExit('Could not find wikitable on the page.')
    for tr in table.find_all('tr')[1:]:
        cols = [td.get_text(strip=True).replace('\xa0', ' ') for td in tr.find_all(['th','td'])]
        if len(cols) >= 3:
            rank = cols[0]
            name = cols[1]
            population = cols[2].replace(',', '')
            rows.append({'Rank': rank, 'Country': name, 'Population': population})
    df = pd.DataFrame(rows)
    out_file = os.path.join(OUT_DIR, 'wikipedia_countries.csv')
    df.to_csv(out_file, index=False)
    print(f'Wrote {len(df)} rows to {out_file}')

if __name__ == '__main__':
    scrape()

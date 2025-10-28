
"""Example: scrape IMDb Top 250 movies (public page) and save basic info to CSV.
NOTE: IMDb may block automatic scraping; use responsibly and consider their API.
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os, time

URL = 'https://www.imdb.com/chart/top/'
OUT_DIR = 'output'
os.makedirs(OUT_DIR, exist_ok=True)
headers = {'User-Agent': 'web-scraping-task1 (+https://example.com)'}

def scrape():
    r = requests.get(URL, headers=headers, timeout=15)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'lxml')
    table = soup.find('tbody', class_='lister-list')
    rows = []
    if not table:
        raise SystemExit('Could not find top chart table.')
    for tr in table.find_all('tr'):
        title_col = tr.find('td', class_='titleColumn')
        rating_col = tr.find('td', class_='ratingColumn imdbRating')
        if title_col and rating_col:
            title = title_col.a.text.strip()
            year = title_col.span.text.strip('()')
            rating = rating_col.strong.text.strip() if rating_col.strong else ''
            rows.append({'Title': title, 'Year': year, 'Rating': rating})
    df = pd.DataFrame(rows)
    out_file = os.path.join(OUT_DIR, 'imdb_top250.csv')
    df.to_csv(out_file, index=False)
    print(f'Wrote {len(df)} rows to {out_file}')

if __name__ == '__main__':
    scrape()


# Web Scraping Task — Package (Task 1 of Data Analytics)

**What this package contains**
- `scripts/` — Example Python scripts using BeautifulSoup and a Scrapy project scaffold.
  - `scrape_wikipedia_countries.py` — BeautifulSoup script to scrape the *Wikipedia — List of countries by population* table and save as CSV.
  - `scrape_imdb_top250_bs4.py` — BeautifulSoup script to scrape the *IMDb Top 250* (example) and save as CSV.
  - `scrapy_project/` — A minimal Scrapy project scaffold with example spider (no external dependencies beyond Scrapy).
- `sample_dataset.csv` — A small sample dataset (3 rows) demonstrating expected output format from `scrape_wikipedia_countries.py`.
- `requirements.txt` — Python dependencies to install.
- `README.md` — This help file.

**How to use (quick)**
1. Create a virtual environment: `python -m venv venv && source venv/bin/activate` (or `venv\Scripts\activate` on Windows).
2. Install dependencies: `pip install -r requirements.txt`
3. Run an example script:
   - `python scripts/scrape_wikipedia_countries.py`
   - Output: `output/wikipedia_countries.csv`
4. Open CSV files with Excel / LibreOffice / pandas for analysis.

**Notes & ethics**
- These example scripts target public pages for educational use. Always check a site's `robots.txt` and terms of service before scraping.
- Add respectful time delays (e.g. `time.sleep(1)`) and limit request rates when running at scale.

**If you want modifications**
- The scripts are ready-to-run; edit the target URLs, selectors, or output filenames as needed.


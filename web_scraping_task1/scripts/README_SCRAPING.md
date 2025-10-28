
Quick notes about the example scripts:
- Each script uses `requests` + `BeautifulSoup` and writes CSV output to `output/`.
- They include a simple User-Agent header. Replace with your project's contact info when doing real scraping.
- Add rate-limiting and error handling for production use (try/except, retries, exponential backoff).
- To extend: parse more columns, normalize numbers/dates, or save to a database.

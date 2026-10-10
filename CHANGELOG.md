# Changelog

All notable changes to this project are documented in this file.

## [0.1.0] - 2026-10-10

### Added
- `scraper.py`: collects post titles and links from the Hacker News front page.
- Pagination: follows the "More" link, `--pages` sets how many pages to collect (default 1).
- `--delay` option: pause between page requests (default 1.0 s).
- CSV export (`--output`, default `hn_data.csv`) with columns `title`, `link`, `scraped_at` (UTC timestamp).
- Relative links (for example Ask HN posts) are resolved to full URLs.
- If a request fails, paging stops and the posts collected so far are saved; if nothing was collected, the script exits with an error.
- README with banner, workflow diagram, usage and example output (`assets/`, `sample_output.csv`).

# GFG NIT Srinagar Student Scraper

A Python-based Scrapy project that automates the collection of student coding statistics from GeeksforGeeks (GFG) for NIT Srinagar. This data is extracted via GFG's public API and exported to a clean CSV format, with scheduled scraping and live visualization support.

## 🔍 Features

- Scrapes paginated student data using GFG's public API.
- Extracts key metrics: username, coding score, problems solved, streak, and profile URL.
- Outputs structured data to a CSV file.
- Supports both manual and automated (scheduled) scraping via GitHub Actions.
- Data visualization powered by Streamlit.

## 🛠️ Tech Stack

- **Programming Language**: Python 3
- **Library** : Pandas
- **Web Scraping**: Scrapy
- **Automation**: GitHub Actions
- **Visualization**: Streamlit

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Aiyaan-Mahajan/nitsgr-gfg-stats-crawler.git
cd nitsgr-gfg-stats-crawler
```

### 2. Create and Activate Virtual Environment

#### macOS / Linux
```bash
python3 -m venv scrapy-env
source scrapy-env/bin/activate
```

#### Windows
```cmd
python -m venv scrapy-env
scrapy-env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install scrapy
```

### 4. Run the Scraper

```bash
scrapy crawl gfgnitsgrstudents -o output.csv
```

## 📄 Output Format

The generated `output.csv` contains the following columns:

- `user_id`
- `handle`
- `coding_score`
- `total_problems_solved`
- `potd_longest_streak`
- `profile_url`

## 📊 Automation & Visualization

- **Automation**: Scraping is scheduled daily via GitHub Actions (`cron`) and can also be triggered manually.
- **Visualization**: A companion Streamlit app presents the scraped data in an interactive UI.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> Feel free to fork, contribute, or use this as a template for similar scraping and visualization projects.

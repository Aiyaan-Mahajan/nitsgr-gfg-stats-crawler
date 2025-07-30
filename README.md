
# GFG NIT Srinagar Student Scraper

A professional Scrapy-based web scraper that collects student statistics from GeeksforGeeks for NIT Srinagar. It fetches data like username, coding score, total problems solved, and profile URL via their public API.

## Features

- Scrapes paginated student data using GFG's public API.
- Extracts structured statistics like coding score, problems solved, and profile links.
- Exports data to a clean CSV file.

## Tech Stack

- Python 3
- Scrapy

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/gfgnitsgrstudents.git
cd gfgnitsgrstudents
```

### 2. Create and Activate Virtual Environment

#### macOS / Linux

```bash
python3 -m venv scrapy-env
source scrapy-env/bin/activate
```

#### Windows (Command Prompt)

```cmd
python -m venv scrapy-env
scrapy-env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install scrapy
```

---

## Running the Scraper

Execute the following command to run the spider and export the data to a CSV file:

```bash
scrapy crawl gfgnitsgrstudents -o output.csv\n
```

This will create a CSV file containing the complete set of student data.

---

## Output CSV Columns

- user_id
- handle
- coding_score
- total_problems_solved
- potd_longest_streak
- profile_url

---

## License

This project is licensed under the MIT License.

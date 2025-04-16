# Job Processor

## Project Overview
The **Job Processor** project is a Python-based web scraper and data aggregator designed to extract job postings from `https://vacancymail.co.zw/jobs/`. The program consolidates the extracted data into a structured CSV file and includes an option to schedule scraping tasks. This script demonstrates key programming concepts, such as web scraping, data handling, and automation.

---

## Features
1. **Web Scraping**:
   - Scrapes the 10 most recently posted jobs.
   - Extracts relevant details, including job title, company name, location, expiration date, and description.

2. **Data Processing**:
   - Cleans the scraped data (e.g., removes duplicates, formats dates).

3. **Data Storage**:
   - Saves job listings in a structured CSV file with a timestamped filename.

4. **Automation**:
   - Optional scheduling feature to automate scraping tasks at regular intervals (e.g., daily, hourly).

5. **Error Handling & Logging**:
   - Logs key events and errors using the `logging` module for debugging and tracking.

---

## Prerequisites
Before running the program, ensure you have the following installed:
- Python 3.x
- Required Python packages:
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `schedule`

---

## Installation
1. Clone the repository or download the script file (`Job_Processor.py`).
2. Install dependencies using pip:
   ```bash
   pip install requests beautifulsoup4 pandas schedule
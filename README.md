# Scraping_Python-Libraries

A collection of Python scripts and projects demonstrating various web scraping techniques using popular libraries such as Scrapy, Selenium, BeautifulSoup, and Requests.

---

## About

This repository showcases multiple approaches to web scraping in Python. It includes complete Scrapy projects, Jupyter notebooks for interactive scraping, and scripts that combine Selenium, BeautifulSoup, and Requests to extract data from various websites. The goal is to provide practical examples for learning and reference.

---

## Folder & File Overview

| File/Folder                                | Description                                               |
|---------------------------------------------|-----------------------------------------------------------|
| `Amazon_Scrappy/`                          | Scrapy project for scraping Amazon product data           |
| `Scrappy_Amazon/`                          | Another Scrapy project focused on Amazon                  |
| `chromedriver-mac-x64`                     | ChromeDriver binary for Selenium automation               |
| `github_scrapping/`                        | Scripts for scraping GitHub data                          |
| `(scraper.py in jupyter_notebook).ipynb`   | Jupyter notebook demonstrating scraping techniques        |
| `Linkedin_Web_Scraper.ipynb`               | Notebook for scraping LinkedIn profiles                   |
| `Selenium with beautifulsoup.ipynb`        | Example combining Selenium and BeautifulSoup              |
| `Selenium_scrapping.ipynb`                 | Selenium-based web scraping notebook                      |
| `github(repo_list).ipynb`                  | Notebook for scraping GitHub repository lists             |
| `job_listings.csv`                         | Sample output: scraped job listings                       |
| `login.txt`                                | Stores login credentials for scraping (keep private)      |
| `scraping.log`                             | Log file for scraping activities                          |
| `test1.csv`                                | Sample output data                                        |

---

## Libraries Used

- **Scrapy**: For scalable, full-featured web crawling and scraping
- **Selenium**: For browser automation and scraping dynamic content
- **BeautifulSoup (bs4)**: For parsing and extracting data from HTML
- **Requests**: For making HTTP requests to web pages
- **Pandas**: For data processing and exporting to CSV
- **Jupyter Notebook**: For interactive development and demonstration

---

## Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package manager)
- Chrome browser (for Selenium)
- ChromeDriver (included as `chromedriver-mac-x64`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Than1612/Data-scraping_python-libraries.git
   cd Data-scraping_python-libraries
   ```

2. Install required libraries:
   ```bash
   pip install scrapy selenium beautifulsoup4 requests pandas jupyter
   ```

3. (Optional) Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

---

## Usage

- Explore the Jupyter notebooks (`*.ipynb`) to see example scraping workflows.
- Run Scrapy projects from their respective folders:
  ```bash
  cd Amazon_Scrappy
  scrapy crawl 
  ```
- Use Selenium scripts for dynamic sites. Make sure ChromeDriver is executable and in your PATH.

---

## Help

- Ensure your ChromeDriver version matches your Chrome browser.
- For login-based scraping, keep `login.txt` secure and never share credentials publicly.
- If you encounter errors, check `scraping.log` for troubleshooting information.

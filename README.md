# Web-Scraper
The Book Scraper is a Python-based web scraper that extracts book data from the Books to Scrape website. 

# Book Scraper Project

The Book Scraper is a Python-based web scraper that extracts book data from the [Books to Scrape](http://books.toscrape.com/) website. The scraper collects information such as book title, price, availability, and star rating, and saves the data to a CSV file.

## Project Structure

The project has the following structure:

```
BOOK_SCRAPER_PROJECT/
├── data/
│   └── books.csv
├── book_scraper/
│   ├── data/
│   │   └── books.csv
│   ├── main.py
│   └── requirements.txt
├── book_scraper_env/
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   └── pyvenv.cfg
├── README.md
└── .gitignore
```

- `data/`: This directory contains the output CSV file with the scraped book data.
- `book_scraper/`: This directory contains the Python script `main.py` and the `requirements.txt` file.
- `book_scraper_env/`: This directory contains the virtual environment for the project.


## Getting Started

1. **Clone the repository**:
   ```
   git clone https://github.com/your-username/book-scraper-project.git
   ```

2. **Create and activate the virtual environment**:
   ```
   cd book-scraper-project/book_scraper_env
   python -m venv .
   source bin/activate  # On Windows, use `.\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```
   cd ../book_scraper
   pip install -r requirements.txt
   ```

4. **Run the scraper**:
   ```
   python main.py
   ```

   The script will scrape the first 5 pages of the Books to Scrape website and save the data to `data/books.csv`.

## Features

- Scrapes book information (title, price, availability, star rating) from the Books to Scrape website.
- Saves the scraped data to a CSV file in the `data/` directory.
- Configures headers to mimic a browser request and adds random delays to prevent overwhelming the server.
- Handles errors and exceptions during the scraping process.


## License

This project is licensed under the [MIT License](LICENSE).

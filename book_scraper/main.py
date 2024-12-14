import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import os

class BookScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.books = []
        
        # Configure headers to mimic a browser request
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9'
        }

    def scrape_books(self, num_pages=5):
        """
        Scrape book information from multiple pages
        
        Args:
            num_pages (int): Number of pages to scrape
        """
        for page in range(1, num_pages + 1):
            try:
                # Construct page URL
                url = f"{self.base_url}/catalogue/page-{page}.html"
                
                # Add random delay to prevent overwhelming the server
                time.sleep(random.uniform(1, 3))
                
                # Send GET request
                response = requests.get(url, headers=self.headers)
                response.raise_for_status()  # Raise an exception for bad status codes
                
                # Parse HTML content
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Find all book elements
                book_elements = soup.find_all('article', class_='product_pod')
                
                # Extract information from each book
                for book in book_elements:
                    book_info = self.extract_book_details(book)
                    self.books.append(book_info)
                
                print(f"Scraped page {page}")
            
            except requests.RequestException as e:
                print(f"Error scraping page {page}: {e}")

    def extract_book_details(self, book_element):
        """
        Extract detailed information for a single book
        
        Args:
            book_element (bs4.element.Tag): Beautiful Soup book element
        
        Returns:
            dict: Book information
        """
        # Extract book title
        title = book_element.h3.a['title']
        
        # Extract price
        price = book_element.find('p', class_='price_color').text[1:]  # Remove £ symbol
        
        # Extract availability
        availability = book_element.find('p', class_='instock availability').text.strip()
        
        # Extract star rating
        star_rating = book_element.find('p', class_='star-rating')['class'][1]
        
        return {
            'Title': title,
            'Price': price,
            'Availability': availability,
            'Star Rating': star_rating
        }

    def save_to_csv(self, filename='data/books.csv'):
        """
        Save scraped books to a CSV file
        
        Args:
            filename (str): Path to save CSV file
        """
        # Ensure data directory exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        df = pd.DataFrame(self.books)
        df.to_csv(filename, index=False)
        print(f"Saved {len(self.books)} books to {filename}")

def main():
    # Specific URL for books to scrape (example site that allows scraping)
    base_url = 'http://books.toscrape.com'
    
    # Initialize and run scraper
    scraper = BookScraper(base_url)
    
    try:
        # Scrape multiple pages
        scraper.scrape_books(num_pages=5)
        
        # Save results
        scraper.save_to_csv()
    
    except Exception as e:
        print(f"An error occurred during scraping: {e}")

if __name__ == '__main__':
    main()
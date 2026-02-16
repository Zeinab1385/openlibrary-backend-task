"""
This script fetches books about Python from the Open Library API,
filters books published after 2000, and saves the data to a CSV file.
"""

from typing import List, TypedDict
import csv
import requests
from requests.adapters import HTTPAdapter, Retry

API_URL = "https://openlibrary.org/search.json?q=python&limit=58"
OUTPUT_FILE = "books.csv"
TIMEOUT = 10  # seconds


# ساختار داده‌ای که از API میاد
class BookAPIResponse(TypedDict, total=False):
    title: str
    language: List[str]
    first_publish_year: int
    ebook_access: str
    edition_count: int
    author_name: List[str]


# ساختار داده‌ای که برای CSV آماده می‌کنیم
class FilteredBook(TypedDict):
    title: str
    language: str
    publish_year: int | str
    ebook_access: str
    edition_count: int
    author: str


def fetch_books() -> List[BookAPIResponse]:
    """
    Fetch books from the Open Library API with retry mechanism.

    Returns:
        List of book dictionaries from the API response.
    """
    session = requests.Session()
    retries = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"],
    )
    session.mount("https://", HTTPAdapter(max_retries=retries))

    try:
        response = session.get(API_URL, timeout=TIMEOUT)
        response.raise_for_status()
        data = response.json()
        return data.get("docs", [])
    except requests.RequestException as error:
        print(f"Error fetching books: {error}")
        return []


def filter_books(books: List[BookAPIResponse]) -> List[FilteredBook]:
    """
    Filter books published after the year 2000 and format for CSV.
    """
    return [
        {
            "title": book.get("title", "N/A"),
            "language": ",".join(book.get("language", [])),
            "publish_year": book.get("first_publish_year", "N/A"),
            "ebook_access": book.get("ebook_access", "N/A"),
            "edition_count": book.get("edition_count", 0),
            "author": ",".join(book.get("author_name", [])),
        }
        for book in books
        if book.get("first_publish_year") and book["first_publish_year"] > 2000
    ]


def save_to_csv(books: List[FilteredBook]) -> None:
    """
    Save filtered books to a CSV file using csv.DictWriter.
    """
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=[
                "title",
                "language",
                "publish_year",
                "ebook_access",
                "edition_count",
                "author",
            ],
        )
        writer.writeheader()
        writer.writerows(books)


def main() -> None:
    """Main function to fetch, filter, and save books."""
    books = fetch_books()
    if not books:
        print("No books fetched. Exiting.")
        return

    filtered_books = filter_books(books)
    save_to_csv(filtered_books)
    print(f"{len(filtered_books)} books saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()

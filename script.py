import requests
import csv

API_URL = "https://openlibrary.org/search.json?q=programming&limit=50"
OUTPUT_FILE = "books.csv"


def fetch_books():
    response = requests.get(API_URL)
    response.raise_for_status()
    data = response.json()
    return data["docs"]


def filter_books(books):
    filtered = []

    for book in books:
        year = book.get("first_publish_year")

        if year and year > 2000:
            filtered.append({
                "title": book.get("title"),
                "author": ", ".join(book.get("author_name", [])),
                "year": year
            })

    return filtered


def save_to_csv(books):
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "author", "year"])
        writer.writeheader()
        writer.writerows(books)


def main():
    books = fetch_books()
    filtered_books = filter_books(books)
    save_to_csv(filtered_books)
    print(f"{len(filtered_books)} books saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()

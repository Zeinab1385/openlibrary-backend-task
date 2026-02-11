import requests
import csv

#API_URL = "https://openlibrary.org/search.json?q=programming&limit=50"
API_URL = "https://openlibrary.org/search.json?q=python&limit=58"
#API_URL = "https://openlibrary.org/search/authors.json?q=twain&limit=50"
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
                "title": book.get('title'),
                "language": ",".join(book.get('language', [])),
                "publish_year": book.get('first_publish_year'),
                "ebook_access": book.get('ebook_access'),
                "edition_count": book.get('edition_count'),
                "author": ",".join(book.get('author_name', [])),

            })

    return filtered

def save_to_csv(requested_books):
    with open("books.csv", "w", newline="", encoding="utf-8") as csvfile:
        csvfile.write(f"{'Title':<75}{'Language':<30}"
                    f"{'Publish Year':<15}{'Ebook Access':<25}"
                    f"{'Edition Count':<15}{'Author'}\n")
        csvfile.write("-" * 180 + "\n")

        for book in requested_books:
            csvfile.write(f"{book['title']:<75}"
                    f"{book['language']:<30}{book['publish_year']:<15}"
                    f"{str(book['ebook_access']):<25}"
                    f"{book['edition_count']:<15}{book['author']}\n")
        csvfile.close()


def main():
    books = fetch_books()
    filtered_books = filter_books(books)
    save_to_csv(filtered_books)
    print(f"{len(filtered_books)} books saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()

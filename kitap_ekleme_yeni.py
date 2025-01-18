import json
from datetime import datetime

# Book data storage
books = []

def save_data(filename, data):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

def load_data(filename):
    try:
        global books
        with open(filename, 'r', encoding='utf-8') as file:
            books = json.load(file)
    except FileNotFoundError:
        print("No existing data file found. Starting fresh.")
    except Exception as e:
        print(f"Error loading data: {e}")

# Kitap Ekleme

def add_book():
    try:
        book_barcode = input("Enter book barcode: ")
        if any(book["Barkod"] == book_barcode for book in books):
            print(f"Error: A book with barcode {book_barcode} already exists.")
            return

        title = input("Enter book title: ")
        author = input("Enter author name: ")
        publisher = input("Enter publisher name: ")
        language = input("Enter book language: ")
        price = float(input("Enter book price: "))
        publish_date = input("Enter publish date (YYYY-MM-DD): ")

        book = {
            "Barkod": book_barcode,
            "Kitap_Adi": title,
            "Yazar": author,
            "Yayinevi": publisher,
            "Dil": language,
            "Fiyat": price,
            "Yayin_Tarihi": publish_date,
            "Kutuphane_Kayit_Tarihi": datetime.now().strftime("%Y-%m-%d"),
        }
        books.append(book)
        save_data("kitap.json", books)
        print(f"Book '{title}' added successfully.")
    except Exception as e:
        print(f"Error adding book: {e}")

# Kitap Silme

def remove_book():
    try:
        barcode = input("Enter the barcode of the book to remove: ")
        global books
        book_to_remove = next((book for book in books if book["Barkod"] == barcode), None)
        if book_to_remove:
            books.remove(book_to_remove)
            save_data("kitap.json", books)
            print(f"Book '{book_to_remove['Kitap_Adi']}' with barcode {barcode} removed successfully.")
        else:
            print(f"No book found with barcode {barcode}.")
    except Exception as e:
        print(f"Error removing book: {e}")

# Kitap Arama

def search_books():
    try:
        print("Search options:")
        print("1. Search by title")
        print("2. Search by author")
        print("3. Search by barcode")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            query = input("Enter book title to search: ")
            results = [book for book in books if query.lower() in book["Kitap_Adi"].lower()]
        elif choice == "2":
            query = input("Enter author name to search: ")
            results = [book for book in books if query.lower() in book["Yazar"].lower()]
        elif choice == "3":
            query = input("Enter barcode to search: ")
            results = [book for book in books if book["Barkod"] == query]
        else:
            print("Invalid choice.")
            return

        if results:
            print("Search results:")
            for book in results:
                print(f"- {book['Kitap_Adi']} by {book['Yazar']} (Barcode: {book['Barkod']})")
        else:
            print("No books found matching the query.")
    except Exception as e:
        print(f"Error searching books: {e}")
# Kitapları Listeleme
def list_books():
    try:
        if not books:
            print("No books in the library.")
        else:
            print("Library books:")
            for book in books:
                print(f"- Title: {book['Kitap_Adi']}, Author: {book['Yazar']}, Barcode: {book['Barkod']}, Price: {book['Fiyat']}")
    except Exception as e:
        print(f"Error listing books: {e}")
    
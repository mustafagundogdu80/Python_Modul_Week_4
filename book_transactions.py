# Book operations
def add_book(book_barcode, title, author, publisher, language, price, publish_date):
    try:
        if any(book["Barkod"] == book_barcode for book in books):
            print(f"Error: A book with barcode {book_barcode} already exists.")
            return

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
        save_data(kitap.json, books)
        print(f"Book '{title}' added successfully.")
    except Exception as e:
        print(f"Error adding book: {e}")

def remove_book(barcode):
    try:
        global books
        books = [book for book in books if book["Barkod"] != barcode]
        save_data(kitap.json, books)
        print(f"Book with barcode {barcode} removed successfully.")
    except Exception as e:
        print(f"Error removing book: {e}")

def search_books(query):
    try:
        results = [book for book in books if query.lower() in book["Kitap_Adi"].lower()]
        return results
    except Exception as e:
        print(f"Error searching books: {e}")
        return []

def get_book_by_barcode(barcode):
    try:
        for book in books:
            if book["Barkod"] == barcode:
                return book
        return None
    except Exception as e:
        print(f"Error retrieving book by barcode: {e}")
        return None

# book_transactions.py
import file_transactions, drawing
import os

def add_book(books, books_file):
    """
    Adds a new book to the list of books.
    """
    barcode = int(input("Enter the book's barcode: "))
    title = input("Enter the book's title: ")
    author = input("Enter the book's author: ")
    publisher = input("Enter the book's publisher: ")
    language = input("Enter the book's language: ")
    price = float(input("Enter the book's price: "))
    book = dict()
    book["Barkod"] = barcode
    book["Kitap_Adi"]= title
    book["Yazar"]= author
    book["Yayinevi"]= publisher
    book["Dil"]= language
    book["Fiyat"]= price
    books.append(book)
    print("Book added successfully.")
    file_transactions.save_file(books_file, books)
    return books

def update_book(books, books_file):
    """
    Updates the information of a book.
    """
    book_barcode = int(input("Enter the book's barcode: "))
    for book in books:
        if book["Barkod"] == book_barcode:
            title = input("Enter the book's new title: ")
            author = input("Enter the book's new author: ")
            publisher = input("Enter the book's new publisher: ")
            language = input("Enter the book's new language: ")
            price = float(input("Enter the book's new price: "))
            book["Kitap_Adi"] = title
            book["Yazar"] = author
            book["Yayinevi"] = publisher
            book["Dil"] = language
            book["Fiyat"] = price
            print("Book updated successfully.")
            file_transactions.save_file(books_file, books)
            return books
    print("Book not found.")
    return books

def search_books(books):
    """
    Searches for books based on a given criteria.
    """
    search_dicttionary = {}
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("Search Criteria:")
        print("1. Barcode")
        print("2. Title")
        print("3. Author")
        print("4. Publisher")
        print("5. Language")
        print("6. Price")
        print("Q. Exit")
        print("Now, choose your search criteria: ")
        for i in search_dicttionary:
            print(i," : ", search_dicttionary[i])
        Choose = input("Enter your choice: ")
        if Choose in ["Q", "q", "exit", "quit"]:
            break
        elif Choose == "1":
            search_dicttionary["Barkod"] = int(input("Enter the book's barcode: "))
        elif Choose == "2":
            search_dicttionary["Kitap_Adi"] = input("Enter the book's title: ")
        elif Choose == "3":
            search_dicttionary["Yazar"] = input("Enter the book's author: ")
        elif Choose == "4":
            search_dicttionary["Yayinevi"] = input("Enter the book's publisher: ")
        elif Choose == "5":
            search_dicttionary["Dil"] = input("Enter the book's language: ")
        elif Choose == "6":
            search_dicttionary["Fiyat"] = float(input("Enter the book's price: "))
        else:
            print("Invalid choice.")

    list_books(books, search_dicttionary)

    
def delete_book(books, books_file):
    """
    Deletes a book from the list of books.
    """
    book_barcode = int(input("Enter the book's barcode: "))
    for book in books:
        if book["Barkod"] == book_barcode:
            books.remove(book)
            print("Book deleted successfully.")
            file_transactions.save_file(books_file, books)
            return books
    print("Book not found.")
    return books

def list_books(books, kwargs=None):
    """
    Lists all the books in the library.
    """
    if kwargs:
        books_list = []
        for book in books:         
            for key, value in kwargs.items():
                if book[key] == value:
                    books_list.append(book)
    else:
        books_list = books

    for i in drawing.create_grid(books_list, ["Barkod", "Kitap_Adi", "Yazar", "Yayinevi", "Dil", "Fiyat"], [17, 80, 50, 70, 20, 10], "Kitaplar"):
        print(i)


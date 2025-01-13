# time_transactions.py
import file_transactions, drawing
import datetime

def book_lending(books, members, trancings, trancings_file, books_file):
    """
    Records the borrowing of a book by a member.
    """
    book_barcode = int(input("Enter the book's barcode: "))
    member_id = int(input("Enter the member's ID: "))
    for book in books:
        if book["Barkod"] == book_barcode:
            for member in members:
                if member["id"] == member_id:
                    trancing = {
                        "id": member["id"],
                        "name": member["name"],
                        "tel": member["tel"],
                        "address": member["address"],
                        "Barkod": book["Barkod"],
                        "Kitap_Adi": book["Kitap_Adi"],
                        "Yazar": book["Yazar"],
                        "Yayinevi": book["Yayinevi"],
                        "Dil": book["Dil"],
                        "Fiyat": book["Fiyat"],
                        "lending_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "return_date": (datetime.datetime.now()+ datetime.timedelta(days=14)).strftime("%Y-%m-%d")
                    }
                    trancings.append(trancing)
                    print("Book lending successfully.")
                    books.remove(book)
                    file_transactions.save_file(trancings_file, trancings)
                    file_transactions.save_file(books_file, books)
                    return trancings, books
            print("Member not found.")
            return trancings, books
    print("Book not found.")
    return trancings, books

def book_return(books, trancings, trancings_file, books_file):
    """
    Records the return of a book by a member.
    """
    book_barcode = int(input("Enter the book's barcode: "))
    member_id = int(input("Enter the member's ID: "))
    for trancing in trancings:
        if trancing["id"] == member_id and trancing["Barkod"] == book_barcode:
            book = {
                "Barkod": trancing["Barkod"],
                "Kitap_Adi": trancing["Kitap_Adi"],
                "Yazar": trancing["Yazar"],
                "Yayinevi": trancing["Yayinevi"],
                "Dil": trancing["Dil"],
                "Fiyat": trancing["Fiyat"]  
            }
            books.append(book)
            trancings.remove(trancing)
            file_transactions.save_file(trancings_file, trancings)
            file_transactions.save_file(books_file, books)
            print("Book returned successfully.")
            return trancings, books
    print("Book not found.")
    return trancings,  books

def list_trancings(trancings, kwargs=None):
    """
    Lists all trancings.
    """
    if kwargs :
        trancings_list = []
        for trancing in trancings:
            for key, value in kwargs.items():
                if trancing[key] == value:
                    trancings_list.append(trancing)
    else:
        trancings_list = trancings
    for i in drawing.create_grid(trancings_list, ["id", "name", "tel", "address", "Barkod", "Kitap_Adi", "Yazar", "Yayinevi", "Dil", "Fiyat", "lending_date", "return_date"],[5, 25, 13, 30, 17, 30, 25, 30, 15, 7, 21, 15],"Trancings"):
        print(i)
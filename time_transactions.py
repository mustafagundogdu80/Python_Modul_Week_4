import datetime
import file_transactions as file_transactions

book_file = "kitap.json"
members_file = "uye.json"
trancings_file = "tracking.json"
 

def book_lending(books, members, trancings, trancings_file, books_file):
    """
    Records the borrowing of a book.
    """
    book_barcode = input("Enter the book's barcode: ")
    member_id = input("Enter the member's ID: ")
    
    # Kitabı ve üyeyi doğrula
    book = None
    for b in books:
        if str(b["Barkod"]) == book_barcode:
            book = b
            break

    member = None
    for m in members:
        if str(m["id"]) == member_id:
            member = m
            break

    if not book:
        print("Book not found.")
        return trancings, books
    if not member:
        print("Member not found.")
        return trancings, books

    # Ödünç alma ve teslim tarihleri
    lending_date = datetime.datetime.now()
    return_date = lending_date + datetime.timedelta(days=14)

    # Yeni takip kaydı
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
        "lending_date": lending_date.strftime("%Y-%m-%d"),
        "return_date": return_date.strftime("%Y-%m-%d")
    }

    #strftime - strftime (string format time), 

    # Python'da datetime nesnelerini belirli bir string formatında ifade etmek için kullanılan bir metottur.
    #  Tarih ve saati insan tarafından okunabilir bir metin haline dönüştürür.
    
    #     Yaygın Format Kodları
    # %Y: Yıl (4 basamaklı)
    # %m: Ay (01-12)
    # %d: Gün (01-31)
    # %H: Saat (00-23)
    # %M: Dakika (00-59)
    # %S: Saniye (00-59)

    trancings.append(trancing)
    books.remove(book)
    file_transactions.save_file(trancings_file, trancings)
    file_transactions.save_file(books_file, books)

    print(f"Book lent successfully. Return by {return_date.strftime('%Y-%m-%d')}.")
    return trancings, books

def book_return(books, trancings, trancings_file, books_file):
    """
    Records the return of a book.
    """
    book_barcode = input("Enter the book's barcode: ")
    member_id = input("Enter the member's ID: ")

    # Takip kaydını bul
    trancing = None
    for t in trancings:
        if str(t["Barkod"]) == book_barcode and str(t["id"]) == member_id:
            trancing = t
            break

    if not trancing:
        print("Transaction not found.")
        return trancings, books

    # Kitabı geri ekle
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

def list_trancings(trancings):
    """
    Displays all active trancings.
    """
    if not trancings:
        print("No active trancings found.")
        return

    print("Current Trancings:")
    for t in trancings:
        print(f"Member ID: {t['id']}, Book Barcode: {t['Barkod']}, Lending Date: {t['lending_date']}, Return Date: {t['return_date']}")


# Python Library
import os

#Special Library
import book_transactions as bt
import membership_transactions as mt
import time_transactions as tt
import file_transactions as ft

if __name__ == '__main__':
    book_file = 'kitap.json'
    members_file = 'uye.json'
    trancings_file = 'tracking.json'
    books = ft.load_file(book_file)
    members = ft.load_file(members_file)
    trancings = ft.load_file(trancings_file)
    incorrectly_entered = False
    exit_confirmation = True
    main_menu = ["╔════════════════════════════════════════════════════════════╗ ",
                "║                 WELCOME TO PUBLIC LIBRARY                  ║ ",
                "╠════════════════════════════════════════════════════════════╣ ",
                "║                                                            ║ ",
                "║                (1) Members Transactions                    ║ ",
                "║                (2) Book Transactions                       ║ ",
                "║                                                            ║ ",
                "╠════════════════════════════════════════════════════════════╣ ",
                "║                   (Q) Quit / Exit (E)                      ║ ",
                "╚════════════════════════════════════════════════════════════╝ "
                ]
    while exit_confirmation:
        os.system("cls" if os.name == "nt" else "clear")
        for i in main_menu:
            print(i)
        if incorrectly_entered:
            print("Incorrect choice. Please try again.")
            incorrectly_entered = False
        choice = input("Enter your choice: ")
        # Choise menu
        if choice in ["q", "Q", "exit", "EXIT", "6"]:
            exit_confirmation = False
        elif choice == "1":
            exit_members_menu = True
            while exit_members_menu:
                os.system("cls" if os.name == "nt" else "clear")
                book_menu = ["╔════════════════════════════════════════════════════════════════════════╗ ",
                            "║                        WELCOME TO PUBLIC LIBRARY                       ║ ",
                            "╠══════════════════════════════════╦═════════════════════════════════════╣ ",
                            "║          MEMBERS MENU            ║           TRACKING MENU             ║ ",
                            "╠══════════════════════════════════╬═════════════════════════════════════╣ ",
                            "║                                  ║                                     ║ ",
                            "║        (1) Members               ║        (5) Lending a books          ║ ",
                            "║        (2) Add a new members     ║        (6) Returning a book         ║ ",
                            "║        (3) Search a members      ║        (7) Book Tracking            ║ ",
                            "║        (4) Delete a members      ║        (8) Search a book            ║ ",
                            "║                                  ║                                     ║ ",
                            "╠══════════════════════════════════╩═════════════════════════════════════╣ ",
                            "║                         (Q) Quit / Exit (E)                            ║ ",
                            "╚════════════════════════════════════════════════════════════════════════╝ "
                            ]
                for i in book_menu:
                    print(i)
                if incorrectly_entered:
                    print("Incorrect choice. Please try again.")
                    incorrectly_entered = False
                choice = input("Enter your choice: ")
                if choice in ["q", "Q", "exit", "EXIT"]:
                    exit_members_menu = False
                elif choice == "1":
                    try:
                        mt.list_members(members)
                    except Exception as e:
                        print("An Error Occurred:", e)
                    input("Press Enter to continue...")
                elif choice == "2":
                    try:
                        members = mt.add_member(members, members_file)
                    except Exception as e:
                        print("An Error Occurred:", e)
                    input("Press Enter to continue...")
                elif choice == "3":
                    try:
                        mt.search_members(members)
                    except Exception as e:
                        print("An Error Occurred:", e)
                    input("Press Enter to continue...")
                elif choice == "4":
                    try:
                        members = mt.delete_member(members, members_file)
                    except Exception as e:
                        print("An Error Occurred:", e)
                    input("Press Enter to continue...")
                elif choice == "5":
                    try:
                        trancings, books = tt.book_lending(books, members, trancings, trancings_file, book_file)
                    except Exception as e:
                        print("An Error Occurred:", e)
                    input("Press Enter to continue...")
                elif choice == "6":
                    try:
                        trancings, books = tt.book_return(books, trancings, trancings_file, book_file)
                    except Exception as e:
                        print("An Error Occurred:", e)
                    input("Press Enter to continue...")
                elif choice == "7":
                    try:
                        tt.list_trancings(trancings)
                    except Exception as e:
                        print("An Error Occurred:", e)
                    input("Press Enter to continue...")
                elif choice == "8":
                    try:
                        bt.search_books(books)
                    except Exception as e:
                        print("An error occurred:", str(e))
                    input("Press Enter to continue...")
                else:
                    incorrectly_entered = True
        elif choice == "2":
            exit_books_menu = True
            while exit_books_menu:
                os.system("cls" if os.name == "nt" else "clear")
                book_menu = ["╔════════════════════════════════════════════════════════════╗ ",
                            "║                 WELCOME TO PUBLIC LIBRARY                  ║ ",
                            "║                        BOOKS MENU                          ║ ",
                            "╠════════════════════════════════════════════════════════════╣ ",
                            "║                                                            ║ ",
                            "║                (1) Books                                   ║ ",
                            "║                (2) Add a new book                          ║ ",
                            "║                (3) Search a book                           ║ ",
                            "║                (4) Delete a book                           ║ ",
                            "║                                                            ║ ",
                            "╠════════════════════════════════════════════════════════════╣ ",
                            "║                     (Q) Quit / Exit                        ║ ",
                            "╚════════════════════════════════════════════════════════════╝ "
                            ]
                for i in book_menu:
                    print(i)
                choice = input("Enter your choice: ")
                if choice in ["q", "Q", "exit", "EXIT"]:
                    exit_books_menu = False
                elif choice == "1":
                    try:
                        bt.list_books(books)
                    except Exception as e:
                        print("An error occurred:", str(e))
                    input("Press Enter to continue...")
                elif choice == "2":
                    try:
                        bt.add_book(books, book_file)
                    except Exception as e:
                        print("An error occurred:", str(e))
                    input("Press Enter to continue...")
                elif choice == "3":
                    try:
                        bt.search_books(books)
                    except Exception as e:
                        print("An error occurred:", str(e))
                    input("Press Enter to continue...")
                elif choice == "4":
                    try:
                        bt.delete_book(books, book_file)
                    except Exception as e:
                        print("An error occurred:", e)
                    input("Press Enter to continue...")
        else:
            incorrectly_entered = True
    else:
        print("Thank you for using Public Library Manager. Goodbye!")
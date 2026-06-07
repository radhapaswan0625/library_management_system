from book import Book
from library import Library

library = Library()
library.load_from_file()

while True:
    print("\n==== LIBRARY MENU ====")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Save and Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        book_id = int(input("Enter Book ID: "))
        title = input ("Enter Title: ")
        author = input("Enter Author:")
        quantity = int(input("Enter Quantity: "))

        book = Book(book_id, title, author, quantity)
        library.add_book(book)

        print("Book added Scuccessfully!")

    elif choice == "2":
        library.show_books()

    elif choice == "3":
        title = input("Enter book title:")
        library.search_books(title)

    elif choice == "4":
        book_id = int(input("Enter Book ID to delete: "))
        library.delete_book(book_id)

    elif choice == "5":
        book_id = int(input("Enter Book ID to issue: "))
        library.issue_book(book_id) 

    elif choice == "6":
        book_id = int(input("Enter Book ID to return: "))
        library.return_book(book_id)  

    elif choice == "7":
        library.save_to_file()
        print("Saved and Exiting....")
        break 

    else:
        print("Invalid Choice")   





import json
from book import Book


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)    

    def show_books(self):
        for book in self.books:
            print("Book ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)
            print("Quantity:", book.quantity)
            print("------------------")

    def search_books(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print("\nBook Found!")
                print("------------------------------------")
                print("\nBook Id:", book.book_id)
                print("Title:", book.title)
                print("Author:", book.author)
                print("Quantity:", book.quantity)
                print("------------------------------------")
                return
        print("Book Not Found")

    def save_to_file(self):
        data = []

        for book in self.books:
            data.append({
                "book_id":book.book_id,
                "title":book.title,
                "author":book.author,
                "quantity":book.quantity
            })

        with open("books.json", "w") as file:
                json.dump(data, file, indent=4)   

    def load_from_file(self):
        try:
            with open("books.json", "r") as file:
                data = json.load(file)

                for item in data:
                    book = Book(
                        item["book_id"], 
                        item["title"],
                        item["author"],
                        item["quantity"]
                    )  
                    self.books.append(book)

        except FileNotFoundError:
            print("No saved file found. starting fresh......") 


    def delete_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print("Book deleted successfully!")
                return

        print("Book not found ") 

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:

                if book.quantity > 0:
                    book.quantity -= 1
                    print("Book issued successfully!")
                else:
                    print("Book is out of stock!")

                return
        print("Book not found")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.quantity += 1
                print("Book returned successfully!")
                return

        print("Book not found")    
                





    
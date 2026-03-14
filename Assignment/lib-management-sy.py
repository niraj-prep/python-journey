#Library Management System

class Book:
    def __init__(self, book_id, title, author):
        self.book_id   = book_id
        self.title     = title
        self.author    = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Lent Out"
        print(f"  ID: {self.book_id} | Title: {self.title} | "
              f"Author: {self.author} | Status: {status}")


class Member:
    def __init__(self, member_id, name):
        self.member_id    = member_id
        self.name         = name
        self.borrowed_books = []

    def display(self):
        print(f"  Member ID: {self.member_id} | Name: {self.name} | "
              f"Books Borrowed: {len(self.borrowed_books)}")


class Library:
    def __init__(self):
        self.books   = {}
        self.members = {}

    # ── Book operations ───────────────────────────────────────────
    def add_book(self):
        bid    = input("Enter Book ID   : ")
        title  = input("Enter Title     : ")
        author = input("Enter Author    : ")
        if bid in self.books:
            print("Book ID already exists.")
        else:
            self.books[bid] = Book(bid, title, author)
            print(f"Book '{title}' added successfully.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\n--- All Books ---")
            for book in self.books.values():
                book.display()

    # ── Member operations ─────────────────────────────────────────
    def add_member(self):
        mid  = input("Enter Member ID  : ")
        name = input("Enter Name       : ")
        if mid in self.members:
            print("Member ID already exists.")
        else:
            self.members[mid] = Member(mid, name)
            print(f"Member '{name}' added successfully.")

    # ── Lending / Returning ───────────────────────────────────────
    def lend_book(self):
        mid = input("Enter Member ID : ")
        bid = input("Enter Book ID   : ")
        if mid not in self.members:
            print("Member not found.")
            return
        if bid not in self.books:
            print("Book not found.")
            return
        book   = self.books[bid]
        member = self.members[mid]
        if not book.available:
            print("Book is not available right now.")
        else:
            book.available = False
            member.borrowed_books.append(bid)
            print(f"Book '{book.title}' lent to {member.name}.")

    def return_book(self):
        mid = input("Enter Member ID : ")
        bid = input("Enter Book ID   : ")
        if mid not in self.members:
            print("Member not found.")
            return
        if bid not in self.books:
            print("Book not found.")
            return
        member = self.members[mid]
        if bid not in member.borrowed_books:
            print("This member did not borrow this book.")
        else:
            self.books[bid].available = True
            member.borrowed_books.remove(bid)
            print(f"Book '{self.books[bid].title}' returned successfully.")


# ── Menu-driven interface ──────────────────────────────────────────
def main():
    lib = Library()

    menu = """
╔══════════════════════════════╗
║   Library Management System  ║
╠══════════════════════════════╣
║ 1. Add Book                  ║
║ 2. Add Member                ║
║ 3. Lend Book                 ║
║ 4. Return Book               ║
║ 5. Display All Books         ║
║ 6. Exit                      ║
╚══════════════════════════════╝"""

    while True:
        print(menu)
        choice = input("Enter your choice: ").strip()

        if   choice == '1': lib.add_book()
        elif choice == '2': lib.add_member()
        elif choice == '3': lib.lend_book()
        elif choice == '4': lib.return_book()
        elif choice == '5': lib.display_books()
        elif choice == '6':
            print("Exiting Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
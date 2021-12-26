from models import Book
from database import SessionLocal

session = SessionLocal()


def add_book():
    title = input("\nBook Title: ")
    author = input("Author: ")
    date_published = input("Published (Example: January 13, 2003): ")
    price = input("Price (Example: 10.99): ")

    new_book = Book(title=title, author=author, date_published=date_published, price=price)
    session.add(new_book)
    session.commit()
    session.close()
    print("Book added!\n")


def get_all_books():
    print("\nALL BOOKS")
    all_books = session.query(Book).order_by(Book.id)
    for book in all_books:
        print(
            f"Book id: {book.id}, Title: {book.title}, Author: {book.author}, Published: {book.date_published}, Price: {book.price}"
        )

from colorama.ansi import Fore
from models import Book
from database import SessionLocal
import time
import keyboard
import datetime


session = SessionLocal()


def add_book():
    title = input("\nBook Title: ")
    author = input("Author: ")
    date_published = input("Published (Example: January 13, 2003): ")
    price = input("Price (Example: 10.99): ")
    try:
        date_published = date_published.split(" ")
        date_published = datetime.date(
            int(date_published[2]),
            datetime.datetime.strptime(date_published[0], "%B").month,
            int(date_published[1].strip(",")),
        )
        new_book = Book(title=title, author=author, date_published=date_published, price=price)
        session.add(new_book)
        session.commit()
        session.close()
        print("Book added!\n")
    except Exception as error:
        print("\nPlease try again.\nError found in input: ", error)
    time.sleep(1)


def get_all_books():
    print(f"\n{Fore.CYAN}ALL BOOKS{Fore.RESET}")
    all_books = session.query(Book).order_by(Book.id)
    if all_books.count() == 0:
        print(f"\n{Fore.RED}No books found.{Fore.RESET}")
    for book in all_books:
        print(
            f"Book id: {book.id}, Title: {book.title}, Author: {book.author}, Published: {book.date_published}, Price: {book.price}"
        )
    time.sleep(1)


def search_for_book():
    book_ids = [book.id for book in session.query(Book).order_by(Book.id)]
    if len(book_ids) == 0:
        print(f"\n{Fore.RED}No books found.{Fore.RESET}")
        time.sleep(1)
        return
    print(f"\nOptions: {book_ids}")
    book_id = input("What is the book's id? ")
    searched_book = session.query(Book).filter_by(id=int(book_id)).first()
    print(type(searched_book))
    print(
        f"\n{searched_book.title} by {searched_book.author}\nPublished: {searched_book.date_published}\nCurrent Price: {searched_book.price}\n"
    )
    operation = input(
        f"1) {Fore.GREEN}Edit entry{Fore.RESET}\n2) {Fore.RED}Delete entry{Fore.RESET}\n3) Search for another book\n4) Return to main menu\n\nWhat would you like to do? "
    )

    def update_detail(property, text):
        keyboard.write(property)
        updated_property = input(text)
        return updated_property

    if operation == "1":
        print("\nEnter new details")
        searched_book.title = update_detail(searched_book.title, "Title: ")
        searched_book.author = update_detail(searched_book.author, "Author: ")
        searched_book.date_published = update_detail(searched_book.date_published, "Published: ")
        searched_book.price = update_detail(searched_book.price, "Price: ")

        session.commit()
        session.close()
        print("Book updated!")

    elif operation == "2":
        session.delete(searched_book)
        session.commit()
        session.close()
        print("Book deleted!")

    elif operation == "3":
        return search_for_book()

    time.sleep(1)


def book_analysis():
    books = session.query(Book).order_by(Book.date_published)
    if books.count() == 0:
        print("\nNo books in library.")
        time.sleep(1)
        return
    try:
        print(
            f"\nNewest book: <Title: {books[0].title}, Author: {books[0].author}, Published: {books[0].date_published}, Price: {books[0].price}>"
        )
        print(
            f"Oldest book: <Title: {books[-1].title}, Author: {books[-1].author}, Published: {books[-1].date_published}, Price: {books[-1].price}>"
        )
        print(f"Total Number of Books: {books.count()}")

        python_books = session.query(Book).filter(Book.title.ilike("%python%")).all()

        print(f"Total Number of Python Books: {len(python_books)}")
    except Exception as error:
        print("Error: ", error)

    time.sleep(1)

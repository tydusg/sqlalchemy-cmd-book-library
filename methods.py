from colorama.ansi import Fore
from models import Book
from database import SessionLocal
import time
import keyboard
import datetime


session = SessionLocal()


def return_to_menu():
    input(f"\nPress {Fore.GREEN}'ENTER'{Fore.RESET} to return to menu. ")


def add_book():
    def clean_date(date):
        """Takes in a date of form (LongMonth DD, YYYY) and
        converts it to a tuple of form (YYYY, MM, DD)
        """
        date = date.split(" ")
        return datetime.date(
            int(date[2]),
            datetime.datetime.strptime(date[0], "%B").month,
            int(date[1].strip(",")),
        )

    title = input("\nBook Title: ")
    author = input("Author: ")
    date_published = input("Published (Example: January 13, 2003): ")
    price = input("Price (Example: 10.99): ")
    try:
        date_published = clean_date(date_published)
        price = round(float(price), 2)
        new_book = Book(title=title, author=author, date_published=date_published, price=price)
        session.add(new_book)
        session.commit()
        session.close()
        print("Book added!\n")
    except Exception as error:
        print("\nPlease try again.\nError found in input: ", error.__repr__())
    return_to_menu()


def get_all_books():
    print(f"\n{Fore.RED}ALL BOOKS{Fore.RESET}")
    all_books = session.query(Book).order_by(Book.id)
    if all_books.count() == 0:
        print(f"\n{Fore.RED}No books found.{Fore.RESET}")
    for book in all_books:
        print(
            f"{book.id} | {Fore.GREEN}{book.title}{Fore.RESET} | {Fore.BLUE}{book.author}{Fore.RESET} | {Fore.LIGHTCYAN_EX}{book.date_published}{Fore.RESET} | {Fore.YELLOW}{book.price}{Fore.RESET}"
        )
    return_to_menu()


def search_for_book():
    book_ids = [book.id for book in session.query(Book).order_by(Book.id)]
    if len(book_ids) == 0:
        print(f"\n{Fore.RED}No books found.{Fore.RESET}")
        return_to_menu()
        return
    print(f"\nOptions: {book_ids}")
    book_id = input("What is the book's id? ")
    searched_book = session.query(Book).filter_by(id=int(book_id)).first()
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

    return_to_menu()


def book_analysis():
    books = session.query(Book).order_by(Book.date_published)
    if books.count() == 0:
        print("\nNo books in library.")
        return_to_menu()
        return
    try:
        print(f"\nNewest book: <{books[0].__repr__()}>")
        print(f"Oldest book: <{books[-1].__repr__()}>")
        print(f"Total Number of Books: {books.count()}")

        python_books = session.query(Book).filter(Book.title.ilike("%python%")).all()

        print(f"Total Number of Python Books: {len(python_books)}")
    except Exception as error:
        print("Error: ", error)

    return_to_menu()

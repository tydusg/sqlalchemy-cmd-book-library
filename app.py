from models import Base
from database import engine
from methods import add_book, get_all_books, search_for_book, book_analysis
from colorama import init, Fore
import time

init()


def app():
    library_on = True
    menu = f"""\n{Fore.CYAN}PROGRAMMING BOOKS{Fore.RESET}
            \r1) Add Book
            \r2) View all books
            \r3) Search for a book
            \r4) Book Analysis
            \r5) Exit\n"""
    while library_on:
        print(menu)
        choice = input("What would you like to do? "
        )
        if choice == "1":
            add_book()
        elif choice == "2":
            get_all_books()
        elif choice == "3":
            search_for_book()
        elif choice == "4":
            book_analysis()
        elif choice == "5":
            library_on = False
            print("Goodbye!")
            time.sleep(1)
        else:
            input(f"\n{Fore.RED}Sorry that's not a valid option.{Fore.RESET}\nPress 'ENTER' to try again. ")


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    app()

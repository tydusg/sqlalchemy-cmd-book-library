from models import Base
from database import engine
from methods import add_book, get_all_books, search_for_book, book_analysis
from colorama import init, Fore, Style

init()

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    library_on = True
    while library_on:
        library_function = input(
            f"\n{Fore.GREEN}PROGRAMMING BOOKS{Fore.RESET}\n1) Add Book\n2) View all books\n3) Search for a book\n4) Book Analysis\n5) Exit\n\nWhat would you like to do? "
        )
        if library_function == "1":
            add_book()
        elif library_function == "2":
            get_all_books()
        elif library_function == "3":
            search_for_book()
        elif library_function == "4":
            book_analysis()
        elif library_function == "5":
            library_on = False

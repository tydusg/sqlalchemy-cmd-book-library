from models import Base
from database import engine
from methods import add_book

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    library_on = True
    while library_on:
        library_function = input(
            "\nPROGRAMMING BOOKS\n1) Add Book\n2) View all books\n3)Search for a book\n4) Book Analysis\n5) Exit\n\nWhat would you like to do? "
        )
        if library_function == "1":
            add_book()
        elif library_function == "5":
            library_on = False

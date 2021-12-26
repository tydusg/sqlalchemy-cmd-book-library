from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    date_published = Column(String)
    price = Column(Float)

    def __repr__(self):
        return f"<Book(title={self.title}, author={self.author}, date_published={self.date_published}, price={self.price})>"

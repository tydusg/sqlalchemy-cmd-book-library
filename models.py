from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    date_published = Column(Date, nullable=False)
    price = Column(Float, nullable=False)

    def __repr__(self):
        return f"Title: {self.title}, Author: {self.author}, Published: {self.date_published}, Price: {self.price}"

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///books.db")
SessionLocal = sessionmaker(bind=engine)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import engine

# engine = create_engine("sqlite:///employees.db")
Session = sessionmaker(bind=engine)
session = Session()
""":type: sqlalchemy.orm.Session"""
import datetime
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///employees.db")
Base = declarative_base()


class Employee(Base):
    __tablename__ = "Employees"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    surname = Column("Surname", String)
    birthday = Column("Birthday", String)
    position = Column("Position", String)
    salary = Column("Salary", Integer)
    started = Column("Starting date", DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, surname, birthday, position, salary) -> None:
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.position = position
        self.salary = salary

    def __repr__(self):
        return f"{self.id} {self.name} {self.surname} {self.birthday} {self.position} {self.salary} {self.started}"


Base.metadata.create_all(engine)

"""Create a TO DO list application that runs in terminal. 
It should allow user to log in. Each user should have his own tasks in to do list. 
User should be able to add/ update/ delete tasks. 
User information and task information should be kept in database"""

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine("sqlite:///user_data.db")
Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    surname = Column("Surname", String)
    email = Column("Email", String)
    password = Column("Password", String)
    data = relationship("Data", back_populates="user")

    def __repr__(self):
        return f"{self.name} {self.surname} {self.email} {self.password}"


class Data(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True)
    type = Column("Type", String)
    attribute = Column("Attribute", String)
    attribute2 = Column("Attribute 2", String)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="data")

    def __repr__(self):
        return f"{self.type} {self.attribute} {self.attribute2}"


if __name__ == "__main__":
    Base.metadata.create_all(engine)

from main import Employee
from session import session

empl = [
    Employee(
        name="Laimonas",
        surname="Paura",
        birthday="1983-01-01",
        position="Junior Python Developer",
        salary=5000,
    ),
    Employee(
        name="Jonas",
        surname="Basanavicius",
        birthday="1962-01-01",
        position="Senior Python Developer",
        salary=15000,
    ),
    Employee(
        name="Antanas",
        surname="Fontanas",
        birthday="2000-01-01",
        position="Junior Java Developer",
        salary=4000,
    ),
    Employee(
        name="Petras",
        surname="Petraitis",
        birthday="1999-01-01",
        position="Junior PHP Developer",
        salary=3000,
    ),
]


session.add_all(empl)
session.commit()

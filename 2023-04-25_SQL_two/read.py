from main import Projektas
from session import session


# projektas1 = session.query(Projektas).get(1)

# print(projektas1.name)
# # Naujas pr.
projects = session.query(Projektas).filter_by(name="Naujas pr.").first()
print(projects)

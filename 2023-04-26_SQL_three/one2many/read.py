from models import Tevas, Vaikas
from session import session

tevas = session.query(Tevas).get(1)
for vaikas in tevas.vaikai:
    print(vaikas.vardas, vaikas.pavarde)

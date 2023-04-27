from models import Tevas, Vaikas
from session import session

vaikas = Vaikas(vardas="Naujas vaikas", pavarde="Tevaika")
tevas = session.query(Tevas).get(1)
tevas.vaikas = vaikas
session.commit()

from models import Tevas, Vaikas
from session import session

# vaikas = Vaikas(vardas="Vaikas", pavarde="Vaikaitis")
# vaikas2 = Vaikas(vardas="Vaikas 2", pavarde="Vaikaitis 2")
# tevas = Tevas(vardas="Tevas", pavarde="Vaikaitis")
# tevas.vaikai.append(vaikas)
# tevas.vaikai.append(vaikas2)
# session.add(tevas)
# session.commit()


tevas = session.query(Tevas).get(1)
vaikas = Vaikas(vardas="Vaikas 3", pavarde="Vaikaitis 3 ")
vaikas.tevas = tevas
session.add(vaikas)
session.commit()

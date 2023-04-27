from models import Tevas, Vaikas
from session import session


# vaikas = Vaikas(vardas="Vaikas", pavarde="Tevaika", mokymo_istaiga = "Čiurlionio gimnazija")
# tevas = Tevas(vardas="Tevas", pavarde="Tevaika", vaikas=vaikas)
# session.add(tevas)
# session.commit()

# tevas = Tevas(vardas="Antras Tevas", pavarde="Tevaika", vaikas_id=1)
# session.add(tevas)
# session.commit()

senas_vaikas = session.query(Vaikas).get(1)
tevas = Tevas(vardas="Antras Tevas", pavarde="Tevaika", vaikas=senas_vaikas)
session.add(tevas)
session.commit()


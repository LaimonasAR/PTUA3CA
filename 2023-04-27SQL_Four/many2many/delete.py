from models import Tevas, Vaikas
from session import session

# ----------------DELETE RELATIONSHIP--------------
# tevas = session.query(Tevas).get(2)
# vaikas1 = tevas.vaikai[0]
# tevas.vaikai.remove(vaikas1)  # deletes relationship
# session.commit()
# ----------------DELECE CHILD---------------------
tevas = session.query(Tevas).get(2)
vaikas1 = tevas.vaikai[0]
session.delete(vaikas1)
session.commit()

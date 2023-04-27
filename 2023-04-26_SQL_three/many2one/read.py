from models import Tevas, Vaikas
from session import session

tevas = session.query(Tevas).get(1)
print(tevas.vaikas.vardas)

vaikas = session.query(Vaikas).get(1)
# print(vaikas.tevai[0].vardas)
for tevas in vaikas.tevai:
    print(tevas.vardas)

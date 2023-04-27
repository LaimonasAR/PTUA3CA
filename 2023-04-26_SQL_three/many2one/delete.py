from models import Tevas
from session import session


tevas = session.query(Tevas).get(1)
session.delete(tevas)
session.commit()

from config import Session ,engine
from tables import User

session = Session()

u = User(name="ahmad", age=20)
session.add(u)
session.commit()
session.close()

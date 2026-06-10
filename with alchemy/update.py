from config import Session
from tables import User

session = Session()

u = session.query(User).filter_by(id=1).first()

u.age = 21

session.commit()
session.close()
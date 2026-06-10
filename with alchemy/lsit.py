from config import Session
from tables import User

session = Session()

users = session.query(User).all()
for user in users:
    print(user.name)
    print(user.age)
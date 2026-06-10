from sqlalchemy import Integer, String, Column
from config import Base, engine, Session

class User(Base):
    __tablename__ = "users23"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine)